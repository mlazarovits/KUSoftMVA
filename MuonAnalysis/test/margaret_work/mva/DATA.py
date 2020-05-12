


import numpy as np
import root_numpy
import pandas as pd
import sys
from os import path
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import *
from keras.optimizers import SGD, Adam
from keras.activations import relu
# np.set_printoptions(threshold=sys.maxsize)
from keras import layers
from sklearn.utils import shuffle




def prepareTrainingSet( sample , model_vars, label_dict ):
	data = sample[ model_vars ]
#	print(data)
	data = shuffle(data)
	target = data['Muon_genPdgId']
	target = abs(target)
	data = data.drop(columns='Muon_genPdgId')

	
	pt = data['Muon_pt']
#	data = data.drop(columns='Muon_pt')

	target = target.map(label_dict)
	norm = MinMaxScaler()
	data = norm.fit_transform(data)
	
	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = .35, random_state=1)
	pt_train, pt_test, _, _ = train_test_split(pt,target, test_size= .35, random_state=1)


	# x_train = x_train.to_numpy()
	# x_test = x_test.to_numpy()
	y_train = y_train.to_numpy()
	y_test = y_test.to_numpy()

	y_train = np.array([np.array(i) for i in y_train])
	y_test = np.array([np.array(i) for i in y_test])
	pt_train = pt_test.to_numpy()
	pt_test = pt_test.to_numpy()

	return x_train, x_test, y_train, y_test, pt_train, pt_test



def reportSample( sample):
                for i in range(len(sample)):
                        print("Sample "+str(i)+" Report")
                        print( sample[i].shape )



def expandList( df, columnNames):
                outDf = pd.DataFrame()
                for col in columnNames:
                        arr = pd.Series(np.array([j for i in df[col] for j in i]))
                        outDf[col] = arr
                return outDf


def makeData(filename,definedIds,treeName):
	# treeName = 'Events'
	# gPath = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/'
	data = root_numpy.root2array(filename+'.root',treeName)
	data = pd.DataFrame(data)
	#make gen pdg ID labels for reco muons
	#-999 if unmatched
	pdgIds = np.array([-999 if mu == -1 else data['GenPart_pdgId'][i][mu] for i, idxs in enumerate(data['Muon_genPartIdx']) for j, mu in enumerate(idxs)])
	#get rid of 0 muon events
	data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])
	#expand the list so each row is a muon (not an event)
	muonMask = data.columns.str.contains('Muon_.*')
	expCols = data.loc[:,muonMask].columns
	data = expandList(data, expCols)
	#add in gen pgdIds and jet btags of reco muons
	data['Muon_genPdgId'] = pdgIds
	#drop muons with pt < 2
	data = data.drop([i for i, pt in enumerate(data['Muon_pt']) if pt < 2])
	data = data.reset_index()
	#drop muons matched to anything not in our defined classes: 13, 221, 321, 2211, or 999
	data = data.drop([i for i, ID in enumerate(data['Muon_genPdgId']) if abs(ID) not in definedIds])
	data = data.reset_index()
	# df = df.drop([i for i, ID in enumerate(df['genPdgId']) if abs(ID) not in definedIds])
	data.to_csv(filename+'.csv')
	return data            

class DATA:


	def __init__(self,fname,name):
		definedIds = np.array([13,211,321,2212,999])
		self.name = name
		self.treeName = 'Events'
		self.fname = fname
		print(self.fname)
		#speeds up processing time
		if path.exists(self.fname+'.csv'):
			self.data = pd.read_csv(self.fname+'.csv')
		else:
			self.data = makeData(self.fname,definedIds,self.treeName)
		# self.tmp = root_numpy.root2array(self.fname,self.treeName)
		# self.data = pd.DataFrame(self.tmp)

		# self.pdgIds = [-999 if mu == -1 else self.data['GenPart_pdgId'][i][mu] for i, idxs in enumerate(self.data['Muon_genPartIdx']) for j, mu in enumerate(idxs)]
		# self.pdgIds = np.array(self.pdgIds)
		# self.data = self.data.drop([i for i, nMu in enumerate(self.data['nMuon']) if nMu == 0])
		
		# self.muonMask = self.data.columns.str.contains('Muon_.*')
		# self.expCols = self.data.loc[:,self.muonMask].columns
		

		# self.data = expandList(self.data, self.expCols)
		
		# self.data['Muon_genPdgId'] = self.pdgIds
	
		self.data1 = self.data[abs(self.data.Muon_genPdgId) == 13]
		self.data2 = self.data[self.data.Muon_genPdgId == -999]
		self.data3 = self.data[abs(self.data.Muon_genPdgId) == 11]
		self.data4 = self.data[abs(self.data.Muon_genPdgId) == 211]
		self.data5 = self.data[abs(self.data.Muon_genPdgId) == 321]
		self.data6 = self.data[abs(self.data.Muon_genPdgId) == 2212]

		self.datacoll = {'mu': self.data1, 'U':self.data2, 'e':self.data3, 'pi':self.data4, 'k':self.data5,'p':self.data6}
			
	
			
	def report(self):
		print("Report for data "+self.name)
		print("mu", self.data1.shape[0])
		print("unmatched", self.data2.shape[0])
		print("elec", self.data3.shape[0])
		print("pion", self.data4.shape[0])
		print("kaon", self.data5.shape[0])
		print("prot", self.data6.shape[0])

		print('Relative Frequencies of Classes (total):')
		print(abs(self.data.Muon_genPdgId).value_counts(normalize=True))



	def sample(self, keys, nsamples):
		return [ self.datacoll[k][:s] for i, (k,s) in enumerate(zip(keys,nsamples)) ] 
		


##
