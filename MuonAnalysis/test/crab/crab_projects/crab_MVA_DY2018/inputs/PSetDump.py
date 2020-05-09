import FWCore.ParameterSet.Config as cms

process = cms.Process("miniflatntuple")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()
)
process.CandVars = cms.PSet(
    charge = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('electric charge'),
        expr = cms.string('charge'),
        mcOnly = cms.bool(False),
        precision = cms.int32(-1),
        type = cms.string('int')
    ),
    eta = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('eta'),
        expr = cms.string('eta'),
        mcOnly = cms.bool(False),
        precision = cms.int32(12),
        type = cms.string('float')
    ),
    mass = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('mass'),
        expr = cms.string('mass'),
        mcOnly = cms.bool(False),
        precision = cms.int32(10),
        type = cms.string('float')
    ),
    pdgId = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('PDG code assigned by the event reconstruction (not by MC truth)'),
        expr = cms.string('pdgId'),
        mcOnly = cms.bool(False),
        precision = cms.int32(-1),
        type = cms.string('int')
    ),
    phi = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('phi'),
        expr = cms.string('phi'),
        mcOnly = cms.bool(False),
        precision = cms.int32(12),
        type = cms.string('float')
    ),
    pt = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('pt'),
        expr = cms.string('pt'),
        mcOnly = cms.bool(False),
        precision = cms.int32(-1),
        type = cms.string('float')
    )
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.P3Vars = cms.PSet(
    eta = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('eta'),
        expr = cms.string('eta'),
        mcOnly = cms.bool(False),
        precision = cms.int32(12),
        type = cms.string('float')
    ),
    phi = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('phi'),
        expr = cms.string('phi'),
        mcOnly = cms.bool(False),
        precision = cms.int32(12),
        type = cms.string('float')
    ),
    pt = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('pt'),
        expr = cms.string('pt'),
        mcOnly = cms.bool(False),
        precision = cms.int32(-1),
        type = cms.string('float')
    )
)

process.P4Vars = cms.PSet(
    eta = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('eta'),
        expr = cms.string('eta'),
        mcOnly = cms.bool(False),
        precision = cms.int32(12),
        type = cms.string('float')
    ),
    mass = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('mass'),
        expr = cms.string('mass'),
        mcOnly = cms.bool(False),
        precision = cms.int32(10),
        type = cms.string('float')
    ),
    phi = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('phi'),
        expr = cms.string('phi'),
        mcOnly = cms.bool(False),
        precision = cms.int32(12),
        type = cms.string('float')
    ),
    pt = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('pt'),
        expr = cms.string('pt'),
        mcOnly = cms.bool(False),
        precision = cms.int32(-1),
        type = cms.string('float')
    )
)

