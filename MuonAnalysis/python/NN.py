import numpy as np
# import root_numpy
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
from array import array
import os


from ROOT import TH1D, TFile, TEfficiency, TCanvas, TGraph

from plotFunctions import plotEfficiency, plotROCcurves




def evaluateModel(model_y, true_y, model_pt, fname, tag, path, results=None ):

	# print(model_y)
	#translate model prediction probabilities to onehot
	# let plabel require >= 0.5
	pred = model_y
	pred[ pred >= 0.5 ] = 1.
	pred[ pred <0.5 ] = 0.

	
	labels = np.unique(pred,axis=0)
	nClasses = len(labels)

	#this num is model predicts class and object matched to same class
	h_num = [ TH1D("num_"+str(i), "label "+str(x), 41, -0.5, 40.5 ) for i, x in enumerate(labels) ]

	#den of objects of a specific class
	h_den = [ TH1D("den_"+str(i), "label "+str(x), 41, -0.5, 40.5 ) for i, x in enumerate(labels) ]

	num_ctr = [ 0. for i in range(nClasses) ]
	den_ctr = [ 0. for i in range(nClasses) ]

	all_num_ctr =  0. 
	all_den_ctr =  0. 

	h_fnum = [ TH1D("fnum_"+str(i), "correct id label "+str(x), 41, -0.5, 40.5 ) for i, x in enumerate(labels) ]		
	#den of all objects that are labeled by model
	h_fden = [ TH1D("fden_"+str(i), "model predicts label "+str(x), 41, -0.5, 40.5 ) for i, x in enumerate(labels) ]

	fnum_ctr = [ 0 for i in range(nClasses) ]
	fden_ctr = [ 0 for i in range(nClasses) ]

	all_fnum_ctr = 0
	all_fden_ctr = 0

	nTrueMu = 0
	nNotMu = 0

	# begin the counting 
	for i , (my, ty, pt) in enumerate(zip(pred, true_y, model_pt)):
		ty = np.array([ty])
		if i < 10:
			print(i,my,ty,pt)

			print(ty.shape)
			print(np.flatnonzero(ty == 1))
		# labelidx = -1
		# modelidx = -1
		# for idx in range(len(ty)):
		# 	if( ty[idx] == 1):
		# 		labelidx = idx
		# for idx in range(len(my)):
		# 	if( my[idx] ==1):
		# 		modelidx = idx
		labelidx = int(np.flatnonzero(ty == 1))
		modelidx = int(np.flatnonzero(my == 1))

		if( (my == ty).all() ): #we have a correct classification

			h_num[labelidx].Fill(pt)
			h_fnum[labelidx].Fill(pt)

			num_ctr[labelidx] +=  1.

			all_num_ctr +=  1.
			#       all_fnum_ctr = all_fnum_ctr + 1.

		h_den[labelidx].Fill(pt)
		h_fden[modelidx].Fill(pt)

		den_ctr[labelidx] +=  1.
		fden_ctr[modelidx] +=  1.

		all_den_ctr +=  1.



		#collect all classifications as well

	print("Reporting results from test data")
	print("We define efficiency and purity s.t.")
	print("efficiency = # of objects correctly classified for a specific label / # of true objects of that label")
	print("purity = # of objects correctly classified for a specific label/ # of objects classified for that label")
	#account for 0 entries
	for j, x in enumerate(labels):	
		tempden = -1
		tempfden = -1
		if(den_ctr[j] != 0):
			tempden = den_ctr[j]
		if(fden_ctr[j] != 0):
			tempfden = fden_ctr[j]
		print("label "+str(x)+":")
		print("Efficiency : "+ str(num_ctr[j]) +" of "+ str(den_ctr[j])+"   "+str(num_ctr[j]/tempden))
		print("Purity     : "+ str(num_ctr[j])+" of "+ str(fden_ctr[j])+"   "+str(num_ctr[j]/tempfden))

	print("Overall performance: ")
	# print("Efficiency: "+ str(all_num_ctr)+" of "+ str( all_den_ctr)+"   "+str(all_num_ctr/all_den_ctr))
	#print("Mis.    ID: "+ str(all_fnum_ctr)+" of "+ str( all_den_ctr)+"   "+str(all_fnum_ctr/all_den_ctr))
	print("Purity: "+ str(all_num_ctr)+" of "+str(all_den_ctr)+"    "+str(all_num_ctr/all_den_ctr))


	goodEff = [ TEfficiency(h_num[i],h_den[i]) for i in range(nClasses) ]
	[ goodEff[i].SetTitle("correct "+str(i)) for i in range(nClasses) ]
	badEff = [ TEfficiency(h_num[i],h_fden[i]) for i in range(nClasses) ]
	[ badEff[i].SetTitle("pure "+str(i)) for i in range(nClasses) ]

