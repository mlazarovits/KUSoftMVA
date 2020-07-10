import numpy as np
import root_numpy
import pandas as pd
import sys
# from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import *
from keras.optimizers import SGD, Adam
from keras.activations import relu
np.set_printoptions(threshold=sys.maxsize)
from keras import layers
from sklearn.utils import shuffle

treeName = 'Events'

#take in all samples (dy, tt, qcd) and shuffle for unmatched (sample evenly for other categories)
gPath = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/'
tmp = root_numpy.root2array(gPath+'DYJetsToLL2018_MINI_numEvent100000.root',treeName)
data = pd.DataFrame(tmp)
#print(data)
#print(data['GenPart_pdgId'])
#expand list in terms of muon
def expandList(df, columnNames):
	outDf = pd.DataFrame()
	for col in columnNames:
		arr = pd.Series(np.array([j for i in df[col] for j in i]))
		outDf[col] = arr
	return outDf


#make gen pdg ID labels for reco muons
#-999 if unmatched
pdgIds = [-999 if mu == -1 else data['GenPart_pdgId'][i][mu] for i, idxs in enumerate(data['Muon_genPartIdx']) for j, mu in enumerate(idxs)]
pdgIds = np.array(pdgIds)
#print(pdgIds)


#make jet btag CSVV2 column
btags = [-999 if mu == -1 else data['Jet_btagCSVV2'][i][mu] for i, idxs in enumerate(data['Muon_jetIdx']) for j, mu in enumerate(idxs)]
btags = np.array(btags)


#get rid of 0 muon events
data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])
#print(data)
#data = data.drop([i for i, p in enumerate(data['GenPart_pdgId']) if np.logical_or( abs(p) != 13, p != -999).any() ])
#print(data)
#for i, p in enumerate(data['GenPart_pdgId']):
#	print(i,p)

#expand the list so each row is a muon (not an event)
muonMask = data.columns.str.contains('Muon_.*')
expCols = data.loc[:,muonMask].columns
data = expandList(data, expCols)

#print(data.head)


#add in gen pgdIds and jet btags of reco muons
data['Muon_genPdgId'] = pdgIds
data['Jet_btagCSVV2'] = btags


maxloop = 30
for i, p in enumerate(data['Muon_genPdgId']):
        print(i,p)
	#print( if(abs(p)!=13 or p!=-999) )
        if i > 30:
                break
ndata= 30000

print("before drop")
#print(data)
#data = data.drop([i for i, p in enumerate(data['Muon_genPdgId']) if np.logical_or( abs(p) != 13, p != -999).any()])
#data = data.drop([i for i,p in enumerate( data['Muon_genPdgId']) if (abs(p)!=13 or p!=-999 )] )
print("dropping")
data1 = data[abs(data.Muon_genPdgId) == 13]
data2 = data[data.Muon_genPdgId == -999]
print("shape d1", data1.shape)
print("shape d2", data2.shape)
data1 = data1[:ndata]
data2= data2[:ndata]
print("d1 ")
#print(data1)
print("d2 ")
#print(data2)
data = pd.concat([data1, data2])
print("after drop")
#print(data)
print("after print")
#data = shuffle(data)
#only keep the variables we want - labels and input
#soft MVA
softMVA = data[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge']]

#lepton MVA
lepMVA = data[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_dxy','Muon_dz',
			'Muon_sip3d','Muon_segmentComp','Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
			'Jet_btagCSVV2']] #need jet ptRel and jet ptRatio


#soft cut-based ID
softID = data[['Muon_genPdgId','Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
				'Muon_nPixelLayers']]
#print(softID)


customID1 = data[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_dxy','Muon_dz',
                        'Muon_sip3d','Muon_segmentComp','Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
                        'Jet_btagCSVV2','Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
                                'Muon_nPixelLayers']]


