import numpy as np
# import root_numpy
import pandas as pd
import matplotlib.pyplot as plt
from os import path

# from itertools import cycle
# from scipy import interp
# from sklearn.metrics import roc_curve, auc

#import user defined functions
from plotFunctions import plotROCcurves, plotLoss, makeEfficiency
from prepData import makeData#, expandList


from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
# from sklearn.metrics import precision_recall_fscore_support

from keras.models import Sequential, Model
from keras.layers import *
from keras.optimizers import SGD, Adam
from keras.activations import relu
from keras.metrics import Precision
print('Packages Loaded')



#define classes
#classes are:
#13: actual mu, 211: pi^+\-, 321: K^+\-,  
#2212: p^+, other, 999: unmatched
definedIds = np.array([13,211,321,2212,999])
nClasses = len(definedIds)

#take in all samples (dy, tt, qcd) and shuffle for unmatched (sample evenly for other categories)
#get dataframes for dyjets and qcd samples

if path.exists('DYJetsToLL2018_MINI_numEvent100000.csv'):
	dyjets = pd.read_csv('DYJetsToLL2018_MINI_numEvent100000.csv')
else:
	dyjets = makeData('DYJetsToLL2018_MINI_numEvent100000',definedIds)


if path.exists('TTJets2018_MINI_numEvent100000.csv'):
	ttjets = pd.read_csv('TTJets2018_MINI_numEvent100000.csv')
else:
	ttjets = makeData('TTJets2018_MINI_numEvent100000',definedIds)

if path.exists('QCD_pt_600to800_2018_MINI_numEvent100000.csv'):
	qcd = pd.read_csv('QCD_pt_600to800_2018_MINI_numEvent100000.csv')
else:
	qcd = makeData('QCD_pt_600to800_2018_MINI_numEvent100000',definedIds)


#sample 3k muons randomly from each MC sample for unmatched and true muons
unmatchedSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 999].sample(n=1000),qcd[abs(qcd['Muon_genPdgId']) == 999].sample(n=1000),ttjets[abs(ttjets['Muon_genPdgId']) == 999].sample(n=1000)],ignore_index=True)
muonSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 13].sample(n=1000),qcd[abs(qcd['Muon_genPdgId']) == 13].sample(n=1000),ttjets[abs(ttjets['Muon_genPdgId']) == 13].sample(n=1000)], ignore_index=True)

#uneven sampling over MC samples based on how many objects are in each MC sample (dyjets has low number of protons, pions, and kaons)
protonSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 2212].sample(n=500),qcd[abs(qcd['Muon_genPdgId']) == 2212].sample(n=1500),ttjets[abs(ttjets['Muon_genPdgId']) == 2212].sample(n=1000)], ignore_index=True)
pionSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 211].sample(n=500),qcd[abs(qcd['Muon_genPdgId']) == 211].sample(n=1500),ttjets[abs(ttjets['Muon_genPdgId']) == 211].sample(n=1000)], ignore_index=True)
kaonSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 321].sample(n=300),qcd[abs(qcd['Muon_genPdgId']) == 321].sample(n=1700),ttjets[abs(ttjets['Muon_genPdgId']) == 321].sample(n=1000)], ignore_index=True)


#even sampling across classes - 3k muons each
allSamples = pd.concat([unmatchedSubset,muonSubset,protonSubset,pionSubset,kaonSubset],ignore_index=True)



#only keep the variables we want - labels and input
#soft MVA
softMVA = allSamples[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge']]


#soft cut-based ID
softID = allSamples[['Muon_genPdgId','Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
				'Muon_nPixelLayers']]


#choose which variables to train with
data = softMVA
#separate labels from input variables and take absolute value of gen PDG ID
target = abs(data['Muon_genPdgId'])

#one hot encode the labels
#define classes
#classes are:
#13: actual mu, 211: pi^+\-, 321: K^+\-,  
#2212: p^+, other, 999: unmatched


enc = OneHotEncoder(sparse=False)
# encode_genPdgId = {13: [1,0,0,0,0], 211: [0,1,0,0,0], 
		# 321: [0,0,1,0,0], 2212: [0,0,0,1,0], 999: [0,0,0,0,1]}
# target = target.map(encode_genPdgId)

print('Relative Frequencies of Classes (total):')
print(target.value_counts(normalize=True))


enc.fit(definedIds.reshape(-1,1))		
target = enc.transform(target.to_numpy().reshape(-1,1))

#drop this column from data
data = data.drop(columns = 'Muon_genPdgId')

#make separate pt column for unnormalize pt to use in efficiency analysis
effPt = data['Muon_pt']



#normalize data
norm = MinMaxScaler()
data = norm.fit_transform(data)

#create test/train split
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = .3, random_state=1, shuffle=True)
_, pt_test, _, _ = train_test_split(effPt, target,test_size = .3, random_state=1,shuffle=True)


#convert 1hot encoding to numpy arrays
y_train = np.array([np.array(i) for i in y_train])
y_test = np.array([np.array(i) for i in y_test])



#build network here
inputs = Input(shape=x_train[0].shape)
x = Dense(64,activation='relu')(inputs)
x = Dense(64,activation='relu')(x)
x = Dense(64,activation='relu')(x)
x = Dense(64,activation='relu')(x)
# x = Dense(128,activation='relu')(x)
# x = Dense(128,activation='relu')(x)
# x = Dense(64, activation='relu')(x)
outputs = Dense(nClasses,activation='softmax')(x)

model = Model(inputs=inputs,outputs=outputs)

model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=1e-3),metrics=['accuracy',Precision()])
model.summary()

history = model.fit(x_train,y_train,batch_size=256,epochs=50,validation_split=0.3)


plotName = 'softMVAvars_evenSampling_dyjets+qcd+ttjets'
plotLoss(history,plotName)


y_predProbs = model.predict(x_test) #need probabilites for ROC curve
plotROCcurves(y_test,y_predProbs,definedIds,plotName)

#transform predictions and labels from 1hot to categorical for efficiency analysis
y_predClasses = enc.inverse_transform(y_predProbs) 
y_testClasses = enc.inverse_transform(y_test)



makeEfficiency(y_testClasses, y_predClasses, pt_test, definedIds,plotName)













