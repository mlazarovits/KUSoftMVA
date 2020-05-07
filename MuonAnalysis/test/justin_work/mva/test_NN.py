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
#from sklearn  import preprocessing
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

#get rid of 0 muon events
data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])
#expand the list so each row is a muon (not an event)
muonMask = data.columns.str.contains('Muon_.*')
expCols = data.loc[:,muonMask].columns
data = expandList(data, expCols)


#add in gen pgdIds and jet btags of reco muons
data['Muon_genPdgId'] = pdgIds

#collect n matched and umatched
ndata = 30000
data1 = data[abs(data.Muon_genPdgId) == 13]
data2 = data[data.Muon_genPdgId == -999]
data1 = data1[:ndata]
data2= data2[:ndata]
data = pd.concat([data1, data2])
data = shuffle(data)
#normalize
#test = data.values
#min_max_scaler = preprocessing.MinMaxScaler()
#test_scaled = min_max_scaler.fit_transform(test)
#data = pd.DataFrame(test_scaled)




#data = shuffle(data)

#only keep the variables we want - labels and input
#soft MVA
#softID = data[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
#'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
#'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
#'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
#'Muon_outerTrackCharge','Muon_innerTrackCharge']]

#lepton MVA
#lepMVA = data[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_dxy','Muon_dz',
#			'Muon_sip3d','Muon_segmentComp','Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
#			'Jet_btagCSVV2']] #need jet ptRel and jet ptRatio


#soft cut-based ID
#softID = data[['Muon_genPdgId','Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
#				'Muon_nPixelLayers']]

#customID1 = data[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_dxy','Muon_dz',
 #                       'Muon_sip3d','Muon_segmentComp','Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
  #                      'Jet_btagCSVV2','Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
   #                             'Muon_nPixelLayers']]


softID = data[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge',
'Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
'Muon_isGood','Muon_isHighPurity','Muon_nPixelLayers']]


#separate labels from input variables
target = softID['Muon_genPdgId']
#take absolute value of gen PDG ID
target = abs(target)
#drop this column from data
#data = data.drop(columns = 'Muon_genPdgId')
softID = softID.drop(columns='Muon_genPdgId')

#define classes
#classes are:
#13: actual mu, 211: pi^+\-, 11: e, 321: K^+\-,  
#2212: p^+, other, 999: unmatched

definedIds = [13,999]
Classes = len(definedIds)

#one hot encode the labels - make dictionary of classes for part I
#encode_genPdgId = {13: [1,0,0,0,0,0,0], 211: [0,1,0,0,0,0,0], 11: [0,0,1,0,0,0,0], 

#		321: [0,0,0,1,0,0,0], 2212: [0,0,0,1,0,0,0], 999: [0,0,0,0,0,1,0]}
encode_genPdgId = {13: [1,0], 999: [0,1]}



target = target.map(encode_genPdgId)


#print("data")
#print(data)

#print("softid")
#print(softID)

print("norm softid")
softID = (softID-softID.mean())/softID.std()
#print(softID)

#print("target")
#print(target)
#create test/train split - try soft cut-based ID first (least columns)
x_train, x_test, y_train, y_test = train_test_split(softID, target, test_size = .1, random_state=1)


#x_train, x_test, y_train, y_test = train_test_split(softMVA, target, test_size= .3, random_state=1)

#convert everything to numpy arrays to feed into network
x_train = x_train.to_numpy()
x_test = x_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

y_train = np.array([np.array(i) for i in y_train])
y_test = np.array([np.array(i) for i in y_test])

#print("x_Train")
#print(x_train)
#print("Y_train")
#print(y_train)

#print("x_test")
#print(x_test)
#print("y_test")
#print(y_test)



#### MODEL TYPE 1
"""
n_features = x_train.shape[1]
# define model
model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(2, activation='softmax'))
# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# fit the model
model.fit(x_train, y_train, epochs=100, batch_size=256,validation_split=0.1)
model.summary()
"""
####

#### MODEL TYPE 2

n_features = x_train.shape[1]
# define model
model = Sequential()
model.add(Dense(128, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))

model.add(Dense(Classes, activation='softmax'))
# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# fit the model
model.fit(x_train, y_train, epochs=100, batch_size=256,validation_split=0.1)
model.summary()

####


#### MODEL TYPE 3
'''
n_features = x_train.shape[1]
# define model
model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(2, activation='sigmoid'))
# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# fit the model
model.fit(x_train, y_train, epochs=100, batch_size=256,validation_split=0.1)
model.summary()
'''
####

"""
inputs = Input(shape=(x_train.shape[1],), name='digits')
x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
x = layers.Dense(64, activation='relu', name='dense_2')(x)
outputs = layers.Dense(2, name='predictions')(x)

model = Model(inputs=inputs, outputs=outputs)
model.summary()
"""
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
#optnew=0.001
model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=optnew),metrics=['accuracy'])
model.summary()


model.fit(x_train,y_train,batch_size=32,epochs=10)
"""
