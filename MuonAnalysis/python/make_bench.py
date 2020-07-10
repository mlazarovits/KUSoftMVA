import math
import numpy as np
from NN import evaluateModel

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



	

	



