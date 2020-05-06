import ROOT
from os import environ
environ['KERAS_BACKEND'] = 'theano'
environ['THEANO_FLAGS'] = 'gcc.cxxflags=-march-=corei7'
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
from keras.optimizers import Adam

#Open file
data = ROOT.TFile.Open('/home/t3-ku/mlazarov/CMSSW_10_6_8/src/KUSoftMVA/test/test.root')

#Get signal and background trees
signal = data.Get('PromptMuons')
bkg_e = data.Get('Electrons')
bkg_pis = data.Get('Pions')
bkg_NPmus = data.Get('NonPromptMuons')
bkg_others = data.Get('Others')

#Add variables to be processed through NN
dataloader = ROOT.TMVA.DataLoader('dataset')

variables = ["Muon_pt","Muon_eta","Muon_sip3d",
	"Muon_dxy","Muon_dz","Muon_segmentComp","Muon_miniPFRelIso_chg"]
nVar = len(variables)
for i in variables:
	dataloader.AddVariable(i)


#variables still needed
#neutral component of miniIso
#ptRel
#ptRatio
#CSVv2 of jet matched to lepton
#for track selection: use pfCand.pseudoTrack() to access track info
#loop through pfCandidations in jet.daughterPtrVector()
#selection on track multiplicity of jet matched to lepton:
	#track pt > 1 GeV
	#charge() != 0
	#deltaR wrt jet (associated w lepton) <= 0.4
	#fromPV() > 1
	#trk.hitPattern().numberOfValidHits()>=8
	# trk.hitPattern().numberOfValidPixelHits()>=2
	# trk.normalizedChi2()<5
	# std::fabs(trk.dxy(vtx.position()))<0.2
	# std::fabs(trk.dz(vtx.position()))<17


dataloader.AddSignalTree(signal)
dataloader.AddBackgroundTree(bkg_e)
dataloader.AddBackgroundTree(bkg_pis)
dataloader.AddBackgroundTree(bkg_NPmus)
dataloader.AddBackgroundTree(bkg_others)

trainTestSplit = 0.7

dataloader.PrepareTrainingAndTestTree(ROOT.TCut(''),
	'TrainTestSplit_Signal={}:'.format(trainTestSplit)+\
	'TrainTestSplit_Background={}'.format(trainTestSplit)+\
	'SplitMode=Random')

#Set up TMVA
ROOT.TMVA.Tools.Instance()
ROOT.TMVA.PyMethodBase.PyInitialize()
outputFile = ROOT.TFile.Open('TMVAtest.root','RECREATE')
factory = ROOT.TMVA.factory('TMVAClassification',outputFile,'!V:!Silent:Color:DrawProgressBar:'+\
	'Transformations=I,G:AnalysisType=Classification')

#Define Keras model
model = Sequential()
model.add(Dense(64,activation='relu',input_dim=nVar))
model.add(Dense(64,activation='relu'))
model.add(Dense(2,activation='softmax'))
model.compile(loss='binary_crossentropy',optimizer=Adam(),metrics=['accuracy'])
model.summary()

numEpochs = 10
batchSize = 64

#Keras interface with previously defined model
factory.BookMethod(dataloader,ROOT.TMVA.Types.kPyKeras,'PyKeras','H:!V:VarTransform=G'+\
	':FilenameModel=model.h5:NumEpochs={}'.format(numEpochs)+\
	'10:BatchSize={}'.format(batchSize))
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

#print ROC curve
cv = factory.GetROCCurve(dataloader)
cv.Draw()




