


import numpy as np
#import root_numpy
import uproot
import pandas as pd
import sys
# from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
# from keras.models import Sequential, Model
# from keras.layers import *
# from keras.optimizers import SGD, Adam
# from keras.activations import relu
np.set_printoptions(threshold=sys.maxsize)
from keras import layers
from sklearn.utils import shuffle
import time as time



def dropBenchmarkVar( sample ):#, benchvars ):
	newsamp = sample
	newsamp = newsamp.drop(columns='Muon_looseId')
	newsamp = newsamp.drop(columns='Muon_softId')
	newsamp = newsamp.drop(columns='Muon_softMvaId')
	return newsamp


def prepareSet( data, label_dict):
	# data=  sample[ model_vars ]
	data = shuffle(data)
	target = data['Muon_genPdgId']
	# target=abs(target)
	
	data = data.drop(columns='Muon_genPdgId')
	pt = data['Muon_pt']
	data = data.drop(columns='Muon_pt')
	target= target.map(label_dict)
	data = (data-data.mean())/data.std()


	#only get test set to test benchmark models on (they are already "trained")
#	x_train,x_test, y_train, y_test = train_test_split(data,target, test_size=.99, random_state=1)
#	pt_train,pt_test, _, _= train_test_split(pt,target, test_size=.99, random_state=1)
	
	x_test = data.to_numpy()
	y_test = target.to_numpy()

	y_test = np.array([np.array(i) for i in y_test])
	#pt_test = pt_test.to_numpy()
	pt_test = pt.to_numpy()
	return x_test,y_test,pt_test

def prepareTestSet( data, label_dict):
	# data=  sample[ model_vars ]
	data = shuffle(data)
	target = data['Muon_genPdgId']
	# target=abs(target)
	
	data = data.drop(columns='Muon_genPdgId')
	pt = data['Muon_pt']
	data = data.drop(columns='Muon_pt')
	target= target.map(label_dict)
	data = (data-data.mean())/data.std()

	#only get test set to test benchmark models on (they are already "trained")
	_,x_test, _, y_test = train_test_split(data,target, test_size=.99, random_state=1)
	_,pt_test, _, _= train_test_split(pt,target, test_size=.99, random_state=1)
	
	x_test = x_test.to_numpy()
	y_test = y_test.to_numpy()
	pt_test = pt_test.to_numpy()
	return x_test,y_test,pt_test

def prepareTrainingSet( data, label_dict):
	# data = sample[ model_vars ]
	#print(data.columns,"\n")
	data = shuffle(data)
	target = data['Muon_genPdgId']
	# target = abs(target)

	data = data.drop(columns='Muon_genPdgId')
	pt = data['Muon_pt']
	data = data.drop(columns='Muon_pt')
	target = target.map(label_dict)
	data = (data-data.mean())/data.std()	
	
	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = .35, random_state=1)
	pt_train, pt_test, _, _ = train_test_split(pt,target, test_size= .35, random_state=1)
	x_train = x_train.to_numpy()
	x_test = x_test.to_numpy()
	y_train = y_train.to_numpy()
	y_test = y_test.to_numpy()

	y_train = np.array([np.array(i) for i in y_train])
	y_test = np.array([np.array(i) for i in y_test])
	pt_train = pt_train.to_numpy()
	pt_test = pt_test.to_numpy()

	return x_train, x_test, y_train, y_test, pt_train, pt_test


	


def reportSample( sample):
    for i in range(len(sample)):
        print("Sample "+str(i)+" Report")
        print( sample[i].shape )

def reportAndSample(df, name, keys, nsamples):
		data1 = df[df.Muon_genPdgId == 13]
		data2 = df[df.Muon_genPdgId == 999]
		data3 = df[df.Muon_genPdgId == 11]
		data4 = df[df.Muon_genPdgId == 211]
		data5 = df[df.Muon_genPdgId == 321]
		data6 = df[df.Muon_genPdgId == 2212]

		print("Report for data",name)
		print("mu",data1.shape)
		print("unmatched", data2.shape)
		print("elec", data3.shape)
		print("pion", data4.shape)
		print("kaon", data5.shape)
		print("prot", data6.shape)
		print("\n")
	
		datacoll ={'mu':data1, 'U':data2, 'e':data3, 'pi':data4, 'k':data5,'p':data6}
		
		temp = pd.concat([ datacoll[k][:s] for i, (k,s) in enumerate(zip(keys,nsamples)) ] )
		print("Report for concat ",temp.shape)
		return temp

		



class DATA:

	#creates a list of dataframes (chunked data)
	def __init__(self,fname,name, model_vars):
		print("Chunking",name)
		self.name = name
		self.treeName = 'Events'
		self.fname = fname
		# tmp = root_numpy.root2array(self.fname,self.treeName)
		events = uproot.open(self.fname)[self.treeName]
		# data = pd.DataFrame(tmp)
		

		#### using uproot to chunk mu and gen data ####
		startTot = time.process_time()
		self.dfs = list()
		chunkTime = np.array([])
		memChunks = [i for i in events.mempartitions(1e8,entrystart=0,entrystop=1e6)] #read 100 MB at a time, max 1mil events
		print("# memChunks:",len(memChunks))
		
		for i in memChunks:
			startChunk = time.process_time()
			memStart = i[0]
			memStop = i[1]
			genData = events.array('GenPart_pdgId',entrystart=memStart,entrystop=memStop)
			dataMu = events.array('Muon_genPartIdx',entrystart=memStart,entrystop=memStop)
			pdgIds = np.array([999 if mu == -1 else abs(genData[i][mu]) for i, idxs in enumerate(dataMu) for j, mu in enumerate(idxs)])
			chunkData = events.pandas.df(model_vars,entrystart=memStart,entrystop=memStop).astype('float32')
			chunkData['Muon_genPdgId'] = pdgIds
			chunkData = chunkData[chunkData.Muon_pt < 20] 	
			chunkData = chunkData[chunkData.Muon_pt >= 3]
			self.dfs.append(chunkData)

			stopChunk = time.process_time()
			chunkTime = np.append(chunkTime,stopChunk-startChunk)
		stopTot = time.process_time()
		print("total time",stopTot-startTot,"secs")
		print("avg chunk time",np.mean(chunkTime),"secs")
		print("\n")



	
		

	def __del__(self):
		del self.dfs


