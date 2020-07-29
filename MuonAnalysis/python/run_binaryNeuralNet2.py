import pandas as pd
import numpy as np

from DATA import *
from NN import evaluateSubset
from NN import NN
import sys
#from make_bench import benchmark_sample
import random
#high stats
dypath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Train_dyjets.root'
qcdpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Train_qcd.root'
ttpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Train_ttjets.root'

#high stats
T_dypath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_dyjets.root'
T_qcdpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_qcd.root'
T_ttpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_ttjets.root'



#muon pt will be dropped late, it must be added now
train_vars = ['Muon_pt','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge',
'Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
'Muon_isGood','Muon_isHighPurity','Muon_nPixelLayers']



#outPath = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis'
outPath = './'
eval_tag = sys.argv[1] # input string for tagging output files 

#quick and dirty sample all
mx = 999999999999

######################################################
####################MODEL 5###########################
print("\nBegin Model 5")

#1-40 pt run
#dymu2, dyU2 = 10000,10000
#tmu2, tU2 = 10000,10000

#small pt run
dymu2, dyU2 = 3000,3000
tmu2, tU2 = 3000,3000

#sampling for benchamrk
Tdymu2  , TdyU2 = 200000, 200000
Ttmu2, TtU2 = 200000, 200000


dataset_DY = DATA(dypath,"Drell-Yan",train_vars)
T_dataset_DY = DATA(T_dypath,"TEST_Drell-Yan",train_vars)
dataset_TT = DATA(ttpath, "TTJets",train_vars)
T_dataset_TT = DATA(T_ttpath,"TEST_ttJets",train_vars)
mdict = {13: [1,0], 999: [0,1], 211:[0,1], 321:[0,1], 2212:[0,1]}
bdict = {'mu': [1,0], 'U':[0,1]}


modelDesc = "Model trained only on true muons vs unmatched with non muons EXCLUDING electrons in both test and in training, binary classification"

m = NN("model5", modelDesc, train_vars,mdict,eval_tag)


lastChunk =35
nepoch =3;

## each chunk is one batch to train the NN on
## for each dataframe in the different physics processes do training for NN preprocessing
#for chunk, (dy, tt, qcd) in enumerate(zip(dataset_DY.dfs, dataset_TT.dfs, dataset_QCD.dfs)):
for epoch in range(1,nepoch+1):
	random.shuffle(dataset_DY.dfs)
	random.shuffle(dataset_TT.dfs)
#	random.shuffle(dataset_QCD.dfs)		

	for chunk, (dy, tt) in enumerate(zip(dataset_DY.dfs, dataset_TT.dfs)):
		if chunk > lastChunk: #reading data in 100 MB chunks, 10*100 = 1 GB/process
			break
		print('chunk #', chunk)


		dy = reportAndSample(dy,dataset_DY.name, ['mu','U'],[dymu2,dyU2])
		tt = reportAndSample(tt,dataset_TT.name, ['mu','U'],[tmu2,tU2])
		

		trainingChunk = pd.concat([dy,tt])
		#trainingChunk

		x_train, y_train, pt_train = prepareSet(trainingChunk,mdict)

		print("training on epoch ", epoch)	

	#use randomly initialized weights for first chunk
		if chunk == 0 and epoch == 1:
			m.trainNetwork(x_train,y_train, pt_train)
		else: #set weights of model from previous chunk
			weights = m.model.get_weights()
			m.model.set_weights(weights)
			m.trainNetwork(x_train,y_train, pt_train,weights)

#dy = reportAndSample(dataset_DY.dfs[lastChunk+1],dataset_DY.name, ['mu','U','pi','k','p' ],[dymu,dyU,dypi,dyk,dyp])
#tt = reportAndSample(dataset_TT.dfs[lastChunk+1],dataset_TT.name, ['mu','U','pi','k','p'],[tmu,tU,tpi,tk,tp])
#qcd = reportAndSample(dataset_QCD.dfs[lastChunk+1],dataset_QCD.name, ['mu','U','pi','k','p'],[qmu,qU,qpi,qk,qp])
#trainingChunk = pd.concat([dy,tt,qcd])
dy = reportAndSample(dataset_DY.dfs[lastChunk+1], dataset_DY.name, ['mu','U'],[dymu2,dyU2])
tt = reportAndSample(dataset_TT.dfs[lastChunk+1], dataset_TT.name, ['mu','U'],[tmu2,tU2])




x_test,y_test,pt_test = prepareSet(trainingChunk,mdict)
# # #evaluate on last memChunk test sets
m.evaluateNetwork(outPath,x_test,y_test,pt_test,0.5)

