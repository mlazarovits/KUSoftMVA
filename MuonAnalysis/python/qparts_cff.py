import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Modifier_run2_muon_2016_cff import run2_muon_2016
from Configuration.Eras.Modifier_run2_miniAOD_80XLegacy_cff import run2_miniAOD_80XLegacy
from Configuration.Eras.Modifier_run2_nanoAOD_94X2016_cff import run2_nanoAOD_94X2016
from Configuration.Eras.Modifier_run2_nanoAOD_94XMiniAODv1_cff import run2_nanoAOD_94XMiniAODv1
from Configuration.Eras.Modifier_run2_nanoAOD_94XMiniAODv2_cff import run2_nanoAOD_94XMiniAODv2
from Configuration.Eras.Modifier_run2_nanoAOD_102Xv1_cff import run2_nanoAOD_102Xv1
from PhysicsTools.NanoAOD.common_cff import *
import PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi




#isoForQP = cms.EDProducer("MuonIsoValueMapProducer",
#    src = cms.InputTag("qParts"),
#    relative = cms.bool(False),
#    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
#    EAFile_MiniIso = cms.FileInPath("PhysicsTools/NanoAOD/data/effAreaMuons_cone03_pfNeuHadronsAndPhotons_94X.txt"),
#)


qParts = cms.EDFilter("CandPtrSelector",
	src = cms.InputTag("packedPFCandidates"),
	cut = cms.string("pt()>1 && pt()>40 && (charge() > 0 || charge() < 0)"),
	
	)

qParts2 = cms.EDFilter("CandPtrSelector",
	src = cms.InputTag("lostTracks"),
	cut = cms.string(""),
	
	)


qTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
#    src = cms.InputTag("linkedObjects","qParts"),
   # src = cms.InputTag("muons"),
    src = cms.InputTag("qParts"),
    cut = cms.string(""), #we should not filter on cross linked collections
    name = cms.string("QP"),
    doc  = cms.string("generic pf tracks after basic selection (" + qParts.cut.value()+")"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table for the muons
    variables = cms.PSet(CandVars,
     #   ptErr   = Var("bestTrack().ptError()", float, doc = "ptError of the qpart track", precision=6),
     #   dxy = Var("bestTrack().dxy()", float, doc ="dxy of qpart", precision=10),
     #   dxyError = Var("bestTrack().dxyError()", float, doc="dxy error of qpart", precision=10),
     #   dz =  Var("bestTrack().dz()", float, doc ="dz of qpart", precision=10),
#	dzError =  Var("bestTrack().dzError()", float, doc ="dz error of qpart", precision=10),

        )
)

qMCMatchForTable = cms.EDProducer("MCMatcher",       # cut on deltaR, deltaPt/Pt; pick best by deltaR
    src         = qTable.src,                         # final reco collection
    matched     = cms.InputTag("finalGenParticles"),     # final mc-truth particle collection
    mcPdgId     = cms.vint32(13),               # one or more PDG ID (13 = mu); absolute values (see below)
    checkCharge = cms.bool(False),              # True = require RECO and MC objects to have the same charge
    mcStatus    = cms.vint32(1),                # PYTHIA status code (1 = stable, 2 = shower, 3 = hard scattering)
    maxDeltaR   = cms.double(0.3),              # Minimum deltaR for the match
    maxDPtRel   = cms.double(0.5),              # Minimum deltaPt/Pt for the match
    resolveAmbiguities    = cms.bool(True),     # Forbid two RECO objects to match to the same GEN object
    resolveByMatchQuality = cms.bool(True),    # False = just match input in order; True = pick lowest deltaR pair first
)

qMCTable = cms.EDProducer("CandMCMatchTableProducer",
    src     = qTable.src,
    mcMap   = cms.InputTag("qMCMatchForTable"),
    objName = qTable.name,
    objType = cms.string("Other"),
    branchName = cms.string("genPart"),
    docString = cms.string("MC matching to status==1 qparts"),
)


qTable2 = cms.EDProducer("SimpleCandidateFlatTableProducer",
#    src = cms.InputTag("linkedObjects","qParts"),
   # src = cms.InputTag("muons"),
    src = cms.InputTag("qParts2"),
    cut = cms.string(""), #we should not filter on cross linked collections
    name = cms.string("QP2"),
    doc  = cms.string("generic pf tracks after basic selection (" + qParts2.cut.value()+")"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table for the muons
    variables = cms.PSet(CandVars,
     #   ptErr   = Var("bestTrack().ptError()", float, doc = "ptError of the qpart track", precision=6),
     #   dxy = Var("bestTrack().dxy()", float, doc ="dxy of qpart", precision=10),
     #   dxyError = Var("bestTrack().dxyError()", float, doc="dxy error of qpart", precision=10),
     #   dz =  Var("bestTrack().dz()", float, doc ="dz of qpart", precision=10),
#	dzError =  Var("bestTrack().dzError()", float, doc ="dz error of qpart", precision=10),

        )
)

qMCTable2 = cms.EDProducer("CandMCMatchTableProducer",
    src     = qTable2.src,
    mcMap   = cms.InputTag("qMCMatchForTable"),
    objName = qTable.name,
    objType = cms.string("Other"),
    branchName = cms.string("genPart"),
    docString = cms.string("MC matching to status==1 qparts"),
)

#qSequence = cms.Sequence(qParts)
#qTables = cms.Sequence(linkedObjects + qParts + qTable)i
qTables = cms.Sequence( qParts + qTable + qParts2 + qTable2)
qMC = cms.Sequence( qMCMatchForTable + qMCTable)# +qMCTable2 )
#muonSequence = cms.Sequence(isoForMu + ptRatioRelForMu + slimmedMuonsWithUserData + finalMuons + finalLooseMuons )
#muonSequence = cms.Sequence(isoForMu + slimmedMuonsWithUserData +finalMuons + finalLooseMuons)
#muonMC = cms.Sequence(muonsMCMatchForTable + muonMCTable)
#muonTables = cms.Sequence(muonFSRphotons + muonFSRassociation + muonMVATTH + muonMVALowPt + muonTable + fsrTable)
#muonTables = cms.Sequence( linkedObjects + muonTable )
#_withUpdate_sequence = muonSequence.copy()
#_withUpdate_sequence.replace(isoForMu, slimmedMuonsUpdated+isoForMu)
#run2_miniAOD_80XLegacy.toReplaceWith(muonSequence, _withUpdate_sequence)

