import pandas as pd
import numpy as np

from DATA import DATA
from DATA import reportSample
from DATA import prepareTrainingSet

from NN import NN

import sys

#initilization of datasets and model variables
dypath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000'
qcdpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000'
ttpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000'

model_vars = ['Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge',
'Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
'Muon_isGood','Muon_isHighPurity','Muon_nPixelLayers']

dataset_DY = DATA(dypath,"Drell-Yan")
dataset_QCD = DATA(qcdpath, "QCD")
dataset_TT = DATA(ttpath, "TTJets")

dataset_DY.report()
dataset_QCD.report()
dataset_TT.report()

eval_tag = sys.argv[1] # input string for tagging output files 

####################MODEL 1###########################
print("\nBegin Model 1")
m1dysample = dataset_DY.sample(['mu','U'],[30000,30000])
m1ttsample = dataset_TT.sample(['mu','U'],[30000,30000])
#print(m1dysample)
reportSample( m1dysample )
reportSample( m1ttsample )
m1dict = {13: [1,0], 999: [0,1]}

datatest =pd.concat([ pd.concat(m1dysample), pd.concat(m1ttsample) ])

x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, m1dict)
#print(x_train, x_test, y_train, y_test)
#print(pt_test)
m1 = NN(x_train, x_test, y_train, y_test, "model1", "Model trained only on true muons and unmatched, binary classicification", m1dict, pt_train, pt_test, eval_tag)

print("\n")

######################################################
####################MODEL 2###########################
print("\nBegin Model 2")
mdysample = dataset_DY.sample(['mu','U','e','pi','k','p' ],[3000,600,2000,600,600,600])
mttsample = dataset_TT.sample(['mu','U','e','pi','k','p'],[3000,600,2000,600,600,600])
mqcdsample = dataset_QCD.sample(['mu','U','e','pi','k','p'],[2000,800,2000,800,800,800])

reportSample( mdysample )
reportSample( mttsample )
reportSample( mqcdsample )
mdict = {13: [1,0], 999: [0,1], 11:[0,1], 211:[0,1], 321:[0,1], 2212:[0,1]}

datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

m = NN(x_train, x_test, y_train, y_test, "model2", "Model trained only on true muons vs unmatched with non muons, binary classification", mdict, pt_train, pt_test, eval_tag)

print("\n")

######################################################
####################MODEL 3###########################
print("\nBegin Model 3")
mdysample = dataset_DY.sample(['mu','e','pi','k','p' ],[3000,2000,600,600,600])
mttsample = dataset_TT.sample(['mu','e','pi','k','p'],[3000,2000,600,600,600])
mqcdsample = dataset_QCD.sample(['mu','e','pi','k','p'],[2000,2000,800,800,800])

reportSample( mdysample )
reportSample( mttsample )
reportSample( mqcdsample )
mdict = {13: [1,0], 11:[0,1], 211:[0,1], 321:[0,1], 2212:[0,1]}

datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

m = NN(x_train, x_test, y_train, y_test, "model3", "Model trained only on true muons vs all  non muons, binary classification", mdict, pt_train, pt_test, eval_tag)

print("\n")
######################################################
####################MODEL 4###########################
print("\nBegin Model 4")
mdysample = dataset_DY.sample(['mu','U','e','pi','k','p' ],[3000,600,2000,600,600,600])
mttsample = dataset_TT.sample(['mu','U','e','pi','k','p'],[3000,600,2000,600,600,600])
mqcdsample = dataset_QCD.sample(['mu','U','e','pi','k','p'],[2000,800,2000,800,800,800])

reportSample( mdysample )
reportSample( mttsample )
reportSample( mqcdsample )
mdict = {13: [1,0,0,0,0,0],999:[0,1,0,0,0,0], 11:[0,0,1,0,0,0], 211:[0,0,0,1,0,0], 321:[0,0,0,0,1,0], 2212:[0,0,0,0,0,1]}

datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

m = NN(x_train, x_test, y_train, y_test, "model4", "Model trained on all classes , classification of all possible labels", mdict, pt_train, pt_test, eval_tag)

print("\n")
######################################################
####################MODEL 5###########################
print("\nBegin Model 5")
mdysample = dataset_DY.sample(['mu','U','pi','k','p' ],[10000,2000,2000,2000,2000])
mttsample = dataset_TT.sample(['mu','U','pi','k','p'],[10000,2000,2000,2000,2000])
mqcdsample = dataset_QCD.sample(['mu','U','pi','k','p'],[4000,2000,2000,2000,2000])

reportSample( mdysample )
reportSample( mttsample )
reportSample( mqcdsample )
mdict = {13: [1,0], 999: [0,1], 211:[0,1], 321:[0,1], 2212:[0,1]}

datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

m = NN(x_train, x_test, y_train, y_test, "model5", "Model trained only on true muons vs unmatched with non muons EXCLUDING electrons in both test and in training, binary classification", mdict, pt_train, pt_test, eval_tag)

print("\n")
######################################################
####################MODEL 6###########################
print("\nBegin Model 6")
mdysample = dataset_DY.sample(['mu','pi','k','p' ],[7000,2000,2000,2000])
mttsample = dataset_TT.sample(['mu','pi','k','p'],[7000,2000,2000,2000])
mqcdsample = dataset_QCD.sample(['mu','pi','k','p'],[4000,2000,2000,2000])

reportSample( mdysample )
reportSample( mttsample )
reportSample( mqcdsample )
mdict = {13: [1,0], 211:[0,1], 321:[0,1], 2212:[0,1]}

datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

m = NN(x_train, x_test, y_train, y_test, "model6", "Model trained on true muons vs all  non muons, EXCLUDING electrons in both test and in training, binary classification", mdict, pt_train, pt_test, eval_tag)

print("\n")
######################################################
####################MODEL 7###########################
print("\nBegin Model 7")
mdysample = dataset_DY.sample(['mu','U','pi','k','p' ],[2000,2000,2000,2000,2000])
mttsample = dataset_TT.sample(['mu','U','pi','k','p'],[2000,2000,2000,2000,2000])
mqcdsample = dataset_QCD.sample(['mu','U','pi','k','p'],[2000,2000,2000,2000,2000])

reportSample( mdysample )
reportSample( mttsample )
reportSample( mqcdsample )
mdict = {13: [1,0,0,0,0],999:[0,1,0,0,0], 211:[0,0,1,0,0], 321:[0,0,0,1,0], 2212:[0,0,0,0,1]}

datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

m = NN(x_train, x_test, y_train, y_test, "model7", "Model trained on all classes EXCLUDING electrons in both training and testing , classification of  most  labels", mdict, pt_train, pt_test, eval_tag)

print("\n")












