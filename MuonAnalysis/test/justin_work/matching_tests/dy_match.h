//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Apr 29 14:23:18 2020 by ROOT version 6.20/00
// from TTree Events/Events
// found on file: ../../OutputFiles/DYJetsToLL2018_MINI_numEvent20000.root
//////////////////////////////////////////////////////////

#ifndef dy_match_h
#define dy_match_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>
#include <TTreeReaderArray.h>

// Headers needed by this particular selector


class dy_match : public TSelector {
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
   TTreeReaderValue<UInt_t> nMuon = {fReader, "nMuon"};
   TTreeReaderArray<Float_t> Muon_dxy = {fReader, "Muon_dxy"};
   TTreeReaderArray<Float_t> Muon_dxyErr = {fReader, "Muon_dxyErr"};
   TTreeReaderArray<Float_t> Muon_dz = {fReader, "Muon_dz"};
   TTreeReaderArray<Float_t> Muon_dzErr = {fReader, "Muon_dzErr"};
   TTreeReaderArray<Float_t> Muon_eta = {fReader, "Muon_eta"};
   TTreeReaderArray<Float_t> Muon_ip3d = {fReader, "Muon_ip3d"};
   TTreeReaderArray<Float_t> Muon_jetPtRelv2 = {fReader, "Muon_jetPtRelv2"};
   TTreeReaderArray<Float_t> Muon_jetRelIso = {fReader, "Muon_jetRelIso"};
   TTreeReaderArray<Float_t> Muon_mass = {fReader, "Muon_mass"};
   TTreeReaderArray<Float_t> Muon_miniPFRelIso_all = {fReader, "Muon_miniPFRelIso_all"};
   TTreeReaderArray<Float_t> Muon_miniPFRelIso_chg = {fReader, "Muon_miniPFRelIso_chg"};
   TTreeReaderArray<Float_t> Muon_pfRelIso03_all = {fReader, "Muon_pfRelIso03_all"};
   TTreeReaderArray<Float_t> Muon_pfRelIso03_chg = {fReader, "Muon_pfRelIso03_chg"};
   TTreeReaderArray<Float_t> Muon_pfRelIso04_all = {fReader, "Muon_pfRelIso04_all"};
   TTreeReaderArray<Float_t> Muon_phi = {fReader, "Muon_phi"};
   TTreeReaderArray<Float_t> Muon_pt = {fReader, "Muon_pt"};
   TTreeReaderArray<Float_t> Muon_ptErr = {fReader, "Muon_ptErr"};
   TTreeReaderArray<Float_t> Muon_segmentComp = {fReader, "Muon_segmentComp"};
   TTreeReaderArray<Float_t> Muon_sip3d = {fReader, "Muon_sip3d"};
   TTreeReaderArray<Float_t> Muon_softMva = {fReader, "Muon_softMva"};
   TTreeReaderArray<Float_t> Muon_tkRelIso = {fReader, "Muon_tkRelIso"};
   TTreeReaderArray<Float_t> Muon_tunepRelPt = {fReader, "Muon_tunepRelPt"};
   TTreeReaderArray<Int_t> Muon_charge = {fReader, "Muon_charge"};
   TTreeReaderArray<Int_t> Muon_jetIdx = {fReader, "Muon_jetIdx"};
   TTreeReaderArray<Int_t> Muon_nStations = {fReader, "Muon_nStations"};
   TTreeReaderArray<Int_t> Muon_nTrackerLayers = {fReader, "Muon_nTrackerLayers"};
   TTreeReaderArray<Int_t> Muon_pdgId = {fReader, "Muon_pdgId"};
   TTreeReaderArray<Int_t> Muon_tightCharge = {fReader, "Muon_tightCharge"};
   TTreeReaderArray<UChar_t> Muon_highPtId = {fReader, "Muon_highPtId"};
   TTreeReaderArray<Bool_t> Muon_inTimeMuon = {fReader, "Muon_inTimeMuon"};
   TTreeReaderArray<Bool_t> Muon_isGlobal = {fReader, "Muon_isGlobal"};
   TTreeReaderArray<Bool_t> Muon_isPFcand = {fReader, "Muon_isPFcand"};
   TTreeReaderArray<Bool_t> Muon_isTracker = {fReader, "Muon_isTracker"};
   TTreeReaderArray<Bool_t> Muon_looseId = {fReader, "Muon_looseId"};
   TTreeReaderArray<Bool_t> Muon_mediumId = {fReader, "Muon_mediumId"};
   TTreeReaderArray<Bool_t> Muon_mediumPromptId = {fReader, "Muon_mediumPromptId"};
   TTreeReaderArray<UChar_t> Muon_miniIsoId = {fReader, "Muon_miniIsoId"};
   TTreeReaderArray<UChar_t> Muon_multiIsoId = {fReader, "Muon_multiIsoId"};
   TTreeReaderArray<UChar_t> Muon_mvaId = {fReader, "Muon_mvaId"};
   TTreeReaderArray<UChar_t> Muon_pfIsoId = {fReader, "Muon_pfIsoId"};
   TTreeReaderArray<UChar_t> Muon_puppiIsoId = {fReader, "Muon_puppiIsoId"};
   TTreeReaderArray<Bool_t> Muon_softId = {fReader, "Muon_softId"};
   TTreeReaderArray<Bool_t> Muon_softMvaId = {fReader, "Muon_softMvaId"};
   TTreeReaderArray<Bool_t> Muon_tightId = {fReader, "Muon_tightId"};
   TTreeReaderArray<UChar_t> Muon_tkIsoId = {fReader, "Muon_tkIsoId"};
   TTreeReaderArray<Bool_t> Muon_triggerIdLoose = {fReader, "Muon_triggerIdLoose"};
   TTreeReaderArray<Int_t> Muon_genPartIdx = {fReader, "Muon_genPartIdx"};
   TTreeReaderArray<UChar_t> Muon_genPartFlav = {fReader, "Muon_genPartFlav"};


