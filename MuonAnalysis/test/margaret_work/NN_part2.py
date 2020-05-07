import numpy as np
import root_numpy
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.activations import relu


treeName = 'Events'
gPath = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/'
tmp = root_numpy.root2array(gPath+'DYJetsToLL2018_MINI_numEvent100.root',treeName)
data = pd.DataFrame(tmp)

def expandList(df, columnNames):
	outDf = pd.DataFrame()
	for col in columnNames:
		arr = pd.Series(np.array([j for i in df[col] for j in i]))
		outDf[col] = arr
	return outDf




#only keep the variables we want - labels and input

#soft MVA
softMVA = data[['Muon_genPartFlav','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
		'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
		'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
		'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
		'Muon_outerTrackCharge','Muon_innerTrackCharge']]

#lepton MVA
lepMVA = data[['Muon_genPartFlav','Muon_pt','Muon_eta','Muon_dxy','Muon_dz',
			'Muon_sip3d','Muon_segmentComp','Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
			'Jet_btagCSVV2']] #need jet ptRel and jet ptRatio

#soft cut-based ID
softID = data[['Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
				'Muon_nPixelLayers']]



#get rid of 0 muon events
data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])

#expand the list so each row is a muon (not an event)
data = expandList(data,['Muon_genPartFlav','Muon_pt','Muon_eta','Muon_dxy','Muon_dz','Muon_sip3d','Muon_segmentComp'])

#remove unmatched muons
data = data.drop([i for i, flav in enumerate(data['Muon_genPartFlav']) if flav == 0])

#separate labels from input variables
target = data['Muon_genPartFlav']
data = data.drop(columns = 'Muon_genPartFlav')


#one hot encode the labels - make dictionary 
encode_genPartFlav = {1: [1,0,0,0], 5: [0,1,0,0], 15: [0,0,1,0], 4: [0,0,0,1], 3: [0,0,0,1]}
#1: prompt, 5: b, 15: tau, 3 + 4: other (3: light, 4: c)
nClasses = 5
target = target.map(encode_genPartFlav)


#create test/train split - try soft cut-based ID first (least columns)
x_train, x_test, y_train, y_test = train_test_split(softID, target, test_size = .3, random_state=1)


#convert everything to numpy arrays to feed into network
x_train = x_train.to_numpy()
x_test = x_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

y_train = np.array([np.array(i) for i in y_train])
y_test = np.array([np.array(i) for i in y_test])


#build network here
inputs = Input(shape=x_train[0].shape)
x = Dense(128,activation='relu')(inputs)
x = Dense(128,activation='relu')(x)
x = Dense(128,activation='relu')(x)
x = Dense(128,activation='relu')(x)
x = Dense(128,activation='relu')(x)
outputs = Dense(nClasses,activation='softmax')(x)

model = Model(inputs=inputs,outputs=outputs)

model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.0001),metrics=['accuracy'])
# model.summary()


model.fit(x_train,y_train,batch_size=256,epochs=10)




