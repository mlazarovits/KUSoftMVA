//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Jul 22 11:27:14 2020 by ROOT version 6.22/00
// from TTree Events/Events
// found on file: /home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_dyjets.root
//////////////////////////////////////////////////////////

#ifndef dyclass_h
#define dyclass_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class dyclass {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   UInt_t          run;
   UInt_t          luminosityBlock;
   ULong64_t       event;
   UInt_t          nGenPart;
   Float_t         GenPart_eta[335];   //[nGenPart]
   Float_t         GenPart_mass[335];   //[nGenPart]
   Float_t         GenPart_phi[335];   //[nGenPart]
   Float_t         GenPart_pt[335];   //[nGenPart]
   Int_t           GenPart_genPartIdxMother[335];   //[nGenPart]
   Int_t           GenPart_pdgId[335];   //[nGenPart]
   Int_t           GenPart_status[335];   //[nGenPart]
   Int_t           GenPart_statusFlags[335];   //[nGenPart]
   UInt_t          nJet;
   Float_t         Jet_area[29];   //[nJet]
   Float_t         Jet_btagCMVA[29];   //[nJet]
   Float_t         Jet_btagCSVV2[29];   //[nJet]
   Float_t         Jet_btagDeepB[29];   //[nJet]
   Float_t         Jet_btagDeepC[29];   //[nJet]
   Float_t         Jet_btagDeepFlavB[29];   //[nJet]
   Float_t         Jet_btagDeepFlavC[29];   //[nJet]
   Float_t         Jet_chEmEF[29];   //[nJet]
   Float_t         Jet_chHEF[29];   //[nJet]
   Float_t         Jet_eta[29];   //[nJet]
   Float_t         Jet_jercCHF[29];   //[nJet]
   Float_t         Jet_jercCHPUF[29];   //[nJet]
   Float_t         Jet_mass[29];   //[nJet]
   Float_t         Jet_muEF[29];   //[nJet]
   Float_t         Jet_neEmEF[29];   //[nJet]
   Float_t         Jet_neHEF[29];   //[nJet]
   Float_t         Jet_phi[29];   //[nJet]
   Float_t         Jet_pt[29];   //[nJet]
   Float_t         Jet_qgl[29];   //[nJet]
   Float_t         Jet_rawFactor[29];   //[nJet]
   Float_t         Jet_bRegCorr[29];   //[nJet]
   Float_t         Jet_bRegRes[29];   //[nJet]
   Int_t           Jet_electronIdx1[29];   //[nJet]
   Int_t           Jet_electronIdx2[29];   //[nJet]
   Int_t           Jet_jetId[29];   //[nJet]
   Int_t           Jet_muonIdx1[29];   //[nJet]
   Int_t           Jet_muonIdx2[29];   //[nJet]
   Int_t           Jet_nConstituents[29];   //[nJet]
   Int_t           Jet_nElectrons[29];   //[nJet]
   Int_t           Jet_nMuons[29];   //[nJet]
   Int_t           Jet_puId[29];   //[nJet]
   UInt_t          nMuon;
   Float_t         Muon_LepGood_jetDF[19];   //[nMuon]
   Float_t         Muon_LepGood_jetPtRatio[19];   //[nMuon]
   Float_t         Muon_LepGood_jetPtRelv2[19];   //[nMuon]
   Float_t         Muon_LepGood_miniRelIsoNeutral[19];   //[nMuon]
   Float_t         Muon_chi2LocalMomentum[19];   //[nMuon]
   Float_t         Muon_chi2LocalPosition[19];   //[nMuon]
   Float_t         Muon_dxy[19];   //[nMuon]
   Float_t         Muon_dxyErr[19];   //[nMuon]
   Float_t         Muon_dz[19];   //[nMuon]
   Float_t         Muon_dzErr[19];   //[nMuon]
   Float_t         Muon_eta[19];   //[nMuon]
   Float_t         Muon_glbKink[19];   //[nMuon]
   Float_t         Muon_glbTrackProbability[19];   //[nMuon]
   Float_t         Muon_innerTrackNormalizedChi2[19];   //[nMuon]
   Float_t         Muon_innerTrackValidFraction[19];   //[nMuon]
   Float_t         Muon_ip3d[19];   //[nMuon]
   Float_t         Muon_jetPtRelv2[19];   //[nMuon]
   Float_t         Muon_jetRelIso[19];   //[nMuon]
   Float_t         Muon_mass[19];   //[nMuon]
   Float_t         Muon_miniPFRelIso_all[19];   //[nMuon]
   Float_t         Muon_miniPFRelIso_chg[19];   //[nMuon]
   Float_t         Muon_outerTrackNormalizedChi2[19];   //[nMuon]
   Float_t         Muon_pfRelIso03_all[19];   //[nMuon]
   Float_t         Muon_pfRelIso03_chg[19];   //[nMuon]
   Float_t         Muon_pfRelIso04_all[19];   //[nMuon]
   Float_t         Muon_phi[19];   //[nMuon]
   Float_t         Muon_pt[19];   //[nMuon]
   Float_t         Muon_ptErr[19];   //[nMuon]
   Float_t         Muon_segmentComp[19];   //[nMuon]
   Float_t         Muon_segmentCompatibility[19];   //[nMuon]
   Float_t         Muon_sip3d[19];   //[nMuon]
   Float_t         Muon_softMva[19];   //[nMuon]
   Float_t         Muon_timeAtIpInOutErr[19];   //[nMuon]
   Float_t         Muon_tkRelIso[19];   //[nMuon]
   Float_t         Muon_trkKink[19];   //[nMuon]
   Float_t         Muon_trkRelChi2[19];   //[nMuon]
   Float_t         Muon_tunepRelPt[19];   //[nMuon]
   Float_t         Muon_mvaLowPt[19];   //[nMuon]
   Float_t         Muon_mvaTTH[19];   //[nMuon]
   Int_t           Muon_LepGood_jetNDauChargedMVASel[19];   //[nMuon]
   Int_t           Muon_charge[19];   //[nMuon]
   Int_t           Muon_innerTrackCharge[19];   //[nMuon]
   Int_t           Muon_jetIdx[19];   //[nMuon]
   Int_t           Muon_nPixelLayers[19];   //[nMuon]
   Int_t           Muon_nStations[19];   //[nMuon]
   Int_t           Muon_nTrackerLayersWithMeasurement[19];   //[nMuon]
   Int_t           Muon_outerTrackCharge[19];   //[nMuon]
   Int_t           Muon_pdgId[19];   //[nMuon]
   Int_t           Muon_tightCharge[19];   //[nMuon]
   Bool_t          Muon_globalTrackNonNull[19];   //[nMuon]
   UChar_t         Muon_highPtId[19];   //[nMuon]
   Bool_t          Muon_inTimeMuon[19];   //[nMuon]
   Bool_t          Muon_innerTrackNonNull[19];   //[nMuon]
   Bool_t          Muon_isGlobal[19];   //[nMuon]
   Bool_t          Muon_isGood[19];   //[nMuon]
   Bool_t          Muon_isHighPurity[19];   //[nMuon]
   Bool_t          Muon_isPFcand[19];   //[nMuon]
   Bool_t          Muon_isTracker[19];   //[nMuon]
   Bool_t          Muon_looseId[19];   //[nMuon]
   Bool_t          Muon_mediumId[19];   //[nMuon]
   Bool_t          Muon_mediumPromptId[19];   //[nMuon]
   UChar_t         Muon_miniIsoId[19];   //[nMuon]
   UChar_t         Muon_multiIsoId[19];   //[nMuon]
   UChar_t         Muon_mvaId[19];   //[nMuon]
   Bool_t          Muon_outerTrackNonNull[19];   //[nMuon]
   UChar_t         Muon_pfIsoId[19];   //[nMuon]
   UChar_t         Muon_puppiIsoId[19];   //[nMuon]
   Bool_t          Muon_softId[19];   //[nMuon]
   Bool_t          Muon_softMvaId[19];   //[nMuon]
   Bool_t          Muon_tightId[19];   //[nMuon]
   UChar_t         Muon_tkIsoId[19];   //[nMuon]
   Bool_t          Muon_triggerIdLoose[19];   //[nMuon]
   Int_t           Muon_genPartIdx[19];   //[nMuon]
   UChar_t         Muon_genPartFlav[19];   //[nMuon]

   // List of branches
   TBranch        *b_run;   //!
   TBranch        *b_luminosityBlock;   //!
   TBranch        *b_event;   //!
   TBranch        *b_nGenPart;   //!
   TBranch        *b_GenPart_eta;   //!
   TBranch        *b_GenPart_mass;   //!
   TBranch        *b_GenPart_phi;   //!
   TBranch        *b_GenPart_pt;   //!
   TBranch        *b_GenPart_genPartIdxMother;   //!
   TBranch        *b_GenPart_pdgId;   //!
   TBranch        *b_GenPart_status;   //!
   TBranch        *b_GenPart_statusFlags;   //!
   TBranch        *b_nJet;   //!
   TBranch        *b_Jet_area;   //!
   TBranch        *b_Jet_btagCMVA;   //!
   TBranch        *b_Jet_btagCSVV2;   //!
   TBranch        *b_Jet_btagDeepB;   //!
   TBranch        *b_Jet_btagDeepC;   //!
   TBranch        *b_Jet_btagDeepFlavB;   //!
   TBranch        *b_Jet_btagDeepFlavC;   //!
   TBranch        *b_Jet_chEmEF;   //!
   TBranch        *b_Jet_chHEF;   //!
   TBranch        *b_Jet_eta;   //!
   TBranch        *b_Jet_jercCHF;   //!
   TBranch        *b_Jet_jercCHPUF;   //!
   TBranch        *b_Jet_mass;   //!
   TBranch        *b_Jet_muEF;   //!
   TBranch        *b_Jet_neEmEF;   //!
   TBranch        *b_Jet_neHEF;   //!
   TBranch        *b_Jet_phi;   //!
   TBranch        *b_Jet_pt;   //!
   TBranch        *b_Jet_qgl;   //!
   TBranch        *b_Jet_rawFactor;   //!
   TBranch        *b_Jet_bRegCorr;   //!
   TBranch        *b_Jet_bRegRes;   //!
   TBranch        *b_Jet_electronIdx1;   //!
   TBranch        *b_Jet_electronIdx2;   //!
   TBranch        *b_Jet_jetId;   //!
   TBranch        *b_Jet_muonIdx1;   //!
   TBranch        *b_Jet_muonIdx2;   //!
   TBranch        *b_Jet_nConstituents;   //!
   TBranch        *b_Jet_nElectrons;   //!
   TBranch        *b_Jet_nMuons;   //!
   TBranch        *b_Jet_puId;   //!
   TBranch        *b_nMuon;   //!
   TBranch        *b_Muon_LepGood_jetDF;   //!
   TBranch        *b_Muon_LepGood_jetPtRatio;   //!
   TBranch        *b_Muon_LepGood_jetPtRelv2;   //!
   TBranch        *b_Muon_LepGood_miniRelIsoNeutral;   //!
   TBranch        *b_Muon_chi2LocalMomentum;   //!
   TBranch        *b_Muon_chi2LocalPosition;   //!
   TBranch        *b_Muon_dxy;   //!
   TBranch        *b_Muon_dxyErr;   //!
   TBranch        *b_Muon_dz;   //!
   TBranch        *b_Muon_dzErr;   //!
   TBranch        *b_Muon_eta;   //!
   TBranch        *b_Muon_glbKink;   //!
   TBranch        *b_Muon_glbTrackProbability;   //!
   TBranch        *b_Muon_innerTrackNormalizedChi2;   //!
   TBranch        *b_Muon_innerTrackValidFraction;   //!
   TBranch        *b_Muon_ip3d;   //!
   TBranch        *b_Muon_jetPtRelv2;   //!
   TBranch        *b_Muon_jetRelIso;   //!
   TBranch        *b_Muon_mass;   //!
   TBranch        *b_Muon_miniPFRelIso_all;   //!
   TBranch        *b_Muon_miniPFRelIso_chg;   //!
   TBranch        *b_Muon_outerTrackNormalizedChi2;   //!
   TBranch        *b_Muon_pfRelIso03_all;   //!
   TBranch        *b_Muon_pfRelIso03_chg;   //!
   TBranch        *b_Muon_pfRelIso04_all;   //!
   TBranch        *b_Muon_phi;   //!
   TBranch        *b_Muon_pt;   //!
   TBranch        *b_Muon_ptErr;   //!
   TBranch        *b_Muon_segmentComp;   //!
   TBranch        *b_Muon_segmentCompatibility;   //!
   TBranch        *b_Muon_sip3d;   //!
   TBranch        *b_Muon_softMva;   //!
   TBranch        *b_Muon_timeAtIpInOutErr;   //!
   TBranch        *b_Muon_tkRelIso;   //!
   TBranch        *b_Muon_trkKink;   //!
   TBranch        *b_Muon_trkRelChi2;   //!
   TBranch        *b_Muon_tunepRelPt;   //!
   TBranch        *b_Muon_mvaLowPt;   //!
   TBranch        *b_Muon_mvaTTH;   //!
   TBranch        *b_Muon_LepGood_jetNDauChargedMVASel;   //!
   TBranch        *b_Muon_charge;   //!
   TBranch        *b_Muon_innerTrackCharge;   //!
   TBranch        *b_Muon_jetIdx;   //!
   TBranch        *b_Muon_nPixelLayers;   //!
   TBranch        *b_Muon_nStations;   //!
   TBranch        *b_Muon_nTrackerLayersWithMeasurement;   //!
   TBranch        *b_Muon_outerTrackCharge;   //!
   TBranch        *b_Muon_pdgId;   //!
   TBranch        *b_Muon_tightCharge;   //!
   TBranch        *b_Muon_globalTrackNonNull;   //!
   TBranch        *b_Muon_highPtId;   //!
   TBranch        *b_Muon_inTimeMuon;   //!
   TBranch        *b_Muon_innerTrackNonNull;   //!
   TBranch        *b_Muon_isGlobal;   //!
   TBranch        *b_Muon_isGood;   //!
   TBranch        *b_Muon_isHighPurity;   //!
   TBranch        *b_Muon_isPFcand;   //!
   TBranch        *b_Muon_isTracker;   //!
   TBranch        *b_Muon_looseId;   //!
   TBranch        *b_Muon_mediumId;   //!
   TBranch        *b_Muon_mediumPromptId;   //!
   TBranch        *b_Muon_miniIsoId;   //!
   TBranch        *b_Muon_multiIsoId;   //!
   TBranch        *b_Muon_mvaId;   //!
   TBranch        *b_Muon_outerTrackNonNull;   //!
   TBranch        *b_Muon_pfIsoId;   //!
   TBranch        *b_Muon_puppiIsoId;   //!
   TBranch        *b_Muon_softId;   //!
   TBranch        *b_Muon_softMvaId;   //!
   TBranch        *b_Muon_tightId;   //!
   TBranch        *b_Muon_tkIsoId;   //!
   TBranch        *b_Muon_triggerIdLoose;   //!
   TBranch        *b_Muon_genPartIdx;   //!
   TBranch        *b_Muon_genPartFlav;   //!

   dyclass(TTree *tree=0);
   virtual ~dyclass();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);

   //soft, softmva, soft+loose, loose, medium, kugold, 
   TH1D* numLoose;
   TH1D* denLoose;
   TH1D* numLoosep;
   TH1D* denLoosep;
 
   TH1D* numsofLoose;
   TH1D* densofLoose;
   TH1D* numsofLoosep;
   TH1D* densofLoosep;

   TH1D* numMed;
   TH1D* denMed;
   TH1D* numMedp;
   TH1D* denMedp;

	//GOLD miniIso<6 sip3d<4   
   TH1D* numGold;
   TH1D* denGold;
   TH1D* numGoldp;
   TH1D* denGoldp;




};

