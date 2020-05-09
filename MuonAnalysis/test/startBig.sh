


#Old mini skimmer
#cmsRun createMiniAODNtuple.py print inputFiles_load=./dasquery/bottomup/DYJetsToLL2018/sublist_1.list outputFile=./OutputFiles/DYJetsToLL2018_MINI.root maxEvents=10000

#cmsRun createMiniAODNtuple.py print inputFiles_load=./dasquery/bottomup/TTJets2018/sublist_1.list outputFile=./OutputFiles/TTJets2018_MINI.root maxEvents=10000

#cmsRun createMiniAODNtuple.py print inputFiles_load=./dasquery/bottomup/QCD_pt_600to800_2018/sublist_1.list outputFile=./OutputFiles/QCD_pt_600to800_2018_MINI.root maxEvents=10000

#new mini skimmer
cmsRun miniNtuple_cfg.py print inputFiles_load=./dasquery/bottomup/DYJetsToLL2018/sublist_1.list outputFile=./OutputFiles/DYJetsToLL2018_MINI.root maxEvents=10000000
mv /home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent1000000.root /home/t3-ku/janguian/janguian/MVA/DYJetsToLL2018_MINI1M.root

cmsRun miniNtuple_cfg.py print inputFiles_load=./dasquery/bottomup/TTJets2018/sublist_1.list outputFile=./OutputFiles/TTJets2018_MINI.root maxEvents=1000000
mv /home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent1000000.root /home/t3-ku/janguian/janguian/MVA/TTJets2018_MINI1M.root

cmsRun miniNtuple_cfg.py print inputFiles_load=./dasquery/bottomup/QCD_pt_600to800_2018/sublist_1.list outputFile=./OutputFiles/QCD_pt_600to800_2018_MINI.root maxEvents=1000000
mv /home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent1000000.root /home/t3-ku/janguian/janguian/MVA/QCD_pt_600to800_2018_MINI_1M.root

