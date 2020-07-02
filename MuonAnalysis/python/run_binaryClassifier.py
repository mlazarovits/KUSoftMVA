import pandas as pd
import numpy as np

from DATA import *
from NN import evaluateSubset
from NN import NN
from DATA import prepareBenchSet
import sys
from make_bench import benchmark_sample
#initilization of datasets and model variables
#dypath='/home/t3-ku/janguian/storeUser/malazaro/TrainSetDYJets.root'
dypath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root'
qcdpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root'
#ttpath='/home/t3-ku/janguian/storeUser/malazaro/TrainSetTTJets.root'
ttpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root'


#T_dypath='/home/t3-ku/janguian/storeUser/malazaro/TestSetDYJets.root'
T_dpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root'
T_qcdpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root'
T_ttpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root'
#T_ttpath='/home/t3-ku/janguian/storeUser/malazaro/TestSetTTJets.root'

model_vars = ['Muon_pt','Muon_eta','Muon_chi2LocalMomentum',
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



eval_tag = sys.argv[1] # input string for tagging output files 

#quick and dirty sample all
mx = 999999999999

#TODO have an extra sample to load for unique sample testing (a separate hadded file)

######################################################
####################MODEL 5###########################
print("\nBegin Model 5")

dymu, dyU, dypi, dyk, dyp = 10000, 2000, 2000, 2000, 2000
qmu, qU, qpi, qk, qp = 10000, 2000, 2000, 2000, 2000
tmu, tU, tpi, tk, tp = 4000, 2000, 2000, 2000, 2000

dataset_DY = DATA(dypath,"Drell-Yan",model_vars)
# dataset_DY.report()
# mdysample = dataset_DY.sample(['mu','U','pi','k','p' ],[dymu,dyU,dypi,dyk,dyp])
# print(len(mdysample))
# del dataset_DY

dataset_TT = DATA(ttpath, "TTJets",model_vars)
# dataset_TT.report()
# mttsample = dataset_TT.sample(['mu','U','pi','k','p'],[tmu,tU,tpi,tk,tp])
# del dataset_TT

# dataset_QCD = DATA(qcdpath, "QCD")
# dataset_QCD.report()
# mqcdsample = dataset_QCD.sample(['mu','U','pi','k','p'],[qmu,qU,qpi,qk,qp])
# del dataset_QCD

mdict = {13: [1,0], 999: [0,1], 211:[0,1], 321:[0,1], 2212:[0,1]}
# bdict = {'mu': [1,0], 'U':[0,1]}

#for each dataframe in the different physics processes
for dy, tt in zip(dataset_DY.dfs, dataset_TT.dfs):
	dy = reportAndSample(dy,dataset_DY.name, ['mu','U','pi','k','p' ],[dymu,dyU,dypi,dyk,dyp])
	# dy = pd.DataFrame(dy)
	tt = reportAndSample(tt,dataset_TT.name, ['mu','U','pi','k','p'],[tmu,tU,tpi,tk,tp])
	# tt = pd.DataFrame(tt)

	trainingChunk = pd.concat([dy,tt])
	trainingChunk = prepareTrainingSet(trainingChunk,mdict)



# T_dataset_DY = DATA(dypath,"TEST_Drell-Yan")
# T_dataset_DY.report()
# T_fulldysample= pd.concat(T_dataset_DY.sample(['mu','U','pi','k','p' ],[mx,mx,mx,mx,mx]) )
# T_subdysample= pd.concat(T_dataset_DY.sample(['mu','U','pi','k','p' ],[dymu,dyU,dypi,dyk,dyp]) )
# del T_dataset_DY
# #benchmark set
# fulldy_x, fulldy_y, fulldy_pt = prepareBenchSet( T_fulldysample, model_vars, mdict)
# benchmark_sample( fulldy_x, fulldy_y, fulldy_pt, bdict, "DYfullB" )

# #special test set for model
# x_test1, y_test1, pt_test1 = prepareBenchSet(T_fulldysample,train_vars, mdict)
# del T_fulldysample

# T_dataset_QCD = DATA(qcdpath, "TEST_QCD")
# T_dataset_QCD.report()
# T_fullqcdsample=pd.concat(T_dataset_QCD.sample(['mu','U','pi','k','p'],[mx,mx,mx,mx,mx]) )
# T_subqcdsample= pd.concat(T_dataset_QCD.sample(['mu','U','pi','k','p'],[qmu,qU,qpi,qk,qp]) )
# del T_dataset_QCD
# fullqcd_x, fullqcd_y, fullqcd_pt = prepareBenchSet( T_fullqcdsample, model_vars, mdict)
# benchmark_sample( fullqcd_x, fullqcd_y, fullqcd_pt, bdict, "QCDfullB")
# x_test3, y_test3, pt_test3 = prepareBenchSet(T_fullqcdsample,train_vars, mdict)
# del T_fullqcdsample


# T_dataset_TT = DATA(ttpath, "TEST_TTJets")
# T_dataset_TT.report()
# T_fullttsample= pd.concat(T_dataset_TT.sample(['mu','U','pi','k','p'],[mx,mx,mx,mx,mx]) )
# T_subttsample= pd.concat(T_dataset_TT.sample(['mu','U','pi','k','p'],[tmu,tU,tpi,tk,tp]) )
# del T_dataset_TT
# fulltt_x, fulltt_y, fulltt_pt = prepareBenchSet( T_fullttsample, model_vars, mdict)
# benchmark_sample( fulltt_x, fulltt_y, fulltt_pt, bdict, "TTfullB")
# x_test2, y_test2, pt_test2 = prepareBenchSet(T_fullttsample,train_vars, mdict)
# del T_fullttsample

# T_fullcombinedsample = pd.concat([T_subdysample, T_subqcdsample, T_subttsample])
# fullcom_x, fullcom_y, fullcom_pt = prepareBenchSet( T_fullcombinedsample, model_vars, mdict)
# benchmark_sample( fullcom_x, fullcom_y, fullcom_pt, bdict, "CombB")
# x_test4, y_test4, pt_test4 = prepareBenchSet(T_fullcombinedsample, train_vars, mdict)
# del T_fullcombinedsample


# mdysample = pd.concat(mdysample)
# mttsample = pd.concat(mttsample)
# mqcdsample = pd.concat(mqcdsample)
# trainingData = pd.concat([mdysample, mttsample, mqcdsample ])
# x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(trainingData, train_vars, mdict)
# m = NN(x_train, x_test, y_train, y_test, "model5", "Model trained only on true muons vs unmatched with non muons EXCLUDING electrons in both test and in training, binary classification", mdict, pt_train, pt_test, '')



#individual sample testing and evaluation
# print("evaluating full DY")
# evaluateSubset(m,m.model, y_test1, x_test1, pt_test1, "DY")
# print("evaluating full TT")
# evaluateSubset(m,m.model, y_test2, x_test2, pt_test2, "TT")
# print("evaluating full QCD")
# evaluateSubset(m,m.model, y_test3, x_test3, pt_test3, "QCD")
# print("evaluating full combined")
# evaluateSubset(m,m.model, y_test4, x_test4, pt_test4, "COMB")





sys.exit();
print("\n")
######################################################
####################MODEL 6###########################
# print("\nBegin Model 6")
# mdysample = dataset_DY.sample(['mu','pi','k','p' ],[7000,2000,2000,2000])
# mttsample = dataset_TT.sample(['mu','pi','k','p'],[7000,2000,2000,2000])
# mqcdsample = dataset_QCD.sample(['mu','pi','k','p'],[4000,2000,2000,2000])

# reportSample( mdysample )
# reportSample( mttsample )
# reportSample( mqcdsample )
# mdict = {13: [1,0], 211:[0,1], 321:[0,1], 2212:[0,1]}

# datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
# x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

# m = NN(x_train, x_test, y_train, y_test, "model6", "Model trained on true muons vs all  non muons, EXCLUDING electrons in both test and in training, binary classification", mdict, pt_train, pt_test, eval_tag)

# print("\n")
# ######################################################
# ####################MODEL 7###########################
# print("\nBegin Model 7")
# mdysample = dataset_DY.sample(['mu','U','pi','k','p' ],[2000,2000,2000,2000,2000])
# mttsample = dataset_TT.sample(['mu','U','pi','k','p'],[2000,2000,2000,2000,2000])
# mqcdsample = dataset_QCD.sample(['mu','U','pi','k','p'],[2000,2000,2000,2000,2000])

# reportSample( mdysample )
# reportSample( mttsample )
# reportSample( mqcdsample )
# mdict = {13: [1,0,0,0,0],999:[0,1,0,0,0], 211:[0,0,1,0,0], 321:[0,0,0,1,0], 2212:[0,0,0,0,1]}

# datatest = pd.concat([pd.concat(mdysample), pd.concat(mttsample), pd.concat(mqcdsample) ])
# x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, mdict)

# m = NN(x_train, x_test, y_train, y_test, "model7", "Model trained on all classes EXCLUDING electrons in both training and testing , classification of  most  labels", mdict, pt_train, pt_test, eval_tag)

# print("\n")