   dy_match(TTree * /*tree*/ =0) { }
   virtual ~dy_match() { }
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
   void getrelatives(int gen_idx);

   ClassDef(dy_match,0);

   TH2D matchpt{"matchpt","matchidx and pt;pt;idx", 41, -0.5, 40.5, 22, -1.5, 20.5};
   TH1D unmatchPt{"unmatchPt","pt dist of unmatched", 41,-0.5,40.5};
   TH1D mupt{"mupt", "pt of all muon",31,-0.5,40.5};
   TH1D matchpdg{"matchpdg","pdg of matches",501,-0.5,500.5};
   TH2D nonmuongenflav{"badgenflav","non muon genflav", 3,-0.5,2.5,16,-0.5,15.5};


   int globalctr_0=0;
   int globalctr_1=0;
};

#endif

#ifdef dy_match_cxx
void dy_match::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the reader is initialized.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   fReader.SetTree(tree);
}

Bool_t dy_match::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}
void dy_match::getrelatives( int gen_idx ){
	std::cout<<"This particle genmatch (pdg, idx): "<< GenPart_pdgId[gen_idx]<<" "<<gen_idx<<std::endl;
	std::cout<<"Parents (pdg,idx): "<<std::endl;
	int idx=GenPart_genPartIdxMother[gen_idx];
	int ctr=0;
	while( GenPart_genPartIdxMother[idx] != -1){
		std::cout<<ctr<<" "<<GenPart_pdgId[idx]<<" "<<idx<<std::endl;
		idx = GenPart_genPartIdxMother[idx];
		ctr++;
	}
	ctr = 0;
	std::cout<<"1st Gen Children (pdg, idx): "<<std::endl;
	for( int i=0; i<GenPart_genPartIdxMother.GetSize(); i++){
		if( gen_idx == GenPart_genPartIdxMother[i] ){
			std::cout<<ctr<<" "<<GenPart_pdgId[i]<<" "<<i<<std::endl;\
			ctr++;
		}
	}
	std::cout<<std::endl;

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

#endif // #ifdef dy_match_cxx