#endif

#ifdef dyclass_cxx
dyclass::dyclass(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_dyjets.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/data/Test_dyjets.root");
      }
      f->GetObject("Events",tree);

   }
   Init(tree);
}

dyclass::~dyclass()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t dyclass::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t dyclass::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void dyclass::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("luminosityBlock", &luminosityBlock, &b_luminosityBlock);
   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("nGenPart", &nGenPart, &b_nGenPart);
   fChain->SetBranchAddress("GenPart_eta", GenPart_eta, &b_GenPart_eta);
   fChain->SetBranchAddress("GenPart_mass", GenPart_mass, &b_GenPart_mass);
   fChain->SetBranchAddress("GenPart_phi", GenPart_phi, &b_GenPart_phi);
   fChain->SetBranchAddress("GenPart_pt", GenPart_pt, &b_GenPart_pt);
   fChain->SetBranchAddress("GenPart_genPartIdxMother", GenPart_genPartIdxMother, &b_GenPart_genPartIdxMother);
   fChain->SetBranchAddress("GenPart_pdgId", GenPart_pdgId, &b_GenPart_pdgId);
   fChain->SetBranchAddress("GenPart_status", GenPart_status, &b_GenPart_status);
   fChain->SetBranchAddress("GenPart_statusFlags", GenPart_statusFlags, &b_GenPart_statusFlags);
   fChain->SetBranchAddress("nJet", &nJet, &b_nJet);
   fChain->SetBranchAddress("Jet_area", Jet_area, &b_Jet_area);
   fChain->SetBranchAddress("Jet_btagCMVA", Jet_btagCMVA, &b_Jet_btagCMVA);
   fChain->SetBranchAddress("Jet_btagCSVV2", Jet_btagCSVV2, &b_Jet_btagCSVV2);
   fChain->SetBranchAddress("Jet_btagDeepB", Jet_btagDeepB, &b_Jet_btagDeepB);
   fChain->SetBranchAddress("Jet_btagDeepC", Jet_btagDeepC, &b_Jet_btagDeepC);
   fChain->SetBranchAddress("Jet_btagDeepFlavB", Jet_btagDeepFlavB, &b_Jet_btagDeepFlavB);
   fChain->SetBranchAddress("Jet_btagDeepFlavC", Jet_btagDeepFlavC, &b_Jet_btagDeepFlavC);
   fChain->SetBranchAddress("Jet_chEmEF", Jet_chEmEF, &b_Jet_chEmEF);
   fChain->SetBranchAddress("Jet_chHEF", Jet_chHEF, &b_Jet_chHEF);
   fChain->SetBranchAddress("Jet_eta", Jet_eta, &b_Jet_eta);
   fChain->SetBranchAddress("Jet_jercCHF", Jet_jercCHF, &b_Jet_jercCHF);
   fChain->SetBranchAddress("Jet_jercCHPUF", Jet_jercCHPUF, &b_Jet_jercCHPUF);
   fChain->SetBranchAddress("Jet_mass", Jet_mass, &b_Jet_mass);
   fChain->SetBranchAddress("Jet_muEF", Jet_muEF, &b_Jet_muEF);
   fChain->SetBranchAddress("Jet_neEmEF", Jet_neEmEF, &b_Jet_neEmEF);
   fChain->SetBranchAddress("Jet_neHEF", Jet_neHEF, &b_Jet_neHEF);
   fChain->SetBranchAddress("Jet_phi", Jet_phi, &b_Jet_phi);
   fChain->SetBranchAddress("Jet_pt", Jet_pt, &b_Jet_pt);
   fChain->SetBranchAddress("Jet_qgl", Jet_qgl, &b_Jet_qgl);
   fChain->SetBranchAddress("Jet_rawFactor", Jet_rawFactor, &b_Jet_rawFactor);
   fChain->SetBranchAddress("Jet_bRegCorr", Jet_bRegCorr, &b_Jet_bRegCorr);
   fChain->SetBranchAddress("Jet_bRegRes", Jet_bRegRes, &b_Jet_bRegRes);
   fChain->SetBranchAddress("Jet_electronIdx1", Jet_electronIdx1, &b_Jet_electronIdx1);
   fChain->SetBranchAddress("Jet_electronIdx2", Jet_electronIdx2, &b_Jet_electronIdx2);
   fChain->SetBranchAddress("Jet_jetId", Jet_jetId, &b_Jet_jetId);
   fChain->SetBranchAddress("Jet_muonIdx1", Jet_muonIdx1, &b_Jet_muonIdx1);
   fChain->SetBranchAddress("Jet_muonIdx2", Jet_muonIdx2, &b_Jet_muonIdx2);
   fChain->SetBranchAddress("Jet_nConstituents", Jet_nConstituents, &b_Jet_nConstituents);
   fChain->SetBranchAddress("Jet_nElectrons", Jet_nElectrons, &b_Jet_nElectrons);
   fChain->SetBranchAddress("Jet_nMuons", Jet_nMuons, &b_Jet_nMuons);
   fChain->SetBranchAddress("Jet_puId", Jet_puId, &b_Jet_puId);
   fChain->SetBranchAddress("nMuon", &nMuon, &b_nMuon);
   fChain->SetBranchAddress("Muon_LepGood_jetDF", Muon_LepGood_jetDF, &b_Muon_LepGood_jetDF);
   fChain->SetBranchAddress("Muon_LepGood_jetPtRatio", Muon_LepGood_jetPtRatio, &b_Muon_LepGood_jetPtRatio);
   fChain->SetBranchAddress("Muon_LepGood_jetPtRelv2", Muon_LepGood_jetPtRelv2, &b_Muon_LepGood_jetPtRelv2);
   fChain->SetBranchAddress("Muon_LepGood_miniRelIsoNeutral", Muon_LepGood_miniRelIsoNeutral, &b_Muon_LepGood_miniRelIsoNeutral);
   fChain->SetBranchAddress("Muon_chi2LocalMomentum", Muon_chi2LocalMomentum, &b_Muon_chi2LocalMomentum);
   fChain->SetBranchAddress("Muon_chi2LocalPosition", Muon_chi2LocalPosition, &b_Muon_chi2LocalPosition);
   fChain->SetBranchAddress("Muon_dxy", Muon_dxy, &b_Muon_dxy);
   fChain->SetBranchAddress("Muon_dxyErr", Muon_dxyErr, &b_Muon_dxyErr);
   fChain->SetBranchAddress("Muon_dz", Muon_dz, &b_Muon_dz);
   fChain->SetBranchAddress("Muon_dzErr", Muon_dzErr, &b_Muon_dzErr);
   fChain->SetBranchAddress("Muon_eta", Muon_eta, &b_Muon_eta);
   fChain->SetBranchAddress("Muon_glbKink", Muon_glbKink, &b_Muon_glbKink);
   fChain->SetBranchAddress("Muon_glbTrackProbability", Muon_glbTrackProbability, &b_Muon_glbTrackProbability);
   fChain->SetBranchAddress("Muon_innerTrackNormalizedChi2", Muon_innerTrackNormalizedChi2, &b_Muon_innerTrackNormalizedChi2);
   fChain->SetBranchAddress("Muon_innerTrackValidFraction", Muon_innerTrackValidFraction, &b_Muon_innerTrackValidFraction);
   fChain->SetBranchAddress("Muon_ip3d", Muon_ip3d, &b_Muon_ip3d);
   fChain->SetBranchAddress("Muon_jetPtRelv2", Muon_jetPtRelv2, &b_Muon_jetPtRelv2);
   fChain->SetBranchAddress("Muon_jetRelIso", Muon_jetRelIso, &b_Muon_jetRelIso);
   fChain->SetBranchAddress("Muon_mass", Muon_mass, &b_Muon_mass);
   fChain->SetBranchAddress("Muon_miniPFRelIso_all", Muon_miniPFRelIso_all, &b_Muon_miniPFRelIso_all);
   fChain->SetBranchAddress("Muon_miniPFRelIso_chg", Muon_miniPFRelIso_chg, &b_Muon_miniPFRelIso_chg);
   fChain->SetBranchAddress("Muon_outerTrackNormalizedChi2", Muon_outerTrackNormalizedChi2, &b_Muon_outerTrackNormalizedChi2);
   fChain->SetBranchAddress("Muon_pfRelIso03_all", Muon_pfRelIso03_all, &b_Muon_pfRelIso03_all);
   fChain->SetBranchAddress("Muon_pfRelIso03_chg", Muon_pfRelIso03_chg, &b_Muon_pfRelIso03_chg);
   fChain->SetBranchAddress("Muon_pfRelIso04_all", Muon_pfRelIso04_all, &b_Muon_pfRelIso04_all);
   fChain->SetBranchAddress("Muon_phi", Muon_phi, &b_Muon_phi);
   fChain->SetBranchAddress("Muon_pt", Muon_pt, &b_Muon_pt);
   fChain->SetBranchAddress("Muon_ptErr", Muon_ptErr, &b_Muon_ptErr);
   fChain->SetBranchAddress("Muon_segmentComp", Muon_segmentComp, &b_Muon_segmentComp);
   fChain->SetBranchAddress("Muon_segmentCompatibility", Muon_segmentCompatibility, &b_Muon_segmentCompatibility);
   fChain->SetBranchAddress("Muon_sip3d", Muon_sip3d, &b_Muon_sip3d);
   fChain->SetBranchAddress("Muon_softMva", Muon_softMva, &b_Muon_softMva);
   fChain->SetBranchAddress("Muon_timeAtIpInOutErr", Muon_timeAtIpInOutErr, &b_Muon_timeAtIpInOutErr);
   fChain->SetBranchAddress("Muon_tkRelIso", Muon_tkRelIso, &b_Muon_tkRelIso);
   fChain->SetBranchAddress("Muon_trkKink", Muon_trkKink, &b_Muon_trkKink);
   fChain->SetBranchAddress("Muon_trkRelChi2", Muon_trkRelChi2, &b_Muon_trkRelChi2);
   fChain->SetBranchAddress("Muon_tunepRelPt", Muon_tunepRelPt, &b_Muon_tunepRelPt);
   fChain->SetBranchAddress("Muon_mvaLowPt", Muon_mvaLowPt, &b_Muon_mvaLowPt);
   fChain->SetBranchAddress("Muon_mvaTTH", Muon_mvaTTH, &b_Muon_mvaTTH);
   fChain->SetBranchAddress("Muon_LepGood_jetNDauChargedMVASel", Muon_LepGood_jetNDauChargedMVASel, &b_Muon_LepGood_jetNDauChargedMVASel);
   fChain->SetBranchAddress("Muon_charge", Muon_charge, &b_Muon_charge);
   fChain->SetBranchAddress("Muon_innerTrackCharge", Muon_innerTrackCharge, &b_Muon_innerTrackCharge);
   fChain->SetBranchAddress("Muon_jetIdx", Muon_jetIdx, &b_Muon_jetIdx);
   fChain->SetBranchAddress("Muon_nPixelLayers", Muon_nPixelLayers, &b_Muon_nPixelLayers);
   fChain->SetBranchAddress("Muon_nStations", Muon_nStations, &b_Muon_nStations);
   fChain->SetBranchAddress("Muon_nTrackerLayersWithMeasurement", Muon_nTrackerLayersWithMeasurement, &b_Muon_nTrackerLayersWithMeasurement);
   fChain->SetBranchAddress("Muon_outerTrackCharge", Muon_outerTrackCharge, &b_Muon_outerTrackCharge);
   fChain->SetBranchAddress("Muon_pdgId", Muon_pdgId, &b_Muon_pdgId);
   fChain->SetBranchAddress("Muon_tightCharge", Muon_tightCharge, &b_Muon_tightCharge);
   fChain->SetBranchAddress("Muon_globalTrackNonNull", Muon_globalTrackNonNull, &b_Muon_globalTrackNonNull);
   fChain->SetBranchAddress("Muon_highPtId", Muon_highPtId, &b_Muon_highPtId);
   fChain->SetBranchAddress("Muon_inTimeMuon", Muon_inTimeMuon, &b_Muon_inTimeMuon);
   fChain->SetBranchAddress("Muon_innerTrackNonNull", Muon_innerTrackNonNull, &b_Muon_innerTrackNonNull);
   fChain->SetBranchAddress("Muon_isGlobal", Muon_isGlobal, &b_Muon_isGlobal);
   fChain->SetBranchAddress("Muon_isGood", Muon_isGood, &b_Muon_isGood);
   fChain->SetBranchAddress("Muon_isHighPurity", Muon_isHighPurity, &b_Muon_isHighPurity);
   fChain->SetBranchAddress("Muon_isPFcand", Muon_isPFcand, &b_Muon_isPFcand);
   fChain->SetBranchAddress("Muon_isTracker", Muon_isTracker, &b_Muon_isTracker);
   fChain->SetBranchAddress("Muon_looseId", Muon_looseId, &b_Muon_looseId);
   fChain->SetBranchAddress("Muon_mediumId", Muon_mediumId, &b_Muon_mediumId);
   fChain->SetBranchAddress("Muon_mediumPromptId", Muon_mediumPromptId, &b_Muon_mediumPromptId);
   fChain->SetBranchAddress("Muon_miniIsoId", Muon_miniIsoId, &b_Muon_miniIsoId);
   fChain->SetBranchAddress("Muon_multiIsoId", Muon_multiIsoId, &b_Muon_multiIsoId);
   fChain->SetBranchAddress("Muon_mvaId", Muon_mvaId, &b_Muon_mvaId);
   fChain->SetBranchAddress("Muon_outerTrackNonNull", Muon_outerTrackNonNull, &b_Muon_outerTrackNonNull);
   fChain->SetBranchAddress("Muon_pfIsoId", Muon_pfIsoId, &b_Muon_pfIsoId);
   fChain->SetBranchAddress("Muon_puppiIsoId", Muon_puppiIsoId, &b_Muon_puppiIsoId);
   fChain->SetBranchAddress("Muon_softId", Muon_softId, &b_Muon_softId);
   fChain->SetBranchAddress("Muon_softMvaId", Muon_softMvaId, &b_Muon_softMvaId);
   fChain->SetBranchAddress("Muon_tightId", Muon_tightId, &b_Muon_tightId);
   fChain->SetBranchAddress("Muon_tkIsoId", Muon_tkIsoId, &b_Muon_tkIsoId);
   fChain->SetBranchAddress("Muon_triggerIdLoose", Muon_triggerIdLoose, &b_Muon_triggerIdLoose);
   fChain->SetBranchAddress("Muon_genPartIdx", Muon_genPartIdx, &b_Muon_genPartIdx);
   fChain->SetBranchAddress("Muon_genPartFlav", Muon_genPartFlav, &b_Muon_genPartFlav);
 




   numLoose = new TH1D("nLoose","",40,0.5,41.5);
   denLoose = new TH1D("dLoose","",40,0.5,41.5);
   numLoosep = new TH1D("nLoosep","",40,0.5,41.5);
   denLoosep= new TH1D("dLoosep","",40,0.5,41.5);

   numsofLoose = new TH1D("nsofLoose","",40,0.5,41.5);
   densofLoose = new TH1D("dsofLoose","",40,0.5,41.5);
   numsofLoosep = new TH1D("nsofLoosep","",40,0.5,41.5);
   densofLoosep= new TH1D("dsofLoosep","",40,0.5,41.5);

   numMed = new TH1D("nMed","",40,0.5,41.5);
   denMed = new TH1D("dMed","",40,0.5,41.5);
   numMedp = new TH1D("nMedp","",40,0.5,41.5);
   denMedp= new TH1D("dMedp","",40,0.5,41.5);

   numGold = new TH1D("nGold","",40,0.5,41.5);
   denGold = new TH1D("dGold","",40,0.5,41.5);
   numGoldp = new TH1D("nGoldp","",40,0.5,41.5);
   denGoldp= new TH1D("dGoldp","",40,0.5,41.5);

   
  Notify();
}

Bool_t dyclass::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void dyclass::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t dyclass::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef dyclass_cxx
