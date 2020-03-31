//make signal (soft prompt muons - truth matched) and background (soft NP muons) trees
#include "TFile.h"
#include "TBranch.h"
#include "TTree.h"
#include "TLeaf.h"

void makeTrees(){
	TFile* fDyjets = TFile::Open("OutputFiles/DYJetsToLL2018_NANO.root");
	TTree* dyjets = (TTree*)fDyjets->Get("Events");
	fDyjets->Close();


	TFile *file = new TFile("TMVA_softLep.root","RECREATE");
	TTree* sig = new TTree("Events","Events");
	// TTree* bkg = new TTree("Events","Events");

	// int nEvts = dyjets->GetEntries();

	UInt_t nMuons;
	Float_t pt[6];
	// Float_t eta;
	// Float_t sipd3d;
	// Float_t dxy;
	// Float_t dz;
	// Float_t miniIsochg;
	// Float_t miniIsoall;
	// Float_t nStations;

	TBranch* b_pt = sig->Branch("Muon_pt",&pt);
	// TBranch* b_eta = sig->Branch("Muon_eta",&eta);
	// TBranch* b_sip3d = sig->Branch("Muon_sip3d",&sipd3d);
	// TBranch* b_dxy = sig->Branch("Muon_dxy",&dxy);
	// TBranch* b_dz = sig->Branch("Muon_dz",&dz);
	// TBranch* b_miniIsochg = sig->Branch("Muon_miniPFRelIso_chg",&miniIsochg);
	// TBranch* b_miniIsoall = sig->Branch("Muon_miniPFRelIso_all",&miniIsoall);
	// TBranch* b_nStations = sig->Branch("Muon_nStations",&nStations);


	for(int i = 0; i < 100; i++){
		dyjets->GetEntry(i);

		//loose definition - is PFCandidate and isGlobal or tracker muon
		// if(!dyjets->GetLeaf("Muon_isPFcand")) continue;
		// if(!dyjets->GetLeaf("Muon_isGlobal") || !dyjets->GetLeaf("Muon_isTracker")) continue;

		nMuons = dyjets->GetLeaf("nMuon")->GetValue();
		for(int mu = 0; mu < nMuons; mu++){
			pt[mu] = dyjets->GetLeaf("Muon_pt")->GetValue(mu);
		}
		
		// eta = dyjets->GetBranch("Muon_eta");
		// sipd3d = dyjets->GetBranch("Muon_sip3d");
		// dxy = dyjets->GetBranch("Muon_dxy");
		// dz = dyjets->GetBranch("");
		// miniIsochg;
		// miniIsoall;
		// nStations;

		//isprompt flag
		// if(dyjets->GetLeaf("GenPart_statusFlags")->GetValue() == 0){
			sig->Fill();
		// }
		// dyjets->GetLeaf(""); //0 = isPrompt, 1 = isDecayedLeptonHadron; 2 = isTauDecayProduct
		// dyjets->GetLeaf("");

		
	}
	file->Write();
	file->Close();

}