process.PTVars = cms.PSet(
    phi = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('phi'),
        expr = cms.string('phi'),
        mcOnly = cms.bool(False),
        precision = cms.int32(12),
        type = cms.string('float')
    ),
    pt = cms.PSet(
        compression = cms.string('none'),
        doc = cms.string('pt'),
        expr = cms.string('pt'),
        mcOnly = cms.bool(False),
        precision = cms.int32(-1),
        type = cms.string('float')
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.QGTagger = cms.EDProducer("QGTagger",
    jetsLabel = cms.string('QGL_AK4PFchs'),
    srcJets = cms.InputTag("ak4PFJetsCHS"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcVertexCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    useQualityCuts = cms.bool(False)
)


process.ak4BetaStar = cms.EDProducer("BetaStarPackedCandidateVarProducer",
    maxDR = cms.double(0.4),
    srcJet = cms.InputTag("slimmedJets"),
    srcPF = cms.InputTag("packedPFCandidates")
)


process.ak4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.bJetVars = cms.EDProducer("JetRegressionVarProducer",
    gpsrc = cms.InputTag("prunedGenParticles"),
    pvsrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    src = cms.InputTag("updatedJets"),
    svsrc = cms.InputTag("slimmedSecondaryVertices")
)


process.bjetMVA = cms.EDProducer("BJetEnergyRegressionMVA",
    backend = cms.string('TMVA'),
    isClassifier = cms.bool(False),
    name = cms.string('JetReg'),
    pvsrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rhosrc = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("linkedObjects","jets"),
    svsrc = cms.InputTag("slimmedSecondaryVertices"),
    variables = cms.PSet(
        Jet_eta = cms.string('eta'),
        Jet_leadTrackPt = cms.string("userFloat(\'leadTrackPt\')"),
        Jet_leptonDeltaR = cms.string("?overlaps(\'muons\').size()>0?deltaR(eta,phi,overlaps(\'muons\')[0].eta,overlaps(\'muons\')[0].phi):\n\t\t\t\t(?overlaps(\'electrons\').size()>0?deltaR(eta,phi,overlaps(\'electrons\')[0].eta,overlaps(\'electrons\')[0].phi):\n\t\t\t\t0)"),
        Jet_leptonPt = cms.string("?overlaps(\'muons\').size()>0?overlaps(\'muons\')[0].pt():(?overlaps(\'electrons\').size()>0?overlaps(\'electrons\')[0].pt():0)"),
        Jet_leptonPtRel = cms.string("userFloat(\'leptonPtRelv0\')"),
        Jet_mt = cms.string('mt'),
        Jet_neEmEF = cms.string('neutralEmEnergy()/energy()'),
        Jet_neHEF = cms.string('neutralHadronEnergy()/energy()'),
        Jet_pt = cms.string('pt'),
        Jet_vtx3dL = cms.string("userFloat(\'vtx3dL\')"),
        Jet_vtx3deL = cms.string("userFloat(\'vtx3deL\')"),
        Jet_vtxMass = cms.string("userFloat(\'vtxMass\')"),
        Jet_vtxNtrk = cms.string("userInt(\'vtxNtrk\')"),
        Jet_vtxPt = cms.string("userFloat(\'vtxPt\')")
    ),
    variablesOrder = cms.vstring(
        'Jet_pt', 
        'nPVs', 
        'Jet_eta', 
        'Jet_mt', 
        'Jet_leadTrackPt', 
        'Jet_leptonPtRel', 
        'Jet_leptonPt', 
        'Jet_leptonDeltaR', 
        'Jet_neHEF', 
        'Jet_neEmEF', 
        'Jet_vtxPt', 
        'Jet_vtxMass', 
        'Jet_vtx3dL', 
        'Jet_vtxNtrk', 
        'Jet_vtx3deL'
    ),
    weightFile = cms.FileInPath('PhysicsTools/NanoAOD/data/bjet-regression.xml')
)


process.bjetNN = cms.EDProducer("BJetEnergyRegressionMVA",
    backend = cms.string('TF'),
    inputTensorName = cms.string('ffwd_inp'),
    isClassifier = cms.bool(False),
    nThreads = cms.uint32(1),
    name = cms.string('JetRegNN'),
    outputFormulas = cms.vstring(
        'at(0)*0.28492164611816406+1.0596693754196167', 
        '0.5*(at(2)-at(1))*0.28492164611816406'
    ),
    outputNames = cms.vstring(
        'corr', 
        'res'
    ),
    outputTensorName = cms.string('ffwd_out/BiasAdd'),
    pvsrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rhosrc = cms.InputTag("fixedGridRhoFastjetAll"),
    singleThreadPool = cms.string('no_threads'),
    src = cms.InputTag("linkedObjects","jets"),
    svsrc = cms.InputTag("slimmedSecondaryVertices"),
    variables = cms.PSet(
        Jet_chEmEF = cms.string('chargedEmEnergyFraction()'),
        Jet_chHEF = cms.string('chargedHadronEnergyFraction()'),
        Jet_eta = cms.string('eta'),
        Jet_leadTrackPt = cms.string("userFloat(\'leadTrackPt\')"),
        Jet_leptonDeltaR = cms.string("userFloat(\'leptonDeltaR\')"),
        Jet_leptonPtRel = cms.string("userFloat(\'leptonPtRelv0\')"),
        Jet_leptonPtRelInv = cms.string("userFloat(\'leptonPtRelInvv0\')*jecFactor(\'Uncorrected\')"),
        Jet_mass = cms.string("mass*jecFactor(\'Uncorrected\')"),
        Jet_mt = cms.string("mt*jecFactor(\'Uncorrected\')"),
        Jet_neEmEF = cms.string('neutralEmEnergyFraction()'),
        Jet_neHEF = cms.string('neutralHadronEnergyFraction()'),
        Jet_pt = cms.string("pt*jecFactor(\'Uncorrected\')"),
        Jet_ptd = cms.string("userFloat(\'ptD\')"),
        Jet_vtx3dL = cms.string("userFloat(\'vtx3dL\')"),
        Jet_vtx3deL = cms.string("userFloat(\'vtx3deL\')"),
        Jet_vtxMass = cms.string("userFloat(\'vtxMass\')"),
        Jet_vtxNtrk = cms.string("userInt(\'vtxNtrk\')"),
        Jet_vtxPt = cms.string("userFloat(\'vtxPt\')"),
        isEle = cms.string("?abs(userInt(\'leptonPdgId\'))==11?1:0"),
        isMu = cms.string("?abs(userInt(\'leptonPdgId\'))==13?1:0"),
        isOther = cms.string("?userInt(\'leptonPdgId\')==0?1:0")
    ),
    variablesOrder = cms.vstring(
        'Jet_pt', 
        'Jet_eta', 
        'rho', 
        'Jet_mt', 
        'Jet_leadTrackPt', 
        'Jet_leptonPtRel', 
        'Jet_leptonDeltaR', 
        'Jet_neHEF', 
        'Jet_neEmEF', 
        'Jet_vtxPt', 
        'Jet_vtxMass', 
        'Jet_vtx3dL', 
        'Jet_vtxNtrk', 
        'Jet_vtx3deL', 
        'Jet_numDaughters_pt03', 
        'Jet_energyRing_dR0_em_Jet_rawEnergy', 
        'Jet_energyRing_dR1_em_Jet_rawEnergy', 
        'Jet_energyRing_dR2_em_Jet_rawEnergy', 
        'Jet_energyRing_dR3_em_Jet_rawEnergy', 
        'Jet_energyRing_dR4_em_Jet_rawEnergy', 
        'Jet_energyRing_dR0_neut_Jet_rawEnergy', 
        'Jet_energyRing_dR1_neut_Jet_rawEnergy', 
        'Jet_energyRing_dR2_neut_Jet_rawEnergy', 
        'Jet_energyRing_dR3_neut_Jet_rawEnergy', 
        'Jet_energyRing_dR4_neut_Jet_rawEnergy', 
        'Jet_energyRing_dR0_ch_Jet_rawEnergy', 
        'Jet_energyRing_dR1_ch_Jet_rawEnergy', 
        'Jet_energyRing_dR2_ch_Jet_rawEnergy', 
        'Jet_energyRing_dR3_ch_Jet_rawEnergy', 
        'Jet_energyRing_dR4_ch_Jet_rawEnergy', 
        'Jet_energyRing_dR0_mu_Jet_rawEnergy', 
        'Jet_energyRing_dR1_mu_Jet_rawEnergy', 
        'Jet_energyRing_dR2_mu_Jet_rawEnergy', 
        'Jet_energyRing_dR3_mu_Jet_rawEnergy', 
        'Jet_energyRing_dR4_mu_Jet_rawEnergy', 
        'Jet_chHEF', 
        'Jet_chEmEF', 
        'Jet_leptonPtRelInv', 
        'isEle', 
        'isMu', 
        'isOther', 
        'Jet_mass', 
        'Jet_ptd'
    ),
    weightFile = cms.FileInPath('PhysicsTools/NanoAOD/data/breg_training_2017.pb')
)


process.corrT1METJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('Additional low-pt jets for Type-1 MET re-correction'),
    extension = cms.bool(False),
    name = cms.string('CorrT1METJet'),
    singleton = cms.bool(False),
    src = cms.InputTag("corrT1METJets"),
    variables = cms.PSet(
        area = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('jet catchment area, for JECs'),
            expr = cms.string('jetArea()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        rawPt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string("pt()*jecFactor(\'Uncorrected\')"),
            expr = cms.string("pt()*jecFactor(\'Uncorrected\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        )
    )
)


process.fatJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(' pt > 170'),
    doc = cms.string('slimmedJetsAK8, i.e. ak8 fat jets for boosted analysis'),
    extension = cms.bool(False),
    name = cms.string('FatJet'),
    singleton = cms.bool(False),
    src = cms.InputTag("finalJetsAK8"),
    variables = cms.PSet(
        area = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('jet catchment area, for JECs'),
            expr = cms.string('jetArea()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagCMVA = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('CMVA V2 btag discriminator'),
            expr = cms.string("bDiscriminator(\'pfCombinedMVAV2BJetTags\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagCSVV2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string(' pfCombinedInclusiveSecondaryVertexV2 b-tag discriminator (aka CSVV2)'),
            expr = cms.string("bDiscriminator(\'pfCombinedInclusiveSecondaryVertexV2BJetTags\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDDBvL = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepDoubleX (mass-decorrelated) discriminator for H(Z)->bb vs QCD'),
            expr = cms.string("bDiscriminator(\'pfMassIndependentDeepDoubleBvLJetTags:probHbb\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDDBvL_noMD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepDoubleX discriminator (no mass-decorrelation) for H(Z)->bb vs QCD'),
            expr = cms.string("bDiscriminator(\'pfDeepDoubleBvLJetTags:probHbb\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDDCvB = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepDoubleX (mass-decorrelated) discriminator for H(Z)->cc vs H(Z)->bb'),
            expr = cms.string("bDiscriminator(\'pfMassIndependentDeepDoubleCvBJetTags:probHcc\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDDCvB_noMD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepDoubleX discriminator (no mass-decorrelation) for H(Z)->cc vs H(Z)->bb'),
            expr = cms.string("bDiscriminator(\'pfDeepDoubleCvBJetTags:probHcc\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDDCvL = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepDoubleX (mass-decorrelated) discriminator for H(Z)->cc vs QCD'),
            expr = cms.string("bDiscriminator(\'pfMassIndependentDeepDoubleCvLJetTags:probHcc\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDDCvL_noMD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepDoubleX discriminator (no mass-decorrelation) for H(Z)->cc vs QCD'),
            expr = cms.string("bDiscriminator(\'pfDeepDoubleCvLJetTags:probHcc\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDeepB = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepCSV b+bb tag discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepCSVJetTags:probb\')+bDiscriminator(\'pfDeepCSVJetTags:probbb\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagHbb = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Higgs to BB tagger discriminator'),
            expr = cms.string("bDiscriminator(\'pfBoostedDoubleSecondaryVertexAK8BJetTags\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_H4qvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger H->4q vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:H4qvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_HbbvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger H->bb vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:HbbvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_TvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger top vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_WvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger W vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:WvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_ZHbbvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger Z/H->bb vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHbbvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_ZHccvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger Z/H->cc vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHccvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_ZbbvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger Z->bb vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZbbvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_ZvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger Z vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_bbvsLight = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger Z/H/gluon->bb vs light flavour discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:bbvsLight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTagMD_ccvsLight = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass-decorrelated DeepBoostedJet tagger Z/H/gluon->cc vs light flavour discriminator'),
            expr = cms.string("bDiscriminator(\'pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ccvsLight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTag_H = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepBoostedJet tagger H(bb,cc,4q) sum'),
            expr = cms.string("bDiscriminator(\'pfDeepBoostedJetTags:probHbb\')+bDiscriminator(\'pfDeepBoostedJetTags:probHcc\')+bDiscriminator(\'pfDeepBoostedJetTags:probHqqqq\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTag_QCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepBoostedJet tagger QCD(bb,cc,b,c,others) sum'),
            expr = cms.string("bDiscriminator(\'pfDeepBoostedJetTags:probQCDbb\')+bDiscriminator(\'pfDeepBoostedJetTags:probQCDcc\')+bDiscriminator(\'pfDeepBoostedJetTags:probQCDb\')+bDiscriminator(\'pfDeepBoostedJetTags:probQCDc\')+bDiscriminator(\'pfDeepBoostedJetTags:probQCDothers\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTag_QCDothers = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepBoostedJet tagger QCDothers value'),
            expr = cms.string("bDiscriminator(\'pfDeepBoostedJetTags:probQCDothers\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTag_TvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepBoostedJet tagger top vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepBoostedDiscriminatorsJetTags:TvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTag_WvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepBoostedJet tagger W vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepBoostedDiscriminatorsJetTags:WvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        deepTag_ZvsQCD = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepBoostedJet tagger Z vs QCD discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepBoostedDiscriminatorsJetTags:ZvsQCD\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        jetId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto'),
            expr = cms.string("userInt(\'tightId\')*2+4*userInt(\'tightIdLepVeto\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mass'),
            expr = cms.string('mass'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        msoftdrop = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Corrected soft drop mass with PUPPI'),
            expr = cms.string("groomedMass(\'SoftDropPuppi\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        n2b1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('N2 with beta=1'),
            expr = cms.string("userFloat(\'ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        n3b1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('N3 with beta=1'),
            expr = cms.string("userFloat(\'ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN3\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        rawFactor = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('1 - Factor to get back to raw pT'),
            expr = cms.string("1.-jecFactor(\'Uncorrected\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        subJetIdx1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of first subjet'),
            expr = cms.string("?nSubjetCollections()>0 && subjets(\'SoftDropPuppi\').size()>0?subjets(\'SoftDropPuppi\')[0].key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        subJetIdx2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of second subjet'),
            expr = cms.string("?nSubjetCollections()>0 && subjets(\'SoftDropPuppi\').size()>1?subjets(\'SoftDropPuppi\')[1].key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        tau1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (1 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Puppi:tau1\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        tau2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (2 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Puppi:tau2\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        tau3 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (3 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Puppi:tau3\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        tau4 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (4 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Puppi:tau4\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        )
    )
)


process.finalGenParticles = cms.EDProducer("GenParticlePruner",
    select = cms.vstring(
        'drop *', 
        'keep++ abs(pdgId) == 15 & (pt > 15 ||  isPromptDecayed() )', 
        'keep+ abs(pdgId) == 15 ', 
        'keep+ abs(pdgId) == 211', 
        '+keep pdgId == 22 && status == 1 && (pt > 10 || isPromptFinalState())', 
        '+keep abs(pdgId) == 11 || abs(pdgId) == 13 || abs(pdgId) == 15', 
        'drop abs(pdgId)= 2212 && abs(pz) > 1000', 
        'keep (400 < abs(pdgId) < 600) || (4000 < abs(pdgId) < 6000)', 
        'keep abs(pdgId) == 12 || abs(pdgId) == 14 || abs(pdgId) == 16', 
        'keep status == 3 || (status > 20 && status < 30)', 
        'keep isHardProcess() ||  fromHardProcessDecayed()  || fromHardProcessFinalState() || (statusFlags().fromHardProcess() && statusFlags().isLastCopy())', 
        'keep  (status > 70 && status < 80 && pt > 15) ', 
        'keep abs(pdgId) == 23 || abs(pdgId) == 24 || abs(pdgId) == 25 || abs(pdgId) == 37 ', 
        'keep abs(pdgId) == 311 && abs(eta) < 2.5 && pt > 1 ', 
        'keep abs(pdgId) == 321 && abs(eta) < 2.5 && pt > 1', 
        'keep (1000001 <= abs(pdgId) <= 1000039 ) || ( 2000001 <= abs(pdgId) <= 2000015)'
    ),
    src = cms.InputTag("prunedGenParticles")
)


process.fsrTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('Final state radiation photons emitted by muons'),
    extension = cms.bool(False),
    name = cms.string('FsrPhoton'),
    singleton = cms.bool(False),
    src = cms.InputTag("muonFSRphotons"),
    variables = cms.PSet(
        dROverEt2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('deltaR to associated muon divided by photon et2'),
            expr = cms.string("userFloat(\'dROverEt2\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        muonIdx = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of associated muon'),
            expr = cms.string("?hasUserCand(\'associatedMuon\')?userCand(\'associatedMuon\').key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        relIso03 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('relative isolation in a 0.3 cone without CHS'),
            expr = cms.string("userFloat(\'relIso03\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        )
    )
)


process.genJetAK8FlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("slimmedGenJetsAK8"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.genJetAK8FlavourTable = cms.EDProducer("GenJetFlavourTableProducer",
    cut = cms.string('pt > 100.'),
    deltaR = cms.double(0.1),
    jetFlavourInfos = cms.InputTag("genJetAK8FlavourAssociation"),
    name = cms.string('GenJetAK8'),
    src = cms.InputTag("slimmedGenJetsAK8")
)


process.genJetAK8Table = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string('pt > 100.'),
    doc = cms.string('slimmedGenJetsAK8, i.e. ak8 Jets made with visible genparticles'),
    extension = cms.bool(False),
    name = cms.string('GenJetAK8'),
    singleton = cms.bool(False),
    src = cms.InputTag("slimmedGenJetsAK8"),
    variables = cms.PSet(
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mass'),
            expr = cms.string('mass'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        )
    )
)


process.genJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("slimmedGenJets"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.4)
)


process.genJetFlavourTable = cms.EDProducer("GenJetFlavourTableProducer",
    cut = cms.string('pt > 10'),
    deltaR = cms.double(0.1),
    jetFlavourInfos = cms.InputTag("slimmedGenJetsFlavourInfos"),
    name = cms.string('GenJet'),
    src = cms.InputTag("slimmedGenJets")
)


process.genJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string('pt > 10'),
    doc = cms.string('slimmedGenJets, i.e. ak4 Jets made with visible genparticles'),
    extension = cms.bool(False),
    name = cms.string('GenJet'),
    singleton = cms.bool(False),
    src = cms.InputTag("slimmedGenJets"),
    variables = cms.PSet(
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mass'),
            expr = cms.string('mass'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        )
    )
)


process.genParticleTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('interesting gen particles '),
    extension = cms.bool(False),
    name = cms.string('GenPart'),
    singleton = cms.bool(False),
    src = cms.InputTag("prunedGenParticles"),
    variables = cms.PSet(
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            type = cms.string('float')
        ),
        genPartIdxMother = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of the mother particle'),
            expr = cms.string('?numberOfMothers>0?motherRef(0).key():-1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mass stored for all particles with mass > 10 GeV and photons with mass > 1 GeV, plus W/Z and BSM particles. For other particles you can lookup from PDGID'),
            expr = cms.string('?mass>10 || (pdgId==22 && mass > 1) || abs(pdgId)==24 || pdgId==23 || abs(pdgId)>1000000?mass:0'),
            mcOnly = cms.bool(False),
            precision = cms.string('?(abs(pdgId)==6 && statusFlags().isLastCopy())?20:8'),
            type = cms.string('float')
        ),
        pdgId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('PDG id'),
            expr = cms.string('pdgId'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            type = cms.string('float')
        ),
        status = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Particle status. 1=stable'),
            expr = cms.string('status'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        statusFlags = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('gen status flags stored bitwise, bits are: 0 : isPrompt, 1 : isDecayedLeptonHadron, 2 : isTauDecayProduct, 3 : isPromptTauDecayProduct, 4 : isDirectTauDecayProduct, 5 : isDirectPromptTauDecayProduct, 6 : isDirectHadronDecayProduct, 7 : isHardProcess, 8 : fromHardProcess, 9 : isHardProcessTauDecayProduct, 10 : isDirectHardProcessTauDecayProduct, 11 : fromHardProcessBeforeFSR, 12 : isFirstCopy, 13 : isLastCopy, 14 : isLastCopyBeforeFSR, '),
            expr = cms.string('statusFlags().isLastCopyBeforeFSR()                  * 16384 +statusFlags().isLastCopy()                           * 8192  +statusFlags().isFirstCopy()                          * 4096  +statusFlags().fromHardProcessBeforeFSR()             * 2048  +statusFlags().isDirectHardProcessTauDecayProduct()   * 1024  +statusFlags().isHardProcessTauDecayProduct()         * 512   +statusFlags().fromHardProcess()                      * 256   +statusFlags().isHardProcess()                        * 128   +statusFlags().isDirectHadronDecayProduct()           * 64    +statusFlags().isDirectPromptTauDecayProduct()        * 32    +statusFlags().isDirectTauDecayProduct()              * 16    +statusFlags().isPromptTauDecayProduct()              * 8     +statusFlags().isTauDecayProduct()                    * 4     +statusFlags().isDecayedLeptonHadron()                * 2     +statusFlags().isPrompt()                             * 1      '),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        )
    )
)


process.genSubJetAK8Table = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('slimmedGenJetsAK8SoftDropSubJets, i.e. subjets of ak8 Jets made with visible genparticles'),
    extension = cms.bool(False),
    name = cms.string('SubGenJetAK8'),
    singleton = cms.bool(False),
    src = cms.InputTag("slimmedGenJetsAK8SoftDropSubJets"),
    variables = cms.PSet(
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mass'),
            expr = cms.string('mass'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        )
    )
)


process.isoForMu = cms.EDProducer("MuonIsoValueMapProducer",
    EAFile_MiniIso = cms.FileInPath('PhysicsTools/NanoAOD/data/effAreaMuons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    relative = cms.bool(False),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedMuons")
)


process.jercVars = cms.EDProducer("BetaStarPackedCandidateVarProducer",
    maxDR = cms.double(0.4),
    srcJet = cms.InputTag("updatedJets"),
    srcPF = cms.InputTag("packedPFCandidates")
)


process.jetCorrFactorsAK8 = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'
    ),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJetsAK8"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.jetCorrFactorsNano = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.jetMCTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    extension = cms.bool(True),
    name = cms.string('Jet'),
    singleton = cms.bool(False),
    src = cms.InputTag("linkedObjects","jets"),
    variables = cms.PSet(
        genJetIdx = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of matched gen jet'),
            expr = cms.string('?genJetFwdRef().backRef().isNonnull()?genJetFwdRef().backRef().key():-1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        hadronFlavour = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('flavour from hadron ghost clustering'),
            expr = cms.string('hadronFlavour()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        partonFlavour = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('flavour from parton matching'),
            expr = cms.string('partonFlavour()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        )
    )
)


process.jetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('slimmedJets, i.e. ak4 PFJets CHS with JECs applied, after basic selection (pt > 15)'),
    extension = cms.bool(False),
    externalVariables = cms.PSet(
        bRegCorr = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt correction for b-jet energy regression'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            src = cms.InputTag("bjetNN","corr"),
            type = cms.string('float')
        ),
        bRegRes = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('res on pt corrected with b-jet regression'),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            src = cms.InputTag("bjetNN","res"),
            type = cms.string('float')
        )
    ),
    name = cms.string('Jet'),
    singleton = cms.bool(False),
    src = cms.InputTag("linkedObjects","jets"),
    variables = cms.PSet(
        area = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('jet catchment area, for JECs'),
            expr = cms.string('jetArea()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagCMVA = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('CMVA V2 btag discriminator'),
            expr = cms.string("bDiscriminator(\'pfCombinedMVAV2BJetTags\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagCSVV2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string(' pfCombinedInclusiveSecondaryVertexV2 b-tag discriminator (aka CSVV2)'),
            expr = cms.string("bDiscriminator(\'pfCombinedInclusiveSecondaryVertexV2BJetTags\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDeepB = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepCSV b+bb tag discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepCSVJetTags:probb\')+bDiscriminator(\'pfDeepCSVJetTags:probbb\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDeepC = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepCSV charm btag discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepCSVJetTags:probc\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDeepFlavB = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepFlavour b+bb+lepb tag discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepFlavourJetTags:probb\')+bDiscriminator(\'pfDeepFlavourJetTags:probbb\')+bDiscriminator(\'pfDeepFlavourJetTags:problepb\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDeepFlavC = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepFlavour charm tag discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepFlavourJetTags:probc\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        chEmEF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('charged Electromagnetic Energy Fraction'),
            expr = cms.string('chargedEmEnergyFraction()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        chHEF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('charged Hadron Energy Fraction'),
            expr = cms.string('chargedHadronEnergyFraction()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        electronIdx1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of first matching electron'),
            expr = cms.string("?overlaps(\'electrons\').size()>0?overlaps(\'electrons\')[0].key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        electronIdx2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of second matching electron'),
            expr = cms.string("?overlaps(\'electrons\').size()>1?overlaps(\'electrons\')[1].key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        jercCHF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Charged Hadron Energy Fraction with the JERC group definition'),
            expr = cms.string("userFloat(\'jercCHF\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        jercCHPUF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Pileup Charged Hadron Energy Fraction with the JERC group definition'),
            expr = cms.string("userFloat(\'jercCHPUF\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        jetId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto'),
            expr = cms.string("userInt(\'tightId\')*2+4*userInt(\'tightIdLepVeto\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mass'),
            expr = cms.string('mass'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        muEF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon Energy Fraction'),
            expr = cms.string('muonEnergyFraction()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        muonIdx1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of first matching muon'),
            expr = cms.string("?overlaps(\'muons\').size()>0?overlaps(\'muons\')[0].key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        muonIdx2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of second matching muon'),
            expr = cms.string("?overlaps(\'muons\').size()>1?overlaps(\'muons\')[1].key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        nConstituents = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Number of particles in the jet'),
            expr = cms.string('numberOfDaughters()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        nElectrons = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('number of electrons in the jet'),
            expr = cms.string("?hasOverlaps(\'electrons\')?overlaps(\'electrons\').size():0"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        nMuons = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('number of muons in the jet'),
            expr = cms.string("?hasOverlaps(\'muons\')?overlaps(\'muons\').size():0"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        neEmEF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('neutral Electromagnetic Energy Fraction'),
            expr = cms.string('neutralEmEnergyFraction()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        neHEF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('neutral Hadron Energy Fraction'),
            expr = cms.string('neutralHadronEnergyFraction()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        puId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Pilup ID flags'),
            expr = cms.string("userInt(\'pileupJetId:fullId\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        qgl = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Quark vs Gluon likelihood discriminator'),
            expr = cms.string("userFloat(\'qgl\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        rawFactor = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('1 - Factor to get back to raw pT'),
            expr = cms.string("1.-jecFactor(\'Uncorrected\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        )
    )
)


process.linkedObjects = cms.EDProducer("PATObjectCrossLinker",
    electrons = cms.InputTag("slimmedElectrons"),
    jets = cms.InputTag("finalJets"),
    muons = cms.InputTag("finalMuons"),
    photons = cms.InputTag("slimmedPhotons"),
    taus = cms.InputTag("slimmedTaus")
)


process.looseJetId = cms.EDProducer("PatJetIDValueMapProducer",
    filterParams = cms.PSet(
        quality = cms.string('LOOSE'),
        version = cms.string('WINTER16')
    ),
    src = cms.InputTag("updatedJets")
)


process.looseJetIdAK8 = cms.EDProducer("PatJetIDValueMapProducer",
    filterParams = cms.PSet(
        quality = cms.string('LOOSE'),
        version = cms.string('WINTER16')
    ),
    src = cms.InputTag("updatedJetsAK8")
)


process.muonFSRAssociator = cms.EDProducer("MuonFSRAssociator")


process.muonFSRProducer = cms.EDProducer("MuonFSRProducer",
    deltaROverEt2Max = cms.double(0.05),
    isolation = cms.double(2),
    muonEtaMax = cms.double(2.4),
    muonPtMin = cms.double(20),
    muons = cms.InputTag("slimmedMuons"),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    photonPtMin = cms.double(2),
    slimmedElectrons = cms.InputTag("slimmedElectrons")
)


process.muonFSRassociation = cms.EDProducer("MuonFSRAssociator",
    muons = cms.InputTag("linkedObjects","muons"),
    photons = cms.InputTag("muonFSRphotons")
)


process.muonFSRphotons = cms.EDProducer("MuonFSRProducer",
    deltaROverEt2Max = cms.double(0.05),
    isolation = cms.double(2),
    muonEtaMax = cms.double(2.4),
    muonPtMin = cms.double(20),
    muons = cms.InputTag("linkedObjects","muons"),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    photonPtMin = cms.double(2),
    slimmedElectrons = cms.InputTag("slimmedElectrons")
)


process.muonMCTable = cms.EDProducer("CandMCMatchTableProducer",
    branchName = cms.string('genPart'),
    docString = cms.string('MC matching to status==1 muons'),
    mcMap = cms.InputTag("muonsMCMatchForTable"),
    objName = cms.string('Muon'),
    objType = cms.string('Muon'),
    src = cms.InputTag("linkedObjects","muons")
)


process.muonMVALowPt = cms.EDProducer("MuonBaseMVAValueMapProducer",
    isClassifier = cms.bool(True),
    name = cms.string('muonMVALowPt'),
    src = cms.InputTag("linkedObjects","muons"),
    variables = cms.PSet(
        LepGood_dxy = cms.string("log(abs(dB(\'PV2D\')))"),
        LepGood_dz = cms.string("log(abs(dB(\'PVDZ\')))"),
        LepGood_eta = cms.string('eta'),
        LepGood_jetDF = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?max(userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probbb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:problepb\'),0.0):0.0"),
        LepGood_jetNDauChargedMVASel = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'jetNDauChargedMVASel\'):0"),
        LepGood_jetPtRatio = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?min(userFloat(\'ptRatio\'),1.5):1.0/(1.0+(pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - pfIsolationR04().sumPUPt/2,0.0))/pt)"),
        LepGood_jetPtRelv2 = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'ptRel\'):0"),
        LepGood_miniRelIsoCharged = cms.string("userFloat(\'miniIsoChg\')/pt"),
        LepGood_miniRelIsoNeutral = cms.string("(userFloat(\'miniIsoAll\')-userFloat(\'miniIsoChg\'))/pt"),
        LepGood_pt = cms.string('pt'),
        LepGood_segmentComp = cms.string('segmentCompatibility'),
        LepGood_sip3d = cms.string("abs(dB(\'PV3D\')/edB(\'PV3D\'))")
    ),
    variablesOrder = cms.vstring(
        'LepGood_pt', 
        'LepGood_eta', 
        'LepGood_jetNDauChargedMVASel', 
        'LepGood_miniRelIsoCharged', 
        'LepGood_miniRelIsoNeutral', 
        'LepGood_jetPtRelv2', 
        'LepGood_jetDF', 
        'LepGood_jetPtRatio', 
        'LepGood_dxy', 
        'LepGood_sip3d', 
        'LepGood_dz', 
        'LepGood_segmentComp'
    ),
    weightFile = cms.FileInPath('PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml')
)


process.muonMVATTH = cms.EDProducer("MuonBaseMVAValueMapProducer",
    isClassifier = cms.bool(True),
    name = cms.string('muonMVATTH'),
    src = cms.InputTag("linkedObjects","muons"),
    variables = cms.PSet(
        LepGood_dxy = cms.string("log(abs(dB(\'PV2D\')))"),
        LepGood_dz = cms.string("log(abs(dB(\'PVDZ\')))"),
        LepGood_eta = cms.string('eta'),
        LepGood_jetDF = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?max(userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probbb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:problepb\'),0.0):0.0"),
        LepGood_jetNDauChargedMVASel = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'jetNDauChargedMVASel\'):0"),
        LepGood_jetPtRatio = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?min(userFloat(\'ptRatio\'),1.5):1.0/(1.0+(pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - pfIsolationR04().sumPUPt/2,0.0))/pt)"),
        LepGood_jetPtRelv2 = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'ptRel\'):0"),
        LepGood_miniRelIsoCharged = cms.string("userFloat(\'miniIsoChg\')/pt"),
        LepGood_miniRelIsoNeutral = cms.string("(userFloat(\'miniIsoAll\')-userFloat(\'miniIsoChg\'))/pt"),
        LepGood_pt = cms.string('pt'),
        LepGood_segmentComp = cms.string('segmentCompatibility'),
        LepGood_sip3d = cms.string("abs(dB(\'PV3D\')/edB(\'PV3D\'))")
    ),
    variablesOrder = cms.vstring(
        'LepGood_pt', 
        'LepGood_eta', 
        'LepGood_jetNDauChargedMVASel', 
        'LepGood_miniRelIsoCharged', 
        'LepGood_miniRelIsoNeutral', 
        'LepGood_jetPtRelv2', 
        'LepGood_jetDF', 
        'LepGood_jetPtRatio', 
        'LepGood_dxy', 
        'LepGood_sip3d', 
        'LepGood_dz', 
        'LepGood_segmentComp'
    ),
    weightFile = cms.FileInPath('PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml')
)


process.muonTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('slimmedMuons after basic selection (pt>1 && pt<40)'),
    extension = cms.bool(False),
    externalVariables = cms.PSet(
        mvaLowPt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Low pt muon ID score'),
            mcOnly = cms.bool(False),
            precision = cms.int32(14),
            src = cms.InputTag("muonMVALowPt"),
            type = cms.string('float')
        ),
        mvaTTH = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('TTH MVA lepton ID score'),
            mcOnly = cms.bool(False),
            precision = cms.int32(14),
            src = cms.InputTag("muonMVATTH"),
            type = cms.string('float')
        )
    ),
    name = cms.string('Muon'),
    singleton = cms.bool(False),
    src = cms.InputTag("linkedObjects","muons"),
    variables = cms.PSet(
        LepGood_jetDF = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('deep flavor jet tagging'),
            expr = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?max(userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probbb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:problepb\'),0.0):0.0"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        LepGood_jetNDauChargedMVASel = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('test'),
            expr = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'jetNDauChargedMVASel\'):0"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        LepGood_jetPtRatio = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt ratio of mu and leading jet'),
            expr = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?min(userFloat(\'ptRatio\'),1.5):1.0/(1.0+(pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - pfIsolationR04().sumPUPt/2,0.0))/pt)"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        LepGood_jetPtRelv2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('relative pt of mu and leading jet'),
            expr = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'ptRel\'):0"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        LepGood_miniRelIsoNeutral = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('relative mini isolation neutral component'),
            expr = cms.string("(userFloat(\'miniIsoAll\')-userFloat(\'miniIsoChg\'))/pt"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        charge = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('electric charge'),
            expr = cms.string('charge'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        chi2LocalMomentum = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('chi2 value for the STA-TK matching of local momentum'),
            expr = cms.string('combinedQuality().chi2LocalMomentum'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        chi2LocalPosition = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('chi2 value for the STA-TK matching of local position'),
            expr = cms.string('combinedQuality().chi2LocalPosition'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        dxy = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('dxy (with sign) wrt first PV,calculated from inner track, in cm'),
            expr = cms.string("dB(\'PV2D\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        dxyErr = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('dxy uncertainty, in cm'),
            expr = cms.string("edB(\'PV2D\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        dz = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('dz (with sign) wrt first PV,calculated from inner track, in cm'),
            expr = cms.string("dB(\'PVDZ\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        dzErr = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('dz uncertainty, in cm'),
            expr = cms.string("abs(edB(\'PVDZ\'))"),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        glbKink = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('log(2 + glbKink); value of the kink algorithm applied to the global track'),
            expr = cms.string('combinedQuality().glbKink'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        glbTrackProbability = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('the tail probability (-ln(P)) of the global fit'),
            expr = cms.string('combinedQuality().glbTrackProbability'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        globalTrackNonNull = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon contains a global track'),
            expr = cms.string('globalTrack().isNonnull()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        highPtId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('high-pT cut-based ID (1 = tracker high pT, 2 = global high pT, which includes tracker high pT)'),
            expr = cms.string("?passed(\'CutBasedIdGlobalHighPt\')?2:passed(\'CutBasedIdTrkHighPt\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('uint8')
        ),
        inTimeMuon = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('inTimeMuon ID'),
            expr = cms.string("passed(\'InTimeMuon\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        innerTrackCharge = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('charge of the inner track, else 0'),
            expr = cms.string('?innerTrack().isNonnull()?innerTrack().charge():0'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        innerTrackNonNull = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon contains an inner track'),
            expr = cms.string('innerTrack().isNonnull()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        innerTrackNormalizedChi2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('inner track chi-squared divided by n.d.o.f. (or chi-squared * 1e6 if n.d.o.f. is zero)'),
            expr = cms.string('?innerTrack().isNonnull()?innerTrack().normalizedChi2():-1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        innerTrackValidFraction = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('fraction of valid hits on the track'),
            expr = cms.string('?innerTrack().isNonnull()?innerTrack().validFraction():-1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        ip3d = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('3D impact parameter wrt first PV, in cm'),
            expr = cms.string("abs(dB(\'PV3D\'))"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        isGlobal = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon is global muon'),
            expr = cms.string('isGlobalMuon'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        isGood = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Tracker track matched with at least one muon segment (in any station) in both X and Y coordinates (< 3sigma) ( TMOneStationTight) and arbitrated'),
            expr = cms.string("isGood(\'TMOneStationTight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        isHighPurity = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('track quality flag for high purity'),
            expr = cms.string("?innerTrack().isNonnull()? innerTrack().quality(\'highPurity\'):-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        isPFcand = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon is PF candidate'),
            expr = cms.string('isPFMuon'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        isTracker = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon is tracker muon'),
            expr = cms.string('isTrackerMuon'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        jetIdx = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('index of the associated jet (-1 if none)'),
            expr = cms.string("?hasUserCand(\'jet\')?userCand(\'jet\').key():-1"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        jetPtRelv2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Relative momentum of the lepton with respect to the closest jet after subtracting the lepton'),
            expr = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'ptRel\'):0"),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            type = cms.string('float')
        ),
        jetRelIso = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Relative isolation in matched jet (1/ptRatio-1, pfRelIso04_all if no matched jet)'),
            expr = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?(1./userFloat(\'ptRatio\'))-1.:(pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - pfIsolationR04().sumPUPt/2,0.0))/pt"),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            type = cms.string('float')
        ),
        looseId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon is loose muon'),
            expr = cms.string("passed(\'CutBasedIdLoose\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mass'),
            expr = cms.string('mass'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        mediumId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('cut-based ID, medium WP'),
            expr = cms.string("passed(\'CutBasedIdMedium\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        mediumPromptId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('cut-based ID, medium prompt WP'),
            expr = cms.string("passed(\'CutBasedIdMediumPrompt\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        miniIsoId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('MiniIso ID from miniAOD selector (1=MiniIsoLoose, 2=MiniIsoMedium, 3=MiniIsoTight, 4=MiniIsoVeryTight)'),
            expr = cms.string("passed(\'MiniIsoLoose\')+passed(\'MiniIsoMedium\')+passed(\'MiniIsoTight\')+passed(\'MiniIsoVeryTight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('uint8')
        ),
        miniPFRelIso_all = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mini PF relative isolation, total (with scaled rho*EA PU corrections)'),
            expr = cms.string("userFloat(\'miniIsoAll\')/pt"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        miniPFRelIso_chg = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mini PF relative isolation, charged component'),
            expr = cms.string("userFloat(\'miniIsoChg\')/pt"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        multiIsoId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('MultiIsoId from miniAOD selector (1=MultiIsoLoose, 2=MultiIsoMedium)'),
            expr = cms.string("?passed(\'MultiIsoMedium\')?2:passed(\'MultiIsoLoose\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('uint8')
        ),
        mvaId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Mva ID from miniAOD selector (1=MvaLoose, 2=MvaMedium, 3=MvaTight)'),
            expr = cms.string("passed(\'MvaLoose\')+passed(\'MvaMedium\')+passed(\'MvaTight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('uint8')
        ),
        nPixelLayers = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Number of pixel layers'),
            expr = cms.string('?innerTrack().isNonnull()? innerTrack().hitPattern().pixelLayersWithMeasurement():-1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        nStations = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('number of matched stations with default arbitration (segment & track)'),
            expr = cms.string('numberOfMatchedStations'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        nTrackerLayersWithMeasurement = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('number of tracker layers with hits'),
            expr = cms.string('?innerTrack().isNonnull()? innerTrack().hitPattern().trackerLayersWithMeasurement():-1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        outerTrackCharge = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('charge of the outer track, else 0'),
            expr = cms.string('?outerTrack().isNonnull()? outerTrack().charge():0'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        outerTrackNonNull = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon contans an outer track'),
            expr = cms.string('outerTrack().isNonnull()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        outerTrackNormalizedChi2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('outer track chi-squared divided by n.d.o.f. (or chi-squared * 1e6 if n.d.o.f. is zero)'),
            expr = cms.string('?outerTrack().isNonnull()? outerTrack().normalizedChi2():-1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        pdgId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('PDG code assigned by the event reconstruction (not by MC truth)'),
            expr = cms.string('pdgId'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        pfIsoId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('PFIso ID from miniAOD selector (1=PFIsoVeryLoose, 2=PFIsoLoose, 3=PFIsoMedium, 4=PFIsoTight, 5=PFIsoVeryTight, 6=PFIsoVeryVeryTight)'),
            expr = cms.string("passed(\'PFIsoVeryLoose\')+passed(\'PFIsoLoose\')+passed(\'PFIsoMedium\')+passed(\'PFIsoTight\')+passed(\'PFIsoVeryTight\')+passed(\'PFIsoVeryVeryTight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('uint8')
        ),
        pfRelIso03_all = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('PF relative isolation dR=0.3, total (deltaBeta corrections)'),
            expr = cms.string('(pfIsolationR03().sumChargedHadronPt + max(pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt - pfIsolationR03().sumPUPt/2,0.0))/pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        pfRelIso03_chg = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('PF relative isolation dR=0.3, charged component'),
            expr = cms.string('pfIsolationR03().sumChargedHadronPt/pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        pfRelIso04_all = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('PF relative isolation dR=0.4, total (deltaBeta corrections)'),
            expr = cms.string('(pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - pfIsolationR04().sumPUPt/2,0.0))/pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        ptErr = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('ptError of the muon track'),
            expr = cms.string('bestTrack().ptError()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        puppiIsoId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('PuppiIsoId from miniAOD selector (1=Loose, 2=Medium, 3=Tight)'),
            expr = cms.string("passed(\'PuppiIsoLoose\')+passed(\'PuppiIsoMedium\')+passed(\'PuppiIsoTight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('uint8')
        ),
        segmentComp = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('muon segment compatibility'),
            expr = cms.string('segmentCompatibility()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(14),
            type = cms.string('float')
        ),
        segmentCompatibility = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('segment compatibility for a track with matched muon info'),
            expr = cms.string('segmentCompatibility()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        sip3d = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('3D impact parameter significance wrt first PV'),
            expr = cms.string("abs(dB(\'PV3D\')/edB(\'PV3D\'))"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        softId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('soft cut-based ID'),
            expr = cms.string("passed(\'SoftCutBasedId\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        softMva = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('soft MVA ID score'),
            expr = cms.string('softMvaValue()'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        softMvaId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('soft MVA ID'),
            expr = cms.string("passed(\'SoftMvaId\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        tightCharge = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Tight charge criterion using pterr/pt of muonBestTrack (0:fail, 2:pass)'),
            expr = cms.string('?(muonBestTrack().ptError()/muonBestTrack().pt() < 0.2)?2:0'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('int')
        ),
        tightId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('cut-based ID, tight WP'),
            expr = cms.string("passed(\'CutBasedIdTight\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        timeAtIpInOutErr = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('time of arrival at the IP for the Beta=1 hypothesis, particle is moving from inside out'),
            expr = cms.string('time().timeAtIpInOutErr'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        tkIsoId = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('TkIso ID (1=TkIsoLoose, 2=TkIsoTight)'),
            expr = cms.string("?passed(\'TkIsoTight\')?2:passed(\'TkIsoLoose\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('uint8')
        ),
        tkRelIso = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Tracker-based relative isolation dR=0.3 for highPt, trkIso/tunePpt'),
            expr = cms.string('isolationR03().sumPt/tunePMuonBestTrack().pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        triggerIdLoose = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('TriggerIdLoose ID'),
            expr = cms.string("passed(\'TriggerIdLoose\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('bool')
        ),
        trkKink = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('chi2 value for the inner track stub with respect to the global track'),
            expr = cms.string('combinedQuality().trkKink'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        trkRelChi2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('chi2 value for the inner track stub with respect to the global track'),
            expr = cms.string('combinedQuality().trkRelChi2'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            type = cms.string('float')
        ),
        tunepRelPt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('TuneP relative pt, tunePpt/pt'),
            expr = cms.string('tunePMuonBestTrack().pt/pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        )
    )
)


process.muonsMCMatchForTable = cms.EDProducer("MCMatcherByPt",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(0.2),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(13, 11, 211, 321, 2212),
    mcStatus = cms.vint32(1, 2, 3),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("linkedObjects","muons")
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    fullChainPhysPartons = cms.bool(True),
    particles = cms.InputTag("prunedGenParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.ptRatioRelForMu = cms.EDProducer("MuonJetVarProducer",
    srcJet = cms.InputTag("updatedJets"),
    srcLep = cms.InputTag("slimmedMuons"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.qgtagger = cms.EDProducer("QGTagger",
    jetsLabel = cms.string('QGL_AK4PFchs'),
    srcJets = cms.InputTag("updatedJets"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcVertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useQualityCuts = cms.bool(False)
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.saJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('jets clustered from charged candidates compatible with primary vertex (charge()!=0 && pvAssociationQuality()>=5 && vertexRef().key()==0)'),
    extension = cms.bool(False),
    maxLen = cms.uint32(6),
    name = cms.string('SoftActivityJet'),
    singleton = cms.bool(False),
    src = cms.InputTag("softActivityJets"),
    variables = cms.PSet(
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(8),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        )
    )
)


process.saTable = cms.EDProducer("GlobalVariablesTableProducer",
    variables = cms.PSet(
        SoftActivityJetHT = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('scalar sum of soft activity jet pt, pt>1'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            src = cms.InputTag("softActivityJets"),
            type = cms.string('candidatescalarsum')
        ),
        SoftActivityJetHT10 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('scalar sum of soft activity jet pt , pt >10'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            src = cms.InputTag("softActivityJets10"),
            type = cms.string('candidatescalarsum')
        ),
        SoftActivityJetHT2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('scalar sum of soft activity jet pt, pt >2'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            src = cms.InputTag("softActivityJets2"),
            type = cms.string('candidatescalarsum')
        ),
        SoftActivityJetHT5 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('scalar sum of soft activity jet pt, pt>5'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            src = cms.InputTag("softActivityJets5"),
            type = cms.string('candidatescalarsum')
        ),
        SoftActivityJetNjets10 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('number of soft activity jet pt, pt >2'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            src = cms.InputTag("softActivityJets10"),
            type = cms.string('candidatesize')
        ),
        SoftActivityJetNjets2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('number of soft activity jet pt, pt >10'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            src = cms.InputTag("softActivityJets2"),
            type = cms.string('candidatesize')
        ),
        SoftActivityJetNjets5 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('number of soft activity jet pt, pt >5'),
            mcOnly = cms.bool(False),
            precision = cms.int32(-1),
            src = cms.InputTag("softActivityJets5"),
            type = cms.string('candidatesize')
        )
    )
)


process.slimmedMuonsUpdated = cms.EDProducer("PATMuonUpdater",
    computeMiniIso = cms.bool(False),
    miniIsoParams = cms.vdouble(
        0.05, 0.2, 10.0, 0.5, 0.0001, 
        0.01, 0.01, 0.01, 0.0
    ),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    recomputeMuonBasicSelectors = cms.bool(False),
    src = cms.InputTag("slimmedMuons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.slimmedMuonsWithUserData = cms.EDProducer("PATMuonUserDataEmbedder",
    src = cms.InputTag("slimmedMuons"),
    userCands = cms.PSet(
        jetForLepJetVar = cms.InputTag("ptRatioRelForMu","jetForLepJetVar")
    ),
    userFloats = cms.PSet(
        jetNDauChargedMVASel = cms.InputTag("ptRatioRelForMu","jetNDauChargedMVASel"),
        miniIsoAll = cms.InputTag("isoForMu","miniIsoAll"),
        miniIsoChg = cms.InputTag("isoForMu","miniIsoChg"),
        ptRatio = cms.InputTag("ptRatioRelForMu","ptRatio"),
        ptRel = cms.InputTag("ptRatioRelForMu","ptRel")
    )
)


process.softActivityJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("chsForSATkJets"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.subJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    cut = cms.string(''),
    doc = cms.string('slimmedJetsAK8, i.e. ak8 fat jets for boosted analysis'),
    extension = cms.bool(False),
    name = cms.string('SubJet'),
    singleton = cms.bool(False),
    src = cms.InputTag("slimmedJetsAK8PFPuppiSoftDropPacked","SubJets"),
    variables = cms.PSet(
        btagCMVA = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('CMVA V2 btag discriminator'),
            expr = cms.string("bDiscriminator(\'pfCombinedMVAV2BJetTags\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagCSVV2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string(' pfCombinedInclusiveSecondaryVertexV2 b-tag discriminator (aka CSVV2)'),
            expr = cms.string("bDiscriminator(\'pfCombinedInclusiveSecondaryVertexV2BJetTags\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        btagDeepB = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('DeepCSV b+bb tag discriminator'),
            expr = cms.string("bDiscriminator(\'pfDeepCSVJetTags:probb\')+bDiscriminator(\'pfDeepCSVJetTags:probbb\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        eta = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('eta'),
            expr = cms.string('eta'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        mass = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('mass'),
            expr = cms.string('mass'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        n2b1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('N2 with beta=1'),
            expr = cms.string("userFloat(\'nb1AK8PuppiSoftDropSubjets:ecfN2\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        n3b1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('N3 with beta=1'),
            expr = cms.string("userFloat(\'nb1AK8PuppiSoftDropSubjets:ecfN3\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        phi = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('phi'),
            expr = cms.string('phi'),
            mcOnly = cms.bool(False),
            precision = cms.int32(12),
            type = cms.string('float')
        ),
        pt = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('pt'),
            expr = cms.string('pt'),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        rawFactor = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('1 - Factor to get back to raw pT'),
            expr = cms.string("1.-jecFactor(\'Uncorrected\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(6),
            type = cms.string('float')
        ),
        tau1 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (1 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Subjets:tau1\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        tau2 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (2 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Subjets:tau2\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        tau3 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (3 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Subjets:tau3\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        ),
        tau4 = cms.PSet(
            compression = cms.string('none'),
            doc = cms.string('Nsubjettiness (4 axis)'),
            expr = cms.string("userFloat(\'NjettinessAK8Subjets:tau4\')"),
            mcOnly = cms.bool(False),
            precision = cms.int32(10),
            type = cms.string('float')
        )
    )
)


process.tightJetId = cms.EDProducer("PatJetIDValueMapProducer",
    filterParams = cms.PSet(
        quality = cms.string('TIGHT'),
        version = cms.string('SUMMER18')
    ),
    src = cms.InputTag("updatedJets")
)


process.tightJetIdAK8 = cms.EDProducer("PatJetIDValueMapProducer",
    filterParams = cms.PSet(
        quality = cms.string('TIGHT'),
        version = cms.string('SUMMER18PUPPI')
    ),
    src = cms.InputTag("updatedJetsAK8")
)


process.tightJetIdLepVeto = cms.EDProducer("PatJetIDValueMapProducer",
    filterParams = cms.PSet(
        quality = cms.string('TIGHTLEPVETO'),
        version = cms.string('SUMMER18')
    ),
    src = cms.InputTag("updatedJets")
)


process.tightJetIdLepVetoAK8 = cms.EDProducer("PatJetIDValueMapProducer",
    filterParams = cms.PSet(
        quality = cms.string('TIGHTLEPVETO'),
        version = cms.string('SUMMER18PUPPI')
    ),
    src = cms.InputTag("updatedJetsAK8")
)


process.updatedJets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("jetCorrFactorsNano")),
    jetSource = cms.InputTag("slimmedJets"),
    printWarning = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedJetsAK8 = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("jetCorrFactorsAK8")),
    jetSource = cms.InputTag("slimmedJetsAK8"),
    printWarning = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedJetsAK8WithUserData = cms.EDProducer("PATJetUserDataEmbedder",
    src = cms.InputTag("updatedJetsAK8"),
    userFloats = cms.PSet(

    ),
    userInts = cms.PSet(
        tightId = cms.InputTag("tightJetIdAK8"),
        tightIdLepVeto = cms.InputTag("tightJetIdLepVetoAK8")
    )
)


process.updatedJetsWithUserData = cms.EDProducer("PATJetUserDataEmbedder",
    src = cms.InputTag("updatedJets"),
    userFloats = cms.PSet(
        genPtwNu = cms.InputTag("bJetVars","genPtwNu"),
        jercCHF = cms.InputTag("jercVars","chargedHadronCHSEnergyFraction"),
        jercCHPUF = cms.InputTag("jercVars","chargedHadronPUEnergyFraction"),
        leadTrackPt = cms.InputTag("bJetVars","leadTrackPt"),
        leptonDeltaR = cms.InputTag("bJetVars","leptonDeltaR"),
        leptonPt = cms.InputTag("bJetVars","leptonPt"),
        leptonPtRatio = cms.InputTag("bJetVars","leptonPtRatio"),
        leptonPtRatiov0 = cms.InputTag("bJetVars","leptonPtRatiov0"),
        leptonPtRel = cms.InputTag("bJetVars","leptonPtRel"),
        leptonPtRelInv = cms.InputTag("bJetVars","leptonPtRelInv"),
        leptonPtRelInvv0 = cms.InputTag("bJetVars","leptonPtRelInvv0"),
        leptonPtRelv0 = cms.InputTag("bJetVars","leptonPtRelv0"),
        ptD = cms.InputTag("bJetVars","ptD"),
        qgl = cms.InputTag("qgtagger","qgLikelihood"),
        vtx3dL = cms.InputTag("bJetVars","vtx3dL"),
        vtx3deL = cms.InputTag("bJetVars","vtx3deL"),
        vtxMass = cms.InputTag("bJetVars","vtxMass"),
        vtxPt = cms.InputTag("bJetVars","vtxPt")
    ),
    userInts = cms.PSet(
        leptonPdgId = cms.InputTag("bJetVars","leptonPdgId"),
        tightId = cms.InputTag("tightJetId"),
        tightIdLepVeto = cms.InputTag("tightJetIdLepVeto"),
        vtxNtrk = cms.InputTag("bJetVars","vtxNtrk")
    )
)


process.updatedPatJets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("updatedPatJetCorrFactors")),
    jetSource = cms.InputTag("slimmedJets"),
    printWarning = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.chsForSATkJets = cms.EDFilter("CandPtrSelector",
    cut = cms.string('charge()!=0 && pvAssociationQuality()>=5 && vertexRef().key()==0'),
    src = cms.InputTag("packedPFCandidates")
)


process.finalJets = cms.EDFilter("PATJetRefSelector",
    cut = cms.string('pt > 15'),
    src = cms.InputTag("updatedJetsWithUserData")
)


process.finalJetsAK8 = cms.EDFilter("PATJetRefSelector",
    cut = cms.string('pt > 170'),
    src = cms.InputTag("updatedJetsAK8WithUserData")
)


process.finalLooseMuons = cms.EDFilter("PATMuonRefSelector",
    cut = cms.string('pt > 3 && track.isNonnull && isLooseMuon'),
    src = cms.InputTag("slimmedMuonsWithUserData")
)


process.finalMuons = cms.EDFilter("PATMuonRefSelector",
    cut = cms.string('pt>1 && pt<40'),
    src = cms.InputTag("slimmedMuonsWithUserData")
)


process.softActivityJets10 = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt>10'),
    src = cms.InputTag("softActivityJets")
)


process.softActivityJets2 = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt>2'),
    src = cms.InputTag("softActivityJets")
)


process.softActivityJets5 = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt>5'),
    src = cms.InputTag("softActivityJets")
)


process.out = cms.OutputModule("NanoAODOutputModule",
    fileName = cms.untracked.string('defaultout.root'),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep nanoaodFlatTable_*Table_*_*'
    )
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    saveByLumi = cms.untracked.bool(False),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(500000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('106X_mc2017_realistic_v7'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.jetMC = cms.Sequence(process.jetMCTable+process.genJetTable+process.patJetPartons+process.genJetFlavourTable+process.genJetAK8Table+process.genJetAK8FlavourAssociation+process.genJetAK8FlavourTable+process.genSubJetAK8Table)


process.muonMC = cms.Sequence(process.muonsMCMatchForTable+process.muonMCTable)


process.crossLinkSequence = cms.Sequence(process.linkedObjects)


process.jetSequence = cms.Sequence(process.jetCorrFactorsNano+process.updatedJets+process.tightJetId+process.tightJetIdLepVeto+process.bJetVars+process.jercVars+process.qgtagger+process.updatedJetsWithUserData+process.finalJets)


process.genParticleTables = cms.Sequence(process.genParticleTable)


process.muonSequence = cms.Sequence(process.isoForMu+process.ptRatioRelForMu+process.slimmedMuonsWithUserData+process.finalMuons+process.finalLooseMuons)


process.genParticleSequence = cms.Sequence(process.finalGenParticles)


process.muonTables = cms.Sequence(process.muonMVATTH+process.muonMVALowPt+process.muonTable)


process.jetTables = cms.Sequence(process.bjetMVA+process.bjetNN+process.jetTable)


process.Path = cms.Path(process.genParticleTables+process.jetSequence+process.muonSequence+process.crossLinkSequence+process.jetTables+process.muonTables+process.muonMC)


process.end = cms.EndPath(process.out)


