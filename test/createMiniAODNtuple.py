import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("OWNPARTICLES")
options = VarParsing.VarParsing('analysis')
options.inputFiles = "file:/home/t3-ku/janguian/CMSSW_10_6_8/src/KUsoftMVA/test/0ACB220F-DB5C-3449-83F5-E04858176001.root"
options.outputFile = "defaultout.root"
options.maxEvents = 100
options.parseArguments()

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input=cms.untracked.int32(options.maxEvents ))
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 5000


process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(options.inputFiles)
)
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outputFile)
    ,outputCommands = cms.untracked.vstring('drop *',
      "keep *_offlineSlimmedPrimaryVertices_*_*",
      "keep *_slimmedMuons_*_*",
      "keep *_slimmedElectrons_*_*",
      "keep *_packedPFCandidates_*_*",
      "keep *_packedGenParticles_*_*")
       
) 
process.e = cms.EndPath(process.out)


