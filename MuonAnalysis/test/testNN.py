import numpy as np
import root_numpy
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.activations import relu


treeName = 'Events'
gPath = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/'
tmp = root_numpy.root2array(gPath+'DYJetsToLL2018_MINI_numEvent200.root',treeName)
data = pd.DataFrame(tmp)

def expandList(df, columnNames):
	outDf = pd.DataFrame()
	for col in columnNames:
		arr = pd.Series(np.array([j for i in df[col] for j in i]))
		outDf[col] = arr
	return outDf


#get rid of 0 muon events
arr = [i for i in range(data.shape[0]) if data['nMuon'][i] == 0]

#only keep the variables we want - labels and input
data = data['Muon_genPartFlav','Muon_pt','Muon_eta','Muon_dxy','Muon_dz',
			'Muon_sip3d','Muon_segmentComp']
# still need:
# selected track multiplicity of the jet matched to the lepton (see below for the applied requirements)
# mini-isolation, charged component (include only charged hadrons in the isolation sum)
# mini-isolation, neutral component (neutral hadrons + photons)
# ptRel: the same variable used in multiIso, using the LepAware JEC approach (def. slides)
# ptRatio: the same variable used in multiIso, using the LepAware JEC approach (def. slides)
# CSVv2 b-tagging discriminator of the jet matched to the lepton

#expand the list so each row is a muon (not an event)
data = expandList(data,['Muon_genPartFlav','Muon_pt','Muon_eta','Muon_dxy','Muon_dz','Muon_sip3d','Muon_segmentComp'])

#remove unmatched muons
for i in range(data['Muon_genPartFlav'].shape[0]):
	if data['Muon_genPartFlav'][i] == 0:
		data = data.drop(i)

#separate labels from input variables
target = data['Muon_genPartFlav']
data = data.drop(columns = 'Muon_genPartFlav')


#one hot encode the labels - make dictionary 
encode_genPartFlav = {1: [1,0,0,0], 5: [0,1,0,0], 15: [0,0,1,0], 4: [0,0,0,1], 3: [0,0,0,1]}
#1: prompt, 5: b, 15: tau, 3 + 4: other (3: light, 4: c)
target = target.map(encode_genPartFlav)


#build network here
model = Sequential()
model.add(Dense(64,activation='relu',input_dim=nVar))
model.add(Dense(64,activation='relu'))
model.add(Dense(2,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer=Adam(),metrics=['accuracy'])
model.summary()

#...etc...




