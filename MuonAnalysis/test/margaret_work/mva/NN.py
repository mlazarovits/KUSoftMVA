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
# np.set_printoptions(threshold=sys.maxsize)
from keras import layers
from sklearn.utils import shuffle
from array import array


from ROOT import TH1D, TFile, TEfficiency, TCanvas, TGraph

from plotFunctions import plotEfficiency, plotROCcurves



def evaluateModel(model_y, true_y, model_pt, fname, tag, nClasses,mdict, results ):

	# print(model_y)
	#translate model prediction probabilities to onehot
	# let plabel require >= 0.5
	pred = model_y
	pred[ pred >= 0.5 ] = 1.
	pred[ pred <0.5 ] = 0.

	h_num = [ TH1D("num_"+str(i), "label "+str(i), 41, -0.5, 40.5 ) for i in range(nClasses) ]	
	h_den = [ TH1D("den_"+str(i), "label "+str(i), 41, -0.5, 40.5 ) for i in range(nClasses) ]

	num_ctr = [ 0. for i in range(nClasses) ]
	den_ctr = [ 0. for i in range(nClasses) ]

	all_num_ctr =  0. 
	all_den_ctr =  0. 

	h_fnum = [ TH1D("fnum_"+str(i), "correct id label "+str(i), 41, -0.5, 40.5 ) for i in range(nClasses) ]	
	#h_fden = [ TH1D("fden_"+str(i), "mis id. label "+str(i), 41, -0.5, 40.5 ) for i in range(nClasses) ]

	fnum_ctr = [ 0 for i in range(nClasses) ]
	#fden_ctr = [ 0 for i in range(nClasses) ]

	all_fnum_ctr = 0
	#all_fden_ctr = 0

	# begin the counting 
	for i , (my, ty, pt) in enumerate(zip(pred, true_y, model_pt)):
		#print i,my,ty,pt
		labelidx = -1
		for idx in range(len(ty)):
			if( ty[idx] == 1):
				labelidx = idx
		if( (my == ty).all() ): #we have a correct classification
			h_num[labelidx].Fill(pt)
			h_den[labelidx].Fill(pt)
			num_ctr[labelidx] = num_ctr[labelidx] + 1.
			den_ctr[labelidx] = num_ctr[labelidx] + 1.
			

			all_num_ctr = all_num_ctr + 1.
			all_den_ctr = all_den_ctr + 1.
		
		else: #incorrect classification
			#h_fnum	
			h_fnum[labelidx].Fill(pt)
			h_den[labelidx].Fill(pt)
			fnum_ctr[labelidx] = fnum_ctr[labelidx] + 1.
			den_ctr[labelidx] = den_ctr[labelidx] + 1.
			
			all_fnum_ctr = all_fnum_ctr +1.
			all_den_ctr = all_den_ctr + 1.

		#collect all classifications as well

			
	print("Reporting results from test data")
	for x in range(nClasses):
		print("label "+str(x)+":")
		print("Correct ID: "+ str(num_ctr[x]) +" of "+ str(den_ctr[x])+"   "+str(num_ctr[x]/den_ctr[x]))
		print("Mis.    ID: "+ str(fnum_ctr[x])+" of "+ str(den_ctr[x])+"   "+str(fnum_ctr[x]/den_ctr[x]))
		
	print("Overall performance: ")
	print("Correct ID: "+ str(all_num_ctr)+" of "+ str( all_den_ctr)+"   "+str(all_num_ctr/all_den_ctr))
	print("Mis.    ID: "+ str(all_fnum_ctr)+" of "+ str( all_den_ctr)+"   "+str(all_fnum_ctr/all_den_ctr))
	




	goodEff = [ TEfficiency(h_num[i],h_den[i]) for i in range(nClasses) ]
	[ goodEff[i].SetName("correct"+str(i)) for i in range(nClasses) ]
	badEff = [ TEfficiency(h_fnum[i],h_den[i]) for i in range(nClasses) ]
	[ badEff[i].SetName("fake"+str(i)) for i in range(nClasses) ]

#[ self.tr_acc, self.tr_loss, self.tr_valacc, self.tr_valloss]
 
	h_loss = TGraph(  len(results[1]), array('d',results[1]), array('d',list(np.arange(len(results[1])))) )
	h_vloss= TGraph(  len(results[3]), array('d',results[3]), array('d',list(np.arange(len(results[3])))) )
	h_acc = TGraph(	  len(results[0]), array('d',results[0]), array('d',list(np.arange(len(results[0])))) )
	h_vacc = TGraph(  len(results[2]), array('d',results[2]), array('d',list(np.arange(len(results[2])))) )

#	c1 = TCanvas()
#	goodEff[0].Draw()
	

	outfile = TFile("./eval_results/"+fname+"_"+tag+".root","RECREATE")
	[ outfile.WriteTObject(x) for x in h_num ]
	[ outfile.WriteTObject(x) for x in h_fnum]
	[ outfile.WriteTObject(x) for x in h_den ]
	plotEfficiency(goodEff,fname+tag,outfile)
	[ outfile.WriteTObject(x) for x in goodEff ]
	[ outfile.WriteTObject(x) for x in badEff ]
	outfile.WriteObject(h_loss, "trainingLoss")
	outfile.WriteObject(h_vloss, "validationLoss")
	outfile.WriteObject(h_acc, "trainingAcc")
	outfile.WriteObject(h_vacc, "validataionAcc")
	outfile.Write()
	outfile.Close()

	plotROCcurves(true_y,model_y,list(mdict.keys()),tag)

	return 1	



class NN:
	def __init__(self,x_train,x_test,y_train,y_test, name, modeldesc, mdict, pt_train, pt_test, tag):
		self.x_train = x_train
		self.y_train = y_train
		self.x_test = x_test
		self.y_test = y_test
		self.pt_train = pt_train
		self.pt_test = pt_test
		self.mdict = mdict
		values = pd.Series(list(mdict.values())).to_numpy()
		nClasses = len(np.unique(values))
		self.nClasses = nClasses	
		self.name = name
		self.tag = tag
		self.modeldesc = modeldesc

		self.n_features = self.x_train.shape[1]
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
		self.Hist = self.model.fit(self.x_train, self.y_train, epochs=100, batch_size=256,validation_split=0.1, verbose=0)
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
		self.predictions = self.model.predict(x_test)	
	#	self.predictions = self.model.predict(x_train)
		
		evaluateModel(self.predictions, self.y_test, self.pt_test, self.name, self.tag, self.nClasses, self.mdict, self.results )			








		
