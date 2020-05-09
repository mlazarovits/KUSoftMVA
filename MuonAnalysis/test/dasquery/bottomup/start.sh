

#python querydatasetforNanoAODfile.py "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/CMSSW_10_2_9-102X_upgrade2018_realistic_v15_RelVal_nanoaod102X2018-v1/NANOAODSIM"
#python querydatasetforNanoAODfile.py "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_CUETP8M1Down/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM"
#python querydatasetforNanoAODfile.py "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISpring18MiniAOD-100X_upgrade2018_realistic_v10-v2/MINIAODSIM"
python querydatasetforNanoAODfile.py "/DYJetsToLL_M-50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM"
python gensublists.py 5 100 "./DYJetsToLL2018/"
python genparentsublists.py "./DYJetsToLL2018/"


python querydatasetforNanoAODfile.py "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"
python gensublists.py 5 100 "./TTJets2018/"
python genparentsublists.py "./TTJets2018/"

python querydatasetforNanoAODfile.py "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIWinter19PFCalibNanoAOD-2018Conditions_105X_upgrade2018_realistic_v4-v1/NANOAODSIM"
python gensublists.py 5 100 "./QCD_pt_600to800_2018/"
python genparentsublists.py "./QCD_pt_600to800_2018/"