#separate labels from input variables
target = data['Muon_genPdgId']
#take absolute value of gen PDG ID
target = abs(target)
#drop this column from data
data = data.drop(columns = 'Muon_genPdgId')


#define classes
#classes are:
#13: actual mu, 211: pi^+\-, 11: e, 321: K^+\-,  
#2212: p^+, other, 999: unmatched

#definedIds = [13,211,11,321,2212,999]
definedIds = [13,999]
#otherIds = [i for i in target.unique() if i not in definedIds]
#nClasses = len(definedIds) + 1
nClasses = len(definedIds)

#one hot encode the labels - make dictionary of classes for part I
#encode_genPdgId = {13: [1,0,0,0,0,0,0], 211: [0,1,0,0,0,0,0], 11: [0,0,1,0,0,0,0], 
#		321: [0,0,0,1,0,0,0], 2212: [0,0,0,1,0,0,0], 999: [0,0,0,0,0,1,0]}
encode_genPdgId = {13: [1,0], 999: [0,1]}


#add entry for 'other' classes
#for i in otherIds:
#	encode_genPdgId[i] = [0,0,0,0,0,1,0]


target = target.map(encode_genPdgId)
print(target)


#create test/train split - try soft cut-based ID first (least columns)
#x_train, x_test, y_train, y_test = train_test_split(softID, target, test_size = .3, random_state=1)
x_train, x_test, y_train, y_test = train_test_split(softMVA, target, test_size= .3, random_state=1)

#convert everything to numpy arrays to feed into network
x_train = x_train.to_numpy()
x_test = x_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

y_train = np.array([np.array(i) for i in y_train])
y_test = np.array([np.array(i) for i in y_test])



inputs = Input(shape=(x_train.shape[1],), name='digits')
x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
x = layers.Dense(64, activation='relu', name='dense_2')(x)
outputs = layers.Dense(2, name='predictions')(x)

model = Model(inputs=inputs, outputs=outputs)
model.summary()

"""

nneuronold = 128
nneuron= 50
#build network here
inputs = Input(shape=x_train[0].shape)
x = Dense(nneuron,activation='relu')(inputs)
x = Dense(nneuron,activation='relu')(x)
x = Dense(nneuron,activation='relu')(x)
x = Dense(nneuron,activation='relu')(x)
x = Dense(nneuron,activation='relu')(x)
outputs = Dense(nClasses,activation='softmax')(x)

model = Model(inputs=inputs,outputs=outputs)

optold=0.0001
optnew=0.001
model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=optnew),metrics=['accuracy'])
model.summary()


model.fit(x_train,y_train,batch_size=32,epochs=10)
"""

"""
nneuron = 128
n_feature = x_train.shape[1]
model = Sequential()
model.add(Dense(nneuron,activation='relu', input_shape=(n_feature,)))
model.add(Dense(nneuron,activation='relu'))
model.add(Dense(nneuron,activation='relu'))
model.add(Dense(nneuron,activation='relu'))
model.add(Dense(nClasses,activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
model.summary()
model.fit(x_train,y_train,batch_size=32,epochs=10)
"""


"""
n_features = x_train.shape[1]
model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=150, batch_size=32, verbose=0)
loss, acc = model.evaluate(X_test, y_test, verbose=0)
"""

"""

inputs2 = Input(shape=x_train[0].shape)
x2 = Dense(nneuron,activation='relu')(inputs)
x2 = Dense(nneuron,activation='relu')(x2)
x2 = Dense(nneuron,activation='relu')(x2)
x2 = Dense(nneuron,activation='relu')(x2)
x2 = Dense(nneuron,activation='relu')(x2)
outputs2 = Dense(nClasses,activation='softmax')(x2)

model2 = Model(inputs=inputs2,outputs=outputs2)
model2.compile(loss='categorical_crossentropy', optimizer=Adam(lr=optnew),metrics=['accuracy'])
model2.summary()
model2.fit(x_train,y_train,batch_size=256,epochs=10)
"""
