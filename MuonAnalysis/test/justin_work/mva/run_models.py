import pandas as pd
import numpy as np

from DATA import DATA
from DATA import reportSample
from DATA import prepareTrainingSet

from NN import NN

import sys

#initilization of datasets and model variables
dypath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root'
qcdpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root'
ttpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root'

model_vars = ['Muon_genPdgId','Muon_pt','Muon_chi2LocalMomentum',
'Muon_chi2LocalPosition','Muon_trkRelChi2','Muon_trkKink','Muon_glbKink',
'Muon_segmentCompatibility','Muon_timeAtIpInOutErr','Muon_innerTrackNormalizedChi2',
'Muon_innerTrackValidFraction','Muon_nTrackerLayersWithMeasurement',
'Muon_outerTrackCharge','Muon_innerTrackCharge',
'Muon_pfRelIso03_chg','Muon_pfRelIso03_all',
'Muon_isGood','Muon_isHighPurity','Muon_nPixelLayers']

dataset_DY = DATA(dypath,"Drell-Yan")
#dataset_QCD = DATA(qcdpath, "QCD")
dataset_TT = DATA(ttpath, "TTJets")

dataset_DY.report()
#dataset_QCD.report()
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

datatest =pd.concat(m1dysample)
x_train, x_test, y_train, y_test, pt_train, pt_test  = prepareTrainingSet(datatest, model_vars, m1dict)
#print(x_train, x_test, y_train, y_test)
#print(pt_test)
m1 = NN(x_train, x_test, y_train, y_test, "model1", "Model trained only on true muons and unmatched", 2, pt_train, pt_test, eval_tag)

print("\n")

######################################################