del dataset_DY
del dataset_TT
#del dataset_QCD

#evaluate on separate test sets
#create subsets for evaluation of network


T_dataset_DY.dfs = pd.concat(T_dataset_DY.dfs)
T_dataset_TT.dfs = pd.concat(T_dataset_TT.dfs)
dyTest = reportAndSample(T_dataset_DY.dfs,format("Full Test "+T_dataset_DY.name), ['mu','U','pi','k','p' ],[mx,mx,mx,mx,mx])
ttTest = reportAndSample(T_dataset_TT.dfs,format("Full Test "+T_dataset_TT.name), ['mu','U','pi','k','p'],[mx,mx,mx,mx,mx])


sub_dyTest = reportAndSample(T_dataset_DY.dfs,format("Sub Test "+T_dataset_DY.name), ['mu','U' ],[Tdymu2,TdyU2])
sub_ttTest = reportAndSample(T_dataset_TT.dfs,format("Sub Test "+T_dataset_TT.name), ['mu','U' ],[Ttmu2,TtU2])

fullcombinedTest = pd.concat([sub_dyTest, sub_ttTest])

x_testDY,y_testDY,pt_testDY = prepareSet(dyTest,mdict)
x_testTT,y_testTT,pt_testTT = prepareSet(ttTest,mdict)
#x_testQCD,y_testQCD,pt_testQCD = prepareSet(qcdTest,mdict)
x_testCOMB,y_testCOMB,pt_testCOMB = prepareSet(fullcombinedTest,mdict)

#del T_dataset_DY
#del T_dataset_QCD
#del T_dataset_TT
#def evaluateModel(model_y, true_y, model_pt,pthreshold, fname, tag, path, results=None ):
#def evaluateSubset( NN, y_testsub,x_testsub , pt_testsub ,pthreshold,  tagsub, path  ):


pthresh = .50
pstr = "p5"
print("evaluating full DY")
evaluateSubset(m, y_testDY, x_testDY, pt_testDY,pthresh, "DY"+pstr ,outPath)
print("\n")
print("evaluating full TT")
evaluateSubset(m, y_testTT, x_testTT, pt_testTT,pthresh, "TT"+pstr, outPath)
print("\n")
#print("evaluating full QCD")
#evaluateSubset(m,y_testQCD, x_testQCD, pt_testQCD, "QCD", outPath)
#print("\n")
print("evaluating full combined")
evaluateSubset(m, y_testCOMB, x_testCOMB, pt_testCOMB,pthresh, "COMB"+pstr , outPath)

#try different probability cuts
print("evaluating p60")
evaluateSubset(m, y_testDY, x_testDY, pt_testDY,.60, "DYp6",outPath)
evaluateSubset(m, y_testTT, x_testTT, pt_testTT,.60, "TTp6", outPath)
evaluateSubset(m, y_testCOMB, x_testCOMB, pt_testCOMB,.60, "COMBp6", outPath)


print("evaluating p70")
evaluateSubset(m, y_testDY, x_testDY, pt_testDY,.70, "DYp7",outPath)
evaluateSubset(m, y_testTT, x_testTT, pt_testTT,.70, "TTp7", outPath)
evaluateSubset(m, y_testCOMB, x_testCOMB, pt_testCOMB,.70, "COMBp7", outPath)


print("evaluating p80")
evaluateSubset(m, y_testDY, x_testDY, pt_testDY,.80, "DYp8",outPath)
evaluateSubset(m, y_testTT, x_testTT, pt_testTT,.80, "TTp8", outPath)
evaluateSubset(m, y_testCOMB, x_testCOMB, pt_testCOMB,.80, "COMBp8", outPath)

print("evaluating p90")
evaluateSubset(m, y_testDY, x_testDY, pt_testDY,.90, "DYp9",outPath)
evaluateSubset(m, y_testTT, x_testTT, pt_testTT,.90, "TTp9", outPath)
evaluateSubset(m, y_testCOMB, x_testCOMB, pt_testCOMB,.90, "COMBp9", outPath)

print("evaluating p95")
evaluateSubset(m, y_testDY, x_testDY, pt_testDY,.95, "DYp95",outPath)
evaluateSubset(m, y_testTT, x_testTT, pt_testTT,.95, "TTp95", outPath)
evaluateSubset(m, y_testCOMB, x_testCOMB, pt_testCOMB,.95, "COMBp95", outPath)







sys.exit();
print("\n")





