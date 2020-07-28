import math
import numpy as np
from NN import evaluateModel
from DATA import DATA
import pandas as pd
from DATA import reportAndSample
from DATA import prepareSet



#load variables of interest to construt benchmarks

var_load=['Muon_pt','Muon_looseId', 'Muon_softId', 'Muon_softMvaId']

#bench_var=['Muon_looseId', 'Muon_softId', 'Muon_softMvaId']
bench_var=['Muon_looseId']

#high stats test files
T_dypath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_dyjets.root'
T_qcdpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_qcd.root'
T_ttpath='/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_ttjets.root'


mx = 999999999999
Tdymu2  , TdyU2 = 200000, 200000
Ttmu2, TtU2 = 200000, 200000


T_dataset_DY = DATA(T_dypath,"TEST_Drell-Yan",var_load)
T_dataset_TT = DATA(T_ttpath,"TEST_ttJets",var_load)

#concat the chunks for quick sample
T_dataset_DY.dfs = pd.concat(T_dataset_DY.dfs)
T_dataset_TT.dfs = pd.concat(T_dataset_TT.dfs)



dyTest = reportAndSample(T_dataset_DY.dfs,format("Full Test "+T_dataset_DY.name), ['mu','U','pi','k','p' ],[mx,mx,mx,mx,mx])

ttTest = reportAndSample(T_dataset_TT.dfs,format("Full Test "+T_dataset_TT.name), ['mu','U','pi','k','p'],[mx,mx,mx,mx,mx])

#subsets to be put together for COMB
sub_dyTest = reportAndSample(T_dataset_DY.dfs,format("Sub Test "+T_dataset_DY.name), ['mu','U' ],[Tdymu2,TdyU2])
sub_ttTest = reportAndSample(T_dataset_TT.dfs,format("Sub Test "+T_dataset_TT.name), ['mu','U' ],[Ttmu2,TtU2])


fullcombinedTest = pd.concat([sub_dyTest, sub_ttTest])

mdict = {13: [1,0], 999: [0,1], 211:[0,1], 321:[0,1], 2212:[0,1]}

#with bench vars define pass/fail flags
#hardcode each one by had for now, and just output each benchmark to its own file

#this will only work on 0,1 flags like looseId etc, combinations of cuts need to be done by hand
def bench_id( idname, tag, dy, tt, comb, label_dict ):
	x_dy, y_dy, pt_dy = prepareSet(dy, label_dict);
	x_tt, y_tt, pt_tt = prepareSet(tt, label_dict);
	x_c, y_c, pt_c = prepareSet(comb, label_dict);
#	x_dy = x_dy[:,id_idx]

	#print(x_dy)
	mdict = {'mu': [1,0], 'U':[0,1]}
	p = mdict['mu']
	f = mdict['U']
	idflags = [[]]
	[idflags.append(p) if val == 1 else idflags.append(f) for val in x_dy[:,0] ]
	idflags = idflags[1:]
	evaluateModel(np.array(idflags),y_dy,pt_dy,0.5,"benchp5",idname+"DY",'./')
	
	idflags = [[]]
	[idflags.append(p) if val == 1 else idflags.append(f) for val in x_tt ]
	idflags = idflags[1:]
	evaluateModel(np.array(idflags),y_tt,pt_tt,0.5,"benchp5",idname+"TT",'./')

	idflags =[[]]
	[idflags.append(p) if val == 1 else idflags.append(f) for val in x_c ]
	idflags = idflags[1:]
	evaluateModel(np.array(idflags),y_c,pt_c,0.5,"benchp5",idname+"COMB",'./')	

	#model_y, true_y, model_pt,pthreshold, fname, tag, path, results=None


bench_id( 'Muon_looseId', '',dyTest,ttTest,fullcombinedTest,mdict)



def benchmark_sample(  x, y, pt, mdict, name ):


	print("from bench xypt")
	#	print(x)
	#	print(y)
	#	print(pt)

	#soft mva -1
	#soft id -2
	#loose id -3

	#make dummy results
	results=np.zeros(4,1)

	nclasses = len(y[0])
	print("nclass", nclasses)
	p = mdict['mu']
	f = mdict['U']
	#	print(p)
	#	print(f)
	#we can always only do 2 class with bench
	#evaluate for soft
	passIdsoft = max(x[:,-2])
	print("passIdsoft",passIdsoft)
	#construct  x prediction
	soft = [[]]
	[soft.append(p) if val == passIdsoft else soft.append(f) for val in x[:,-2] ]
	soft = soft[1:]
	#	print soft	
	evaluateModel(np.array(soft),y,pt,name,"SoftId",nclasses,results)

	#evaluate soft + loose
	passIdloose = max(x[:,-3])
	print("passIdloose",passIdloose)
	softloose = [[]]
	id1 = x[:,-3]
	id2 = x[:,-2]

	[softloose.append(p) if i1 == passIdloose and i2 == passIdsoft else softloose.append(f) for i1,i2 in zip(id1,id2)  ]
	softloose = softloose[1:]
	#	print softloose
	evaluateModel(np.array(softloose),y,pt,name,"SoftLoose",nclasses,results)


	passIdmva = max(x[:,-1])
	print("passIdmva",passIdmva)
	softmva = [[]]
	if(math.isnan(passIdmva)):
		[	softmva.append(f) for val in x[:,-1] ]
	else:
		[softmva.append(p) if val == passIdmva else soft.append(f) for val in x[:,-1]	]
	#evaluate soft mva soft mva doesnt work on DY?
	softmva = softmva[1:]
	#	print  softmva	
	evaluateModel(np.array(softmva),y,pt,name,"SoftMva",nclasses,results)



	

	



