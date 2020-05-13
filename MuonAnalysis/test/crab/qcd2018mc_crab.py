from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'MVA_QCD2018'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/miniNtuple_cfg.py'

#config.Data.inputDataset = '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIWinter19PFCalibMiniAOD-2018Conditions_105X_upgrade2018_realistic_v4-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIWinter19PFCalibMiniAOD-2018Conditions_105X_upgrade2018_realistic_v4-v1/MINIAODSIM'
config.Data.inputDataset = '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
config.Data.useParent = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 3
config.Data.outLFNDirBase = '/store/user/jsingera/MVA/'
config.Data.publication = True
config.Data.outputDatasetTag = 'MVA_QCD2018'

config.Site.storageSite = 'T2_US_Nebraska'
