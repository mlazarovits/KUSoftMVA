

python querydatasetforNanoAODfile.py "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/CMSSW_10_2_9-102X_upgrade2018_realistic_v15_RelVal_nanoaod102X2018-v1/NANOAODSIM"
python gensublists.py 1 20 "./DYJetsToLL2018/"
python genparentsublists.py "./DYJetsToLL2018/"


python querydatasetforNanoAODfile.py "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"
python gensublists.py 1 20 "./TTJets2018/"
python genparentsublists.py "./TTJets2018/"

python querydatasetforNanoAODfile.py "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIWinter19PFCalibNanoAOD-2018Conditions_105X_upgrade2018_realistic_v4-v1/NANOAODSIM"
python gensublists.py 1 20 "./QCD_pt_600to800_2018/"
python genparentsublists.py "./QCD_pt_600to800_2018/"


