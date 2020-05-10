import numpy as np
# import root_numpy
import pandas as pd
import matplotlib.pyplot as plt
from os import path

from itertools import cycle
from scipy import interp
from sklearn.metrics import roc_curve, auc

#import user defined functions
from plotFunctions import plotROCcurves, plotLoss, plotPrecision
from prepData import makeData#, expandList


# from scipy import interp
# from itertools import cycle
# from sklearn.metrics import roc_curve, auc

from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support

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
# dyjets = makeData('DYJetsToLL2018_MINI_numEvent100000.root',definedIds)
# qcd = makeData('QCD_pt_600to800_2018_MINI_numEvent100000.root',definedIds)
# ttjets = makeData('TTJets2018_MINI_numEvent100000.root',definedIds)

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





#normalize data
norm = MinMaxScaler()
data = norm.fit_transform(data)

#create test/train split - try soft cut-based ID first (least columns)
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = .3, random_state=1, shuffle=True)








# #convert everything to numpy arrays to feed into network
# x_train = x_train.to_numpy()
# x_test = x_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

y_train = np.array([np.array(i) for i in y_train])
y_test = np.array([np.array(i) for i in y_test])

###### unit testing ######
# x_train = x_train[:2]
# y_train = y_train[:2]



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

history = model.fit(x_train,y_train,batch_size=256,epochs=70,validation_split=0.3)

#STARTS TO OVERFIT AROUND EPOCH 10 - MAYBE INDUCE SOME REGULARIZATION??

plotName = 'softMVAvars_evenSampling_dyjets+qcd+ttjets'
plotLoss(history,plotName)


y_predProbs = model.predict(x_test) #need probabilites for ROC curve
plotROCcurves(y_test,y_predProbs,definedIds,plotName)

y_predClasses = enc.inverse_transform(y_predProbs) #need classes for confusion matrix/precison by class

#gives precision (efficiency) of each class
precision, _, _, _ = precision_recall_fscore_support(y_test,y_predClasses)


#match to pt in x_test to plot as function of pt
#bin x_test in pt
# bins = np.linspace(x_test['Muon_pt'].min(),x_test['Muon_pt'].max(),int(x_test['Muon_pt'].max() - x_test['Muon_pt'].min()))
# bins = bins.round(3)
# x_test['bins'] = pd.cut(x_test['Muon_pt'],bins)
# precision_pt = []
# for i, Bin in enumerate(bins):
# 	if Bin == bins[-1]:
# 		break
# 	left = x_test['Muon_pt'] > bins[i]
# 	right = x_test['Muon_pt'] < bins[i+1]

# 	x_testSubset = x_test[left & right]
# 	idxs = x_testSubset.index.to_numpy()
# 	y_testSubset = y_test.loc[idxs]

# 	y_predProbsSubset = model.predict(x_testSubset)

# 	y_predClassesSubset = enc.inverse_transform(y_predProbsSubset)
# 	precision, _, _, _ = precision_recall_fscore_support(y_testSubset,y_predClassesSubset,average=None)
	
# 	precision_pt.append(precision)


passedHists = [TH1D("num_"+str(i), "label "+str(ID), 41, -0.5, 40.5 ) for i,ID in enumerate(definedIds)]
totalHists =  [TH1D("den_"+str(i), "label "+str(ID), 41, -0.5, 40.5 ) for i,ID in enumerate(definedIds)]

#break it down by class
for j, ID in enumerate(definedIds):
	for i, n in enumerate(zip(y_test,y_predClasses)):
		if n[0] == ID:
			if n[0] == n[1]: #correct match
				passedHists[j].Fill(x_test['Muon_pt'].loc[i])
				totalHists[j].Fill(x_test['Muon_pt'].loc[i])
			elif n[0] != n[1]: #incorrect match
				totalHists[j].Fill(x_test['Muon_pt'].loc[i])



goodEff = [ TEfficiency(passedHists[i],totalHists[i]) for i in range(nClasses) ]


outfile = TFile("./test.root","RECREATE")
[ outfile.WriteTObject(x) for x in goodEff ]






# plotPrecision(history,plotName)