#[ self.tr_acc, self.tr_loss, self.tr_valacc, self.tr_valloss]
	#	c1 = TCanvas()
#	goodEff[0].Draw()
	
	#make new outFile directory
	if not os.path.exists(path+"/eval_results/"):
		os.mkdir(path+"/eval_results/")

	outfile = TFile(path+"/eval_results/"+fname+"_"+tag+".root","RECREATE")
	[ outfile.WriteTObject(x) for x in h_num ]
	[ outfile.WriteTObject(x) for x in h_fnum]
	[ outfile.WriteTObject(x) for x in h_den ]
	#efficiency
	plotEfficiency(goodEff,fname+tag+"eff",outfile)
	[ outfile.WriteTObject(x) for x in goodEff ]
	#purity
	plotEfficiency(badEff,fname+tag+"purity",outfile)
	[ outfile.WriteTObject(x) for x in badEff ]
	# 
	if results != None:
		h_loss = TGraph(  len(results[1]),  array('d',list(np.arange(len(results[1])))), array('d',results[1])   )
		h_vloss= TGraph(  len(results[3]),  array('d',list(np.arange(len(results[3])))), array('d',results[3])   )
		h_acc = TGraph(   len(results[0]),  array('d',list(np.arange(len(results[0])))), array('d',results[0])   )
		h_vacc = TGraph(  len(results[2]),  array('d',list(np.arange(len(results[2])))), array('d',results[2])   )

		outfile.WriteObject(h_loss, "trainingLoss")
		outfile.WriteObject(h_vloss, "validationLoss")
		outfile.WriteObject(h_acc, "trainingAcc")
		outfile.WriteObject(h_vacc, "validataionAcc")

	outfile.Write()
	outfile.Close()

	#map true values to [0,1] for muon - 1 or not - 0 to match dim of scores output (prob for each class)
	# plotROCcurves(true_y,model_y,nClasses,fname)

	return 1	


def evaluateSubset( NN, y_testsub,x_testsub , pt_testsub ,  tagsub, path  ):
	model_y = NN.model.predict(x_testsub)
	# print("true_y")
#	print(true_y)
	true_y = y_testsub
#	print(true_y)
	model_pt = pt_testsub

	evaluateModel(model_y, true_y, model_pt, NN.name, tagsub, path )




class NN:
	def __init__(self, name, modeldesc, model_vars,mdict,tag):
		self.name = name
		self.modeldesc = modeldesc
		self.tag = tag
		self.mdict = mdict
		values = pd.Series(list(mdict.values())).to_numpy()
		self.nClasses = len(np.unique(values))

		self.n_features = len(model_vars)

		self.model = Sequential()
		self.model.add(Dense(128, activation='relu', kernel_initializer='he_normal', input_shape=(self.n_features,)))
		self.model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))
		self.model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))
		self.model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))

		self.model.add(Dense(self.nClasses, activation='softmax'))
		self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
		# fit the model
		print("Training model: "+self.name)
		print("Desc.: "+ self.modeldesc)
		print("\n")

	def trainNetwork(self,x_train,x_test,y_train,y_test, pt_train, pt_test,weights=None):
		self.x_train = x_train
		self.y_train = y_train
		self.x_test = x_test
		self.y_test = y_test
		self.pt_train = pt_train
		self.pt_test = pt_test
		
		if weights != None:
			self.model.set_weights(weights)
		self.Hist = self.model.fit(self.x_train, self.y_train, epochs=100, batch_size=256,validation_split=0.1, verbose=0)
		

	#evalautes network on last chunk of data
	def evaluateNetwork(self,path):
		self.tr_acc = self.Hist.history['accuracy']
		self.tr_loss = self.Hist.history['loss']		
		self.tr_valacc = self.Hist.history['val_accuracy']
		self.tr_valloss = self.Hist.history['val_loss']
		self.results = [ self.tr_acc, self.tr_loss, self.tr_valacc, self.tr_valloss]	

		#self.model.summary()
		self.te_loss, self.te_acc = self.model.evaluate(self.x_test,self.y_test,verbose=0)
		print("Model Report:")
		print("Training accuracy: %.4f " % self.tr_acc[-1])
		print("Validation accuracy: %.4f" % self.tr_valacc[-1])
		print("Training loss: %.4f" % self.tr_loss[-1])
		print("Validation loss: %.4f" % self.tr_valloss[-1])
		print('Test Accuracy: %.4f' % self.te_acc)
		print('Test loss: %.4f' % self.te_loss)
		print("Evaluating model....")
		self.predictions = self.model.predict(self.x_test)	
		evaluateModel(self.predictions, self.y_test, self.pt_test, self.name, self.tag, path, self.results )			








		
