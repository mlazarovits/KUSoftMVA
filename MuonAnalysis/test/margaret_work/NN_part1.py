import numpy as np
import root_numpy
import pandas as pd
import matplotlib.pyplot as plt

# from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import *
from keras.optimizers import SGD, Adam
from keras.activations import relu



treeName = 'Events'

#take in all samples (dy, tt, qcd) and shuffle for unmatched (sample evenly for other categories)
gPath = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/'
# dyjets = root_numpy.root2array(gPath+'DYJetsToLL2018_MINI_numEvent100000.root',treeName)
# dyjets = pd.DataFrame(dyjets)

# qcd = root_numpy.root2array(gPath+'QCD_pt_600to800_2018_MINI_numEvent100000.root',treeName)
# qcd = pd.DataFrame(qcd)

#expand list in terms of muon
def expandList(df, columnNames):
	outDf = pd.DataFrame()
	for col in columnNames:
		arr = pd.Series(np.array([j for i in df[col] for j in i]))
		outDf[col] = arr
	return outDf

def prepData(filename):
	data = root_numpy.root2array(gPath+filename,treeName)
	data = pd.DataFrame(data)
	#make gen pdg ID labels for reco muons
	#-999 if unmatched
	pdgIds = [-999 if mu == -1 else data['GenPart_pdgId'][i][mu] for i, idxs in enumerate(data['Muon_genPartIdx']) for j, mu in enumerate(idxs)]
	pdgIds = np.array(pdgIds)

	#make jet btag CSVV2 column
	btags = [-999 if mu == -1 else data['Jet_btagCSVV2'][i][mu] for i, idxs in enumerate(data['Muon_jetIdx']) for j, mu in enumerate(idxs)]
	btags = np.array(btags)


	#get rid of 0 muon events
	data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])

	#expand the list so each row is a muon (not an event)
	muonMask = data.columns.str.contains('Muon_.*')
	expCols = data.loc[:,muonMask].columns
	data = expandList(data, expCols)

	#add in gen pgdIds and jet btags of reco muons
	data['Muon_genPdgId'] = pdgIds
	data['Jet_btagCSVV2'] = btags

	#drop muons with pt < 2
	data = data.drop([i for i, pt in enumerate(data['Muon_pt']) if pt < 2])
	return data

	

#get dataframes for dyjets and qcd samples
dyjets = prepData('DYJetsToLL2018_MINI_numEvent100000.root')
qcd = prepData('QCD_pt_600to800_2018_MINI_numEvent100000.root')


#sample 20k muons from each sample set
dyjetsSubset = dyjets.sample(n=20000)
qcdSubset = qcd.sample(n=20000)

allSamples = pd.concat([dyjetsSubset,qcdSubset],ignore_index=True)





#only keep the variables we want - labels and input
#soft MVA
softMVA = allSamples[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge']]

#lepton MVA - use LepGood variables
lepMVA = allSamples[['Muon_genPdgId','Muon_pt','Muon_eta','Muon_dxy','Muon_dz',
			'Muon_sip3d','Muon_segmentComp','Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
			'Jet_btagCSVV2']] #need jet ptRel and jet ptRatio


#soft cut-based ID
softID = allSamples[['Muon_genPdgId','Muon_isGood','Muon_nTrackerLayersWithMeasurement','Muon_isHighPurity',
				'Muon_nPixelLayers']]


#separate labels from input variables
target = allSamples['Muon_genPdgId']
#take absolute value of gen PDG ID
target = abs(target)
#drop this column from data
allSamples = allSamples.drop(columns = 'Muon_genPdgId')

#define classes
#classes are:
#13: actual mu, 211: pi^+\-, 11: e, 321: K^+\-,  
#2212: p^+, other, 999: unmatched

definedIds = [13,211,11,321,2212,999]
otherIds = [i for i in target.unique() if i not in definedIds]
nClasses = len(definedIds) + 1

#one hot encode the labels - make dictionary of classes for part I
encode_genPdgId = {13: [1,0,0,0,0,0,0], 211: [0,1,0,0,0,0,0], 11: [0,0,1,0,0,0,0], 
		321: [0,0,0,1,0,0,0], 2212: [0,0,0,1,0,0,0], 999: [0,0,0,0,0,1,0]}

#add entry for 'other' classes
for i in otherIds:
	encode_genPdgId[i] = [0,0,0,0,0,1,0]


target = target.map(encode_genPdgId)



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

model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.001),metrics=['accuracy'])
model.summary()

#test model with validation data but lower lr, maybe increase batch size and play w val split?
history = model.fit(x_train,y_train,batch_size=256,epochs=10,validation_split=0.3)

plt.figure()
plt.plot(history.history['val_loss'],label='val loss')
plt.plot(history.history['loss'],label='training loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.savefig('lossHistory_evenSample.pdf')






