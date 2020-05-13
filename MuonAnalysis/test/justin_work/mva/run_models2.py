import pandas as pd
import numpy as np

from DATA import DATA
from DATA import reportSample
from DATA import prepareTrainingSet
from DATA import dropBenchmarkVar
from NN import evaluateSubset
from NN import NN
from DATA import prepareBenchSet
import sys

#initilization of datasets and model variables
dypath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root'
qcdpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root'
ttpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root'

T_dypath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root'
T_qcdpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root'
T_ttpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root'

model_vars = ['Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge',
'Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
'Muon_isGood','Muon_isHighPurity','Muon_nPixelLayers','Muon_miniPFRelIso_chg','Muon_miniPFRelIso_all', 'Muon_looseId', 'Muon_softId', 'Muon_softMvaId' ]


train_vars = [ 'Muon_genPdgId','Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge',
'Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
'Muon_isGood','Muon_isHighPurity','Muon_nPixelLayers','Muon_miniPFRelIso_chg','Muon_miniPFRelIso_all']



#bench_vars = ['Muon_genPdgId','Muon_pt','Muon_looseId', 'Muon_softId', 'Muon_softMvaId']

dataset_DY = DATA(dypath,"Drell-Yan")
dataset_QCD = DATA(qcdpath, "QCD")
dataset_TT = DATA(ttpath, "TTJets")
print("Reporting training datasets")
dataset_DY.report()
dataset_QCD.report()
dataset_TT.report()


T_dataset_DY = DATA(dypath,"TEST_Drell-Yan")
T_dataset_QCD = DATA(qcdpath, "TEST_QCD")
T_dataset_TT = DATA(ttpath, "TEST_TTJets")
print("Reporting testing datasets")
T_dataset_DY.report()
T_dataset_QCD.report()
T_dataset_TT.report()

eval_tag = sys.argv[1] # input string for tagging output files 

#quick and dirty sample all
mx = 99999999999999999

#TODO have an extra sample to load for unique sample testing (a separate hadded file)

######################################################
####################MODEL 5###########################
print("\nBegin Model 5")
mdysample = dataset_DY.sample(['mu','U','pi','k','p' ],[10000,2000,2000,2000,2000])
mttsample = dataset_TT.sample(['mu','U','pi','k','p'],[10000,2000,2000,2000,2000])
mqcdsample = dataset_QCD.sample(['mu','U','pi','k','p'],[4000,2000,2000,2000,2000])


#This is the full testing sample, it will have uneven amouts of classes
T_fulldysample= pd.concat(T_dataset_DY.sample(['mu','U','pi','k','p' ],[mx,mx,mx,mx,mx]) )
T_fullttsample= pd.concat(T_dataset_TT.sample(['mu','U','pi','k','p'],[mx,mx,mx,mx,mx]) )
T_fullqcdsample=pd.concat(T_dataset_QCD.sample(['mu','U','pi','k','p'],[mx,mx,mx,mx,mx]) )


#these are the combined testing samples, ill have the same object ratios as training
T_subdysample= pd.concat(T_dataset_DY.sample(['mu','U','pi','k','p' ],[10000,2000,2000,2000,2000]) )
T_subttsample= pd.concat(T_dataset_TT.sample(['mu','U','pi','k','p'],[10000,2000,2000,2000,2000]) )
T_subqcdsample= pd.concat(T_dataset_QCD.sample(['mu','U','pi','k','p'],[4000,2000,2000,2000,2000]) )
#merge subsetse
T_fullcombinedsample =pd.concat([ T_subdysample, T_subttsample, T_subqcdsample] )


reportSample( mdysample )
reportSample( mttsample )
reportSample( mqcdsample )

mdict = {13: [1,0], 999: [0,1], 211:[0,1], 321:[0,1], 2212:[0,1]}

fulldy_x, fulldy_y, fulldy_pt = prepareBenchSet( T_fulldysample, model_vars, mdict)
fulltt_x, fulltt_y, fulldy_pt = prepareBenchSet( T_fullttsample, model_vars, mdict)
fullqcd_x, fullqcd_y, fullqcd_pt = prepareBenchSet( T_fullqcdsample, model_vars, mdict)
fullcom_x, fullcom_y, fullcom_pt = prepareBenchSet( T_fullcombinedsample, model_vars, mdict)
#print(fulldy_y)
#Data sets are prepped for benchmarking
#benchmark_sample(mdict, )


mdysample = pd.concat(mdysample)
mttsample = pd.concat(mttsample)
mqcdsample = pd.concat(mqcdsample)

#remove benchmark variables from the training sample and test samples
#drop benchmakrs for training in NN
#mdysample = dropBenchmarkVar(mdysample)
#mttsample = dropBenchmarkVar(mttsample)
#mqcdsample = dropBenchmarkVar(mqcdsample)
#drop bench mark from these so we can do predict with them later
#T_fulldysample = dropBenchmarkVar(T_fulldysample)
#T_fullttsample = dropBenchmarkVar(T_fullttsample)
#T_fullqcdsample = dropBenchmarkVar(T_fullqcdsample)
#T_fullcombinedsample = dropBenchmarkVar(T_fullcombinedsample)
#T_fulldysample = T_fulldysample.drop(columns='Muon_genPdgId')
#T_fullttsample = T_fullttsample.drop(columns='Muon_genPdgId')
#T_fullqcdsample = T_fullqcdsample.drop(columns='Muon_genPdgId')
#T_fullcombinedsample = T_fullcombinedsample.drop(columns='Muon_genPdgId')

datatest = pd.concat([mdysample, mttsample, mqcdsample ])
#print(T_fulldysample.columns)

#make the special test sets
x_test1, y_test1, pt_test1 = prepareBenchSet(T_fulldysample,train_vars, mdict) 
x_test2, y_test2, pt_test2 = prepareBenchSet(T_fullttsample,train_vars, mdict)
x_test3, y_test3, pt_test3 = prepareBenchSet(T_fullqcdsample,train_vars, mdict)
x_test4, y_test4, pt_test4 = prepareBenchSet(T_fullcombinedsample, train_vars, mdict)



datatest = pd.concat([mdysample, mttsample, mqcdsample ])


#get the model training set
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, train_vars, mdict)
#train the model
m = NN(x_train, x_test, y_train, y_test, "model5", "Model trained only on true muons vs unmatched with non muons EXCLUDING electrons in both test and in training, binary classification", 2, pt_train, pt_test, '')




#individual sample testing and evaluation
print("evaluating full DY")
evaluateSubset(m,m.model, y_test1, x_test1, pt_test1, "DY")
print("evaluating full TT")
evaluateSubset(m,m.model, y_test2, x_test2, pt_test2, "TT")
print("evaluating full QCD")
evaluateSubset(m,m.model, y_test3, x_test3, pt_test3, "QCD")
print("evaluating full combined")
evaluateSubset(m,m.model, y_test4, x_test4, pt_test4, "COMB")





sys.exit();
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

m = NN(x_train, x_test, y_train, y_test, "model6", "Model trained on true muons vs all  non muons, EXCLUDING electrons in both test and in training, binary classification", 2, pt_train, pt_test, eval_tag)

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

m = NN(x_train, x_test, y_train, y_test, "model7", "Model trained on all classes EXCLUDING electrons in both training and testing , classification of  most  labels", 5, pt_train, pt_test, eval_tag)

print("\n")












