


#Old mini skimmer
#cmsRun createMiniAODNtuple.py print inputFiles_load=./dasquery/bottomup/DYJetsToLL2018/sublist_1.list outputFile=./OutputFiles/DYJetsToLL2018_MINI.root maxEvents=10000

#cmsRun createMiniAODNtuple.py print inputFiles_load=./dasquery/bottomup/TTJets2018/sublist_1.list outputFile=./OutputFiles/TTJets2018_MINI.root maxEvents=10000

#cmsRun createMiniAODNtuple.py print inputFiles_load=./dasquery/bottomup/QCD_pt_600to800_2018/sublist_1.list outputFile=./OutputFiles/QCD_pt_600to800_2018_MINI.root maxEvents=10000

#new mini skimmer
cmsRun miniNtuple_cfg.py print inputFiles_load=./dasquery/bottomup/DYJetsToLL2018/sublist_1.list outputFile=./OutputFiles/DYJetsToLL2018_MINI.root maxEvents=100000
cmsRun miniNtuple_cfg.py print inputFiles_load=./dasquery/bottomup/TTJets2018/sublist_1.list outputFile=./OutputFiles/TTJets2018_MINI.root maxEvents=100000

cmsRun miniNtuple_cfg.py print inputFiles_load=./dasquery/bottomup/QCD_pt_600to800_2018/sublist_1.list outputFile=./OutputFiles/QCD_pt_600to800_2018_MINI.root maxEvents=100000


