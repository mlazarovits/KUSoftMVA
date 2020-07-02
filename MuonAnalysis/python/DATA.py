


import numpy as np
#import root_numpy
import uproot
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



def dropBenchmarkVar( sample ):#, benchvars ):
	newsamp = sample
	newsamp = newsamp.drop(columns='Muon_looseId')
	newsamp = newsamp.drop(columns='Muon_softId')
	newsamp = newsamp.drop(columns='Muon_softMvaId')
	return newsamp

def prepareBenchSet( data, target):
	# data=  sample[ model_vars ]
	
	# target = data['Muon_genPdgId']
	# target=abs(target)
	
	# data = data.drop(columns='Muon_genPdgId')
	# pt = data['Muon_pt']
	# target= target.map(label_dict)
	# data = (data-data.mean())/data.std()

	_,x_test, _, y_test = train_test_split(data,target, test_size=.99, random_state=1)
	_,pt_test, _, _= train_test_split(pt,target, test_size=.99, random_state=1)
	
	x_test = x_test.to_numpy()
	y_test = y_test.to_numpy()
	pt_test = pt_test.to_numpy()
	return x_test,y_test,pt_test

def prepareTrainingSet( data, target ):
# 	data = sample[ model_vars ]
# #	print(data)
# 	data = shuffle(data)
# 	target = data['Muon_genPdgId']
# 	target = abs(target)
# 	data = data.drop(columns='Muon_genPdgId')

	
# 	pt = data['Muon_pt']
# #	data = data.drop(columns='Muon_pt')

# 	target = target.map(label_dict)
# 	data = (data-data.mean())/data.std()	
	
	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = .35, random_state=1)
	pt_train, pt_test, y_train2, y_test2 = train_test_split(pt,target, test_size= .35, random_state=1)
	x_train = x_train.to_numpy()
	x_test = x_test.to_numpy()
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



# def expandList( df, columnNames):
#                 outDf = pd.DataFrame()
#                 for col in columnNames:
#                         arr = pd.Series(np.array([j for i in df[col] for j in i]))
#                         outDf[col] = arr
#                 return outDf




def preprocessing(sample , model_vars, label_dict):
	events = uproot.open(self.fname)[self.treeName]
	memChunks = [i for i in events.mempartitions(1e6)]
	pdgIds = np.array([])
	for i in memChunks:
		memStart = i[0]
		memStop = i[1]
		data = events.arrays(model_vars,entrystart=memStart,entrystop=memStop)

		#make labels
		genData = events.array('GenPart_pdgId',entrystart=memStart,entrystop=memStop)
		dataMu = events.array('Muon_genPartIdx',entrystart=memStart,entrystop=memStop)
		pdgIds = np.append(pdgIds,[-999 if mu == -1 else genData[i][mu] for i, idxs in enumerate(dataMu) for j, mu in enumerate(idxs)])
			



	data = sample[ model_vars ]
#	print(data)
	data = shuffle(data)
	target = data['Muon_genPdgId']
	target = abs(target)
	data = data.drop(columns='Muon_genPdgId')

	
	pt = data['Muon_pt']
#	data = data.drop(columns='Muon_pt')

	target = target.map(label_dict)
	data = (data-data.mean())/data.std()

	return data, target

class DATA:

	def __init__(self,fname,name, model_vars):
		self.name = name
		self.treeName = 'Events'
		self.fname = fname
		# tmp = root_numpy.root2array(self.fname,self.treeName)
		events = uproot.open(self.fname)[self.treeName]
		# data = pd.DataFrame(tmp)
		

		#### using uproot to chunk mu and gen data ####
		dfs = list()
		memChunks = [i for i in events['GenPart_pdgId'].mempartitions(1e6)] #read 1 MB at a time
		print("# memChunks:",len(memChunks))
		for i in memChunks:
			memStart = i[0]
			memStop = i[1]
			genData = events.array('GenPart_pdgId',entrystart=memStart,entrystop=memStop)
			dataMu = events.array('Muon_genPartIdx',entrystart=memStart,entrystop=memStop)
			pdgIds = np.array([-999 if mu == -1 else genData[i][mu] for i, idxs in enumerate(dataMu) for j, mu in enumerate(idxs)])
			chunkData = events.pandas.df(model_vars,entrystart=memStart,entrystop=memStop).astype('float32')
			print(len(pdgIds),chunkData.shape)
			chunkData['Muon_genPdgId'] = pdgIds
			dfs.append(chunkData)



	
		# pdgIds = [-999 if mu == -1 else genData['GenPart_pdgId'][i][mu] for i, idxs in enumerate(np.array(data['Muon_genPartIdx'])) for j, mu in enumerate(idxs)]
		# pdgIds = np.array(pdgIds)
		# data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])
		
		# muonMask = data.columns.str.contains('Muon_.*')
		# expCols = data.loc[:,muonMask].columns
		

		# data = expandList(data, expCols)
		# data = events.pandas.df('Muon_*')
		# data['Muon_genPdgId'] = pdgIds
		
		data = pd.concat(dfs,ignore_index=True)
		self.data1 = data[abs(data.Muon_genPdgId) == 13]
		self.data2 = data[data.Muon_genPdgId == -999]
		self.data3 = data[abs(data.Muon_genPdgId) == 11]
		self.data4 = data[abs(data.Muon_genPdgId) == 211]
		self.data5 = data[abs(data.Muon_genPdgId) == 321]
		self.data6 = data[abs(data.Muon_genPdgId) == 2212]
			

		self.datacoll ={'mu': self.data1, 'U':self.data2, 'e':self.data3, 'pi':self.data4, 'k':self.data5,'p':self.data6}
	
	def __del__(self):
		del self.data1
		del self.data2
		del self.data3
		del self.data4
		del self.data5	
		del self.data6
			
	def report(self):
		print("Report for data "+self.name)
		print("mu", self.data1.shape)
		print("unmatched", self.data2.shape)
		print("elec", self.data3.shape)
		print("pion", self.data4.shape)
		print("kaon", self.data5.shape)
		print("prot", self.data6.shape)
		print("\n")



	def sample(self, keys, nsamples):
		return [ self.datacoll[k][:s] for i, (k,s) in enumerate(zip(keys,nsamples)) ] 
		


##
