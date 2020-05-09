


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




def prepareTrainingSet( sample , model_vars, label_dict ):
	data = sample[ model_vars ]
#	print(data)
	data = shuffle(data)
	target = data['Muon_genPdgId']
	target = abs(target)
	data = data.drop(columns='Muon_genPdgId')

	
	pt = data['Muon_pt']
	data = data.drop(columns='Muon_pt')

	target = target.map(label_dict)
	data = (data-data.mean())/data.std()	
	
	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = .2, random_state=1)
	pt_train, pt_test, y_train2, y_test2 = train_test_split(pt,target, test_size= .2, random_state=1)


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



def expandList( df, columnNames):
                outDf = pd.DataFrame()
                for col in columnNames:
                        arr = pd.Series(np.array([j for i in df[col] for j in i]))
                        outDf[col] = arr
                return outDf

class DATA:


	def __init__(self,fname,name):
		self.name = name
		self.treeName = 'Events'
		self.fname = fname
		self.tmp = root_numpy.root2array(self.fname,self.treeName)
		self.data = pd.DataFrame(self.tmp)

		self.pdgIds = [-999 if mu == -1 else self.data['GenPart_pdgId'][i][mu] for i, idxs in enumerate(self.data['Muon_genPartIdx']) for j, mu in enumerate(idxs)]
		self.pdgIds = np.array(self.pdgIds)
		self.data = self.data.drop([i for i, nMu in enumerate(self.data['nMuon']) if nMu == 0])
		
		self.muonMask = self.data.columns.str.contains('Muon_.*')
		self.expCols = self.data.loc[:,self.muonMask].columns
		

		self.data = expandList(self.data, self.expCols)
		
		self.data['Muon_genPdgId'] = self.pdgIds
	
		self.data1 = self.data[abs(self.data.Muon_genPdgId) == 13]
		self.data2 = self.data[self.data.Muon_genPdgId == -999]
		self.data3 = self.data[abs(self.data.Muon_genPdgId) == 11]
		self.data4 = self.data[abs(self.data.Muon_genPdgId) == 211]
		self.data5 = self.data[abs(self.data.Muon_genPdgId) == 321]
		self.data6 = self.data[abs(self.data.Muon_genPdgId) == 2212]

		self.datacoll = {'mu': self.data1, 'U':self.data2, 'e':self.data3, 'pi':self.data4, 'k':self.data5,'p':self.data6}
			
	
			
	def report(self):
		print("Report for data "+self.name)
		print("mu", self.data1.shape)
		print("unmathched", self.data2.shape)
		print("elec", self.data3.shape)
		print("pion", self.data4.shape)
		print("kaon", self.data5.shape)
		print("prot", self.data6.shape)



	def sample(self, keys, nsamples):
		return [ self.datacoll[k][:s] for i, (k,s) in enumerate(zip(keys,nsamples)) ] 
		


##
