//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun May  3 12:53:04 2020 by ROOT version 6.20/00
// from TTree Events/Events
// found on file: dy100k.root
//////////////////////////////////////////////////////////

#ifndef matchnew_h
#define matchnew_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>
#include <TTreeReaderArray.h>

// Headers needed by this particular selector


class matchnew : public TSelector {
public :
   TTreeReader     fReader;  //!the tree reader
   TTree          *fChain = 0;   //!pointer to the analyzed TTree or TChain

   // Readers to access the data (delete the ones you do not need).
   TTreeReaderValue<UInt_t> run = {fReader, "run"};
   TTreeReaderValue<UInt_t> luminosityBlock = {fReader, "luminosityBlock"};
   TTreeReaderValue<ULong64_t> event = {fReader, "event"};
   TTreeReaderValue<UInt_t> nGenPart = {fReader, "nGenPart"};
   TTreeReaderArray<Float_t> GenPart_eta = {fReader, "GenPart_eta"};
   TTreeReaderArray<Float_t> GenPart_mass = {fReader, "GenPart_mass"};
   TTreeReaderArray<Float_t> GenPart_phi = {fReader, "GenPart_phi"};
   TTreeReaderArray<Float_t> GenPart_pt = {fReader, "GenPart_pt"};
   TTreeReaderArray<Int_t> GenPart_genPartIdxMother = {fReader, "GenPart_genPartIdxMother"};
   TTreeReaderArray<Int_t> GenPart_pdgId = {fReader, "GenPart_pdgId"};
   TTreeReaderArray<Int_t> GenPart_status = {fReader, "GenPart_status"};
   TTreeReaderArray<Int_t> GenPart_statusFlags = {fReader, "GenPart_statusFlags"};
   TTreeReaderValue<UInt_t> nJet = {fReader, "nJet"};
   TTreeReaderArray<Float_t> Jet_area = {fReader, "Jet_area"};
   TTreeReaderArray<Float_t> Jet_btagCMVA = {fReader, "Jet_btagCMVA"};
   TTreeReaderArray<Float_t> Jet_btagCSVV2 = {fReader, "Jet_btagCSVV2"};
   TTreeReaderArray<Float_t> Jet_btagDeepB = {fReader, "Jet_btagDeepB"};
   TTreeReaderArray<Float_t> Jet_btagDeepC = {fReader, "Jet_btagDeepC"};
   TTreeReaderArray<Float_t> Jet_btagDeepFlavB = {fReader, "Jet_btagDeepFlavB"};
   TTreeReaderArray<Float_t> Jet_btagDeepFlavC = {fReader, "Jet_btagDeepFlavC"};
   TTreeReaderArray<Float_t> Jet_chEmEF = {fReader, "Jet_chEmEF"};
   TTreeReaderArray<Float_t> Jet_chHEF = {fReader, "Jet_chHEF"};
   TTreeReaderArray<Float_t> Jet_eta = {fReader, "Jet_eta"};
   TTreeReaderArray<Float_t> Jet_jercCHF = {fReader, "Jet_jercCHF"};
   TTreeReaderArray<Float_t> Jet_jercCHPUF = {fReader, "Jet_jercCHPUF"};
   TTreeReaderArray<Float_t> Jet_mass = {fReader, "Jet_mass"};
   TTreeReaderArray<Float_t> Jet_muEF = {fReader, "Jet_muEF"};
   TTreeReaderArray<Float_t> Jet_neEmEF = {fReader, "Jet_neEmEF"};
   TTreeReaderArray<Float_t> Jet_neHEF = {fReader, "Jet_neHEF"};
   TTreeReaderArray<Float_t> Jet_phi = {fReader, "Jet_phi"};
   TTreeReaderArray<Float_t> Jet_pt = {fReader, "Jet_pt"};
   TTreeReaderArray<Float_t> Jet_qgl = {fReader, "Jet_qgl"};
   TTreeReaderArray<Float_t> Jet_rawFactor = {fReader, "Jet_rawFactor"};
   TTreeReaderArray<Float_t> Jet_bRegCorr = {fReader, "Jet_bRegCorr"};
   TTreeReaderArray<Float_t> Jet_bRegRes = {fReader, "Jet_bRegRes"};
   TTreeReaderArray<Int_t> Jet_electronIdx1 = {fReader, "Jet_electronIdx1"};
   TTreeReaderArray<Int_t> Jet_electronIdx2 = {fReader, "Jet_electronIdx2"};
   TTreeReaderArray<Int_t> Jet_jetId = {fReader, "Jet_jetId"};
   TTreeReaderArray<Int_t> Jet_muonIdx1 = {fReader, "Jet_muonIdx1"};
   TTreeReaderArray<Int_t> Jet_muonIdx2 = {fReader, "Jet_muonIdx2"};
   TTreeReaderArray<Int_t> Jet_nConstituents = {fReader, "Jet_nConstituents"};
   TTreeReaderArray<Int_t> Jet_nElectrons = {fReader, "Jet_nElectrons"};
   TTreeReaderArray<Int_t> Jet_nMuons = {fReader, "Jet_nMuons"};
   TTreeReaderArray<Int_t> Jet_puId = {fReader, "Jet_puId"};
   TTreeReaderValue<UInt_t> nMuon = {fReader, "nMuon"};
   TTreeReaderArray<Float_t> Muon_LepGood_jetDF = {fReader, "Muon_LepGood_jetDF"};
   TTreeReaderArray<Float_t> Muon_LepGood_jetPtRatio = {fReader, "Muon_LepGood_jetPtRatio"};
   TTreeReaderArray<Float_t> Muon_LepGood_jetPtRelv2 = {fReader, "Muon_LepGood_jetPtRelv2"};
   TTreeReaderArray<Float_t> Muon_LepGood_miniRelIsoNeutral = {fReader, "Muon_LepGood_miniRelIsoNeutral"};
   TTreeReaderArray<Float_t> Muon_chi2LocalMomentum = {fReader, "Muon_chi2LocalMomentum"};
   TTreeReaderArray<Float_t> Muon_chi2LocalPosition = {fReader, "Muon_chi2LocalPosition"};
   TTreeReaderArray<Float_t> Muon_dxy = {fReader, "Muon_dxy"};
   TTreeReaderArray<Float_t> Muon_dxyErr = {fReader, "Muon_dxyErr"};
   TTreeReaderArray<Float_t> Muon_dz = {fReader, "Muon_dz"};
   TTreeReaderArray<Float_t> Muon_dzErr = {fReader, "Muon_dzErr"};
   TTreeReaderArray<Float_t> Muon_eta = {fReader, "Muon_eta"};
   TTreeReaderArray<Float_t> Muon_glbKink = {fReader, "Muon_glbKink"};
   TTreeReaderArray<Float_t> Muon_glbTrackProbability = {fReader, "Muon_glbTrackProbability"};
   TTreeReaderArray<Float_t> Muon_innerTrackNormalizedChi2 = {fReader, "Muon_innerTrackNormalizedChi2"};
   TTreeReaderArray<Float_t> Muon_innerTrackValidFraction = {fReader, "Muon_innerTrackValidFraction"};
   TTreeReaderArray<Float_t> Muon_ip3d = {fReader, "Muon_ip3d"};
   TTreeReaderArray<Float_t> Muon_jetPtRelv2 = {fReader, "Muon_jetPtRelv2"};
   TTreeReaderArray<Float_t> Muon_jetRelIso = {fReader, "Muon_jetRelIso"};
   TTreeReaderArray<Float_t> Muon_mass = {fReader, "Muon_mass"};
   TTreeReaderArray<Float_t> Muon_miniPFRelIso_all = {fReader, "Muon_miniPFRelIso_all"};
   TTreeReaderArray<Float_t> Muon_miniPFRelIso_chg = {fReader, "Muon_miniPFRelIso_chg"};
   TTreeReaderArray<Float_t> Muon_outerTrackNormalizedChi2 = {fReader, "Muon_outerTrackNormalizedChi2"};
   TTreeReaderArray<Float_t> Muon_pfRelIso03_all = {fReader, "Muon_pfRelIso03_all"};
   TTreeReaderArray<Float_t> Muon_pfRelIso03_chg = {fReader, "Muon_pfRelIso03_chg"};
   TTreeReaderArray<Float_t> Muon_pfRelIso04_all = {fReader, "Muon_pfRelIso04_all"};
   TTreeReaderArray<Float_t> Muon_phi = {fReader, "Muon_phi"};
   TTreeReaderArray<Float_t> Muon_pt = {fReader, "Muon_pt"};
   TTreeReaderArray<Float_t> Muon_ptErr = {fReader, "Muon_ptErr"};
   TTreeReaderArray<Float_t> Muon_segmentComp = {fReader, "Muon_segmentComp"};
   TTreeReaderArray<Float_t> Muon_segmentCompatibility = {fReader, "Muon_segmentCompatibility"};
   TTreeReaderArray<Float_t> Muon_sip3d = {fReader, "Muon_sip3d"};
   TTreeReaderArray<Float_t> Muon_softMva = {fReader, "Muon_softMva"};
   TTreeReaderArray<Float_t> Muon_timeAtIpInOutErr = {fReader, "Muon_timeAtIpInOutErr"};
   TTreeReaderArray<Float_t> Muon_tkRelIso = {fReader, "Muon_tkRelIso"};
   TTreeReaderArray<Float_t> Muon_trkKink = {fReader, "Muon_trkKink"};
   TTreeReaderArray<Float_t> Muon_trkRelChi2 = {fReader, "Muon_trkRelChi2"};
   TTreeReaderArray<Float_t> Muon_tunepRelPt = {fReader, "Muon_tunepRelPt"};
   TTreeReaderArray<Float_t> Muon_mvaLowPt = {fReader, "Muon_mvaLowPt"};
   TTreeReaderArray<Float_t> Muon_mvaTTH = {fReader, "Muon_mvaTTH"};
   TTreeReaderArray<Int_t> Muon_LepGood_jetNDauChargedMVASel = {fReader, "Muon_LepGood_jetNDauChargedMVASel"};
   TTreeReaderArray<Int_t> Muon_charge = {fReader, "Muon_charge"};
   TTreeReaderArray<Int_t> Muon_innerTrackCharge = {fReader, "Muon_innerTrackCharge"};
   TTreeReaderArray<Int_t> Muon_jetIdx = {fReader, "Muon_jetIdx"};
   TTreeReaderArray<Int_t> Muon_nPixelLayers = {fReader, "Muon_nPixelLayers"};
   TTreeReaderArray<Int_t> Muon_nStations = {fReader, "Muon_nStations"};
   TTreeReaderArray<Int_t> Muon_nTrackerLayersWithMeasurement = {fReader, "Muon_nTrackerLayersWithMeasurement"};
   TTreeReaderArray<Int_t> Muon_outerTrackCharge = {fReader, "Muon_outerTrackCharge"};
   TTreeReaderArray<Int_t> Muon_pdgId = {fReader, "Muon_pdgId"};
   TTreeReaderArray<Int_t> Muon_tightCharge = {fReader, "Muon_tightCharge"};
   TTreeReaderArray<Bool_t> Muon_globalTrackNonNull = {fReader, "Muon_globalTrackNonNull"};
   TTreeReaderArray<UChar_t> Muon_highPtId = {fReader, "Muon_highPtId"};
   TTreeReaderArray<Bool_t> Muon_inTimeMuon = {fReader, "Muon_inTimeMuon"};
   TTreeReaderArray<Bool_t> Muon_innerTrackNonNull = {fReader, "Muon_innerTrackNonNull"};
   TTreeReaderArray<Bool_t> Muon_isGlobal = {fReader, "Muon_isGlobal"};
   TTreeReaderArray<Bool_t> Muon_isGood = {fReader, "Muon_isGood"};
   TTreeReaderArray<Bool_t> Muon_isHighPurity = {fReader, "Muon_isHighPurity"};
   TTreeReaderArray<Bool_t> Muon_isPFcand = {fReader, "Muon_isPFcand"};
   TTreeReaderArray<Bool_t> Muon_isTracker = {fReader, "Muon_isTracker"};
   TTreeReaderArray<Bool_t> Muon_looseId = {fReader, "Muon_looseId"};
   TTreeReaderArray<Bool_t> Muon_mediumId = {fReader, "Muon_mediumId"};
   TTreeReaderArray<Bool_t> Muon_mediumPromptId = {fReader, "Muon_mediumPromptId"};
   TTreeReaderArray<UChar_t> Muon_miniIsoId = {fReader, "Muon_miniIsoId"};
   TTreeReaderArray<UChar_t> Muon_multiIsoId = {fReader, "Muon_multiIsoId"};
   TTreeReaderArray<UChar_t> Muon_mvaId = {fReader, "Muon_mvaId"};
   TTreeReaderArray<Bool_t> Muon_outerTrackNonNull = {fReader, "Muon_outerTrackNonNull"};
   TTreeReaderArray<UChar_t> Muon_pfIsoId = {fReader, "Muon_pfIsoId"};
   TTreeReaderArray<UChar_t> Muon_puppiIsoId = {fReader, "Muon_puppiIsoId"};
   TTreeReaderArray<Bool_t> Muon_softId = {fReader, "Muon_softId"};
   TTreeReaderArray<Bool_t> Muon_softMvaId = {fReader, "Muon_softMvaId"};
   TTreeReaderArray<Bool_t> Muon_tightId = {fReader, "Muon_tightId"};
   TTreeReaderArray<UChar_t> Muon_tkIsoId = {fReader, "Muon_tkIsoId"};
   TTreeReaderArray<Bool_t> Muon_triggerIdLoose = {fReader, "Muon_triggerIdLoose"};
   TTreeReaderArray<Int_t> Muon_genPartIdx = {fReader, "Muon_genPartIdx"};
   TTreeReaderArray<UChar_t> Muon_genPartFlav = {fReader, "Muon_genPartFlav"};


