import math
import numpy as np
from NN import evaluateModel



class benchmarkSample:
	def __init__(self,x,y,pt,mdict,name):
		self.x = x
		self.y = y
		self.pt = pt
		self.mdict = mdict
		self.name = name
		# print("from bench xypt")
		self.path = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis'
		#	print(x)
		#	print(y)
		#	print(pt)

		#soft mva -1
		#soft id -2
		#loose id -3

		

		# self.nclasses = len(y[0])
		# print("nclasses", self.nclasses)
		self.p = mdict['mu']
		self.f = mdict['U']

		self.passIdsoft = max(self.x[:,-2])
		self.passIdloose = max(self.x[:,-3])
		self.passIdmva = max(self.x[:,-1])
	def makeSoftId(self):
		# self.passIdsoft = max(self.x[:,-2])
		print("assIdsoft",self.self.passIdsoft)
		#construct  x prediction
		soft = [[]]
		[soft.append(self.p) if val == self.passIdsoft else soft.append(self.f) for val in self.x[:,-2] ]
		soft = soft[1:]
		#	print soft	
		evaluateModel(np.array(soft),self.y,self.pt,self.name,"SoftId",self.path)
	def makeLooseId(self):
		# self.passIdloose = max(self.x[:,-3])
		print("passIdSoftLoose",self.passIdloose)
		softloose = [[]]
		id1 = self.x[:,-3]
		id2 = self.x[:,-2]
		# self.passIdmva = max(self.x[:,-1])
		[softloose.append(self.p) if i1 == self.passIdloose and i2 == self.passIdsoft else softloose.append(self.f) for i1,i2 in zip(id1,id2)  ]
		softloose = softloose[1:]
		#	print softloose
		evaluateModel(np.array(softloose),self.y,self.pt,self.name,"SoftLoose",self.path)

	def makeMvaId(self):
		# self.passIdmva = max(self.x[:,-1])
		print("passIdmva",self.passIdmva)
		softmva = [[]]
		if(math.isnan(self.passIdmva)):
			[	softmva.append(self.f) for val in x[:,-1] ]
		else:
			[softmva.append(self.p) if val == self.passIdmva else soft.append(self.f) for val in self.x[:,-1]	]
		#evaluate soft mva soft mva doesnt work on DY?
		softmva = softmva[1:]
		#	print  softmva	
		evaluateModel(np.array(softmva),self.y,self.pt,self.name,"SoftMva",self.path)

	def evaluateAllBenchmarks(self):
		self.makeSoftId()
		self.makeLooseId()
		self.makeMvaId()


# def benchmark_sample(  x, y, pt, mdict, name ):


# 	print("from bench xypt")
# 	#	print(x)
# 	#	print(y)
# 	#	print(pt)

# 	#soft mva -1
# 	#soft id -2
# 	#loose id -3

# 	#make dummy results
# 	results=np.zeros(4,1)

# 	nclasses = len(y[0])
# 	print("nclass", nclasses)
# 	p = mdict['mu']
# 	f = mdict['U']
# 	#	print(p)
# 	#	print(f)
# 	#we can always only do 2 class with bench
# 	#evaluate for soft
# 	self.passIdsoft = max(x[:,-2])
# 	print("self.passIdsoft",self.passIdsoft)
# 	#construct  x prediction
# 	soft = [[]]
# 	[soft.append(p) if val == self.passIdsoft else soft.append(f) for val in x[:,-2] ]
# 	soft = soft[1:]
# 	#	print soft	
# 	evaluateModel(np.array(soft),y,pt,name,"SoftId",nclasses,results)

# 	#evaluate soft + loose
# 	self.passIdloose = max(x[:,-3])
# 	print("self.passIdloose",self.passIdloose)
# 	softloose = [[]]
# 	id1 = x[:,-3]
# 	id2 = x[:,-2]

# 	[softloose.append(p) if i1 == self.passIdloose and i2 == self.passIdsoft else softloose.append(f) for i1,i2 in zip(id1,id2)  ]
# 	softloose = softloose[1:]
# 	#	print softloose
# 	evaluateModel(np.array(softloose),y,pt,name,"SoftLoose",nclasses,results)


# 	self.passIdmva = max(x[:,-1])
# 	print("self.passIdmva",self.passIdmva)
# 	softmva = [[]]
# 	if(math.isnan(self.passIdmva)):
# 		[	softmva.append(f) for val in x[:,-1] ]
# 	else:
# 		[softmva.append(p) if val == self.passIdmva else soft.append(f) for val in x[:,-1]	]
# 	#evaluate soft mva soft mva doesnt work on DY?
# 	softmva = softmva[1:]
# 	#	print  softmva	
# 	evaluateModel(np.array(softmva),y,pt,name,"SoftMva",nclasses,results)



	

	



