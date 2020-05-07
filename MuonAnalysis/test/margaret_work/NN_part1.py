import numpy as np
# import root_numpy
import pandas as pd
import matplotlib.pyplot as plt

#import user defined functions
from plotFunctions import plotROCcurves, plotLoss
from prepData import makeData, expandList


# from scipy import interp
# from itertools import cycle
# from sklearn.metrics import roc_curve, auc

# from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import *
from keras.optimizers import SGD, Adam
from keras.activations import relu





#define classes
#classes are:
#13: actual mu, 211: pi^+\-, 321: K^+\-,  
#2212: p^+, other, 999: unmatched
definedIds = [13,211,321,2212,999]
nClasses = len(definedIds)


#take in all samples (dy, tt, qcd) and shuffle for unmatched (sample evenly for other categories)
#get dataframes for dyjets and qcd samples
dyjets = makeData('DYJetsToLL2018_MINI_numEvent100000.root',definedIds)
qcd = makeData('QCD_pt_600to800_2018_MINI_numEvent100000.root',definedIds)

# TRY SAMPLING EACH CLASS RANDOMLY FROM DYJETS AND QCD (SAMPLE UNMATCHED BIN EVENLY)
# SO THAT EACH CLASS HAS AN EVEN NUMBER OF MUONS

#sample 2k muons randomly from each class
unmatchedSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 999].sample(n=1000),qcd[abs(qcd['Muon_genPdgId']) == 999].sample(n=1000)],ignore_index=True)
muonSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 13].sample(n=1000),qcd[abs(qcd['Muon_genPdgId']) == 13].sample(n=1000)], ignore_index=True)

#uneven sampling over MC samples based on how many objects are in each MC sample (dyjets has low number of protons, pions, and kaons)
protonSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 2212].sample(n=500),qcd[abs(qcd['Muon_genPdgId']) == 2212].sample(n=1500)], ignore_index=True)
pionSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 211].sample(n=500),qcd[abs(qcd['Muon_genPdgId']) == 211].sample(n=1500)], ignore_index=True)
kaonSubset = pd.concat([dyjets[abs(dyjets['Muon_genPdgId']) == 321].sample(n=300),qcd[abs(qcd['Muon_genPdgId']) == 321].sample(n=1700)], ignore_index=True)



#even sampling from dyjets and qcd - 20k muons each
# allSamples = pd.concat([dyjets.sample(n=20000),qcd.sample(n=20000)],ignore_index=True)

#even sampling across classes - 2k muons each
allSamples = pd.concat([unmatchedSubset,muonSubset,protonSubset,pionSubset,kaonSubset],ignore_index=True)


#separate labels from input variables
target = allSamples['Muon_genPdgId']
#take absolute value of gen PDG ID
target = abs(target)
#one hot encode the labels - make dictionary of classes for part I
encode_genPdgId = {13: [1,0,0,0,0], 211: [0,1,0,0,0], 
		321: [0,0,1,0,0], 2212: [0,0,0,1,0], 999: [0,0,0,0,1]}
target = target.map(encode_genPdgId)
#drop this column from data
allSamples = allSamples.drop(columns = 'Muon_genPdgId')



#only keep the variables we want - labels and input
#soft MVA
softMVA = allSamples[['Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge']]


#soft cut-based ID
softID = allSamples[['Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
				'Muon_nPixelLayers']]





print('Relative Frequencies of Classes (total):')
print(target.value_counts(normalize=True))



#create test/train split - try soft cut-based ID first (least columns)
x_train, x_test, y_train, y_test = train_test_split(softID, target, test_size = .3, random_state=1, shuffle=True)
print('Relative Frequencies of Classes (training):')
print(y_train.value_counts(normalize=True))




# #convert everything to numpy arrays to feed into network
x_train = x_train.to_numpy()
x_test = x_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

y_train = np.array([np.array(i) for i in y_train])
y_test = np.array([np.array(i) for i in y_test])

###### unit testing ######
x_train = x_train[:15]
y_train = y_train[:15]




# #build network here
inputs = Input(shape=x_train[0].shape)
x = Dense(128,activation='relu')(inputs)
x = Dense(128,activation='relu')(x)
x = Dense(128, activation='relu')(x)
x = Dense(128,activation='relu')(x)
x = Dense(128,activation='relu')(x)
outputs = Dense(nClasses,activation='softmax')(x)

model = Model(inputs=inputs,outputs=outputs)

model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.001),metrics=['accuracy'])
model.summary()

history = model.fit(x_train,y_train,batch_size=256,epochs=10,validation_split=0.3)

# plotName = 'evenSampling_dyjets+qcd'
# plotLoss(history,plotName)

# y_pred = model.predict(y_test)

# plotROCcurves(y_test,y_pred,nClasses,plotName)