   matchnew(TTree * /*tree*/ =0) { }
   virtual ~matchnew() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();

   ClassDef(matchnew,0);
  TH1D rawmatchPt{"rawmatchPt","Matched p_{T}",41,-0.5,40.5};
  TH1D rawunmatchPt{"rawunmatchPt","Unmatched p_{T}", 41,-0.5,40.5};

  TH1D rawmatchfraction{"rawmatchfraction","",2,-0.5,1.5};
  
//////
  TH1D matchPt{"matchPt","Matched p_{T}",41,-0.5,40.5};
  TH1D unmatchPt{"unmatchPt","Unmatched p_{T}", 41,-0.5,40.5};

  TH1D matchfraction{"matchfraction","",2,-0.5,1.5};
//////
  //label enum: 0=mu 1=elec 2=pion 3=kaon 4=proton
  TH1D labelcomp{"labelcomp","Label Composition",6,-0.5,5.5};
// 1 = prompt muon (including gamma*->mu mu), 15 = muon from prompt tau, 5 = muon from b, 4 = muon from c, 3 = muon from light or unknown, 0 = unmatched*

//gf 0=unknown 1=prompt, 2=tau 3=light/unknown 4=c 5=b
  TH1D mugf{"mugf","Muon",5,1,6};
  TH1D egf{"egf","Electron",5,1,6};
  TH1D pigf{"pigf","Pion",5,1,6};
  TH1D kgf{"kgf","Kaon",5,1,6};
  TH1D pgf{"pgf","Proton",5,1,6};	
  TH1D denomgf{"denomgf","All",5,1,6};


//////
	//dr dists.
   TH1D drmu{"drmu","Muon",20,0.,0.03};
   TH1D dre{"dre","Electron",20,0.,0.03};
   TH1D drpi{"drpi","Pion",20,0.,0.03};
   TH1D drk{"drk","Kaon",20,0.,0.03};
   TH1D drp{"drp","Proton",20,0.,0.03};

   TH1D dptmu{"dptmu","Muon",20,0.,0.1};
   TH1D dpte{"dpte","Electron",20,0.,0.1};
   TH1D dptpi{"dptpi","Pion",20,0.,0.1};
   TH1D dptk{"dptk","Kaon",20,0.,0.1};
   TH1D dptp{"dptp","Proton",20,0.,0.1};

   
  
};

#endif

#ifdef matchnew_cxx
void matchnew::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the reader is initialized.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   fReader.SetTree(tree);
}

Bool_t matchnew::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}
double dR(float eta1, float phi1, float eta2, float phi2) {
    
    float p1 = phi1;
    float p2 = phi2;
    float e1 = eta1;
    float e2 = eta2;
    auto dp = std::abs(p1 - p2);
    if (dp > float(M_PI))
      dp -= float(2 * M_PI);
    return sqrt ((e1 - e2) * (e1 - e2) + dp * dp);
  }
// 1 = prompt muon (including gamma*->mu mu), 15 = muon from prompt tau, 5 = muon from b, 4 = muon from c, 3 = muon from light or unknown, 0 = unmatched*

//gf 0=unknown 1=prompt, 2=tau 3=light/unknown 4=c 5=b
double getflav(int genflav){
	if(genflav == 0) return 0;
	if(genflav == 1) return 1;
	if(genflav == 15) return 2;
	if(genflav == 3) return 3;
	if(genflav == 4) return 4;
	if(genflav == 5) return 5;
	return -1;
}

#endif // #ifdef matchnew_cxx
