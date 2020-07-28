#define dyclass_cxx
#include "dyclass.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void dyclass::Loop()
{
//   In a ROOT session, you can do:
//      root> .L dyclass.C
//      root> dyclass t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
  	//GenPart_pdgId[335]
	//Muon_genPartIdx[19]
	//Muon_looseId[19]
	for(int i=0; i< nMuon; i++){


		//Loose/////////////////////////////////
		int parentpdg = GenPart_pdgId[ Muon_genPartIdx[i]  ];
		if( Muon_looseId[i] && abs(parentpdg) == 13 ){
			numLoose->Fill(Muon_pt[i]);
		}
		if(abs(parentpdg) == 13){
			denLoose->Fill(Muon_pt[i]);
		}
	
		if( Muon_looseId[i] && abs(parentpdg) == 13 ){
			numLoosep->Fill(Muon_pt[i]);
			
		}
		if( Muon_looseId[i]){ 
			denLoosep->Fill(Muon_pt[i]);
		}
		//////////////////////////////////////

		//soft+Loose/////////////////////////////////
                //int parentpdg = GenPart_pdgId[ Muon_genPartIdx[i]  ];
                if( Muon_softId[i] && Muon_looseId[i] && abs(parentpdg) == 13 ){
                        numsofLoose->Fill(Muon_pt[i]);
                }
                if(abs(parentpdg) == 13){
                        densofLoose->Fill(Muon_pt[i]);
                }

                if( Muon_softId[i] && Muon_looseId[i] && abs(parentpdg) == 13 ){
                        numsofLoosep->Fill(Muon_pt[i]);

                }
                if( Muon_softId[i] && Muon_looseId[i]){
                        densofLoosep->Fill(Muon_pt[i]);
                }
                //////////////////////////////////////


		 //Med/////////////////////////////////
               // int parentpdg = GenPart_pdgId[ Muon_genPartIdx[i]  ];
                if( Muon_mediumId[i] && abs(parentpdg) == 13 ){
                        numMed->Fill(Muon_pt[i]);
                }
                if(abs(parentpdg) == 13){
                        denMed->Fill(Muon_pt[i]);
                }

                if( Muon_mediumId[i] && abs(parentpdg) == 13 ){
                        numMedp->Fill(Muon_pt[i]);

                }
                if( Muon_mediumId[i]){
                        denMedp->Fill(Muon_pt[i]);
                }
                //////////////////////////////////////


		 //Med+ sip3d<4 + miniso<6/////////////////////////////////
               // int parentpdg = GenPart_pdgId[ Muon_genPartIdx[i]  ];
		double sip3d = Muon_sip3d[i];
		double miso = Muon_pt[i] * Muon_miniPFRelIso_all[i];
                if( Muon_mediumId[i] && sip3d<4 && miso<6 && abs(parentpdg) == 13 ){
                        numGold->Fill(Muon_pt[i]);
                }
                if(abs(parentpdg) == 13){
                        denGold->Fill(Muon_pt[i]);
                }

                if( Muon_mediumId[i] && sip3d<4 && miso<6 && abs(parentpdg) == 13 ){
                        numGoldp->Fill(Muon_pt[i]);

                }
                if( Muon_mediumId[i] && sip3d<4 && miso<6){
                        denGoldp->Fill(Muon_pt[i]);
                }
                //////////////////////////////////////




	}

	
    }





TFile* f = new TFile("bench.root","RECREATE");

//loose
f->WriteTObject(numLoose);
f->WriteTObject(denLoose);
TEfficiency* loose = new TEfficiency(*numLoose,*denLoose);
f->WriteTObject(loose);


f->WriteTObject(numLoosep);
f->WriteTObject(denLoosep);
TEfficiency* loosep = new TEfficiency(*numLoosep, *denLoosep);
f->WriteTObject(loosep);
//////


//soft+loose
f->WriteTObject(numsofLoose);
f->WriteTObject(densofLoose);
TEfficiency* sofloose = new TEfficiency(*numsofLoose,*densofLoose);
f->WriteTObject(sofloose);


f->WriteTObject(numsofLoosep);
f->WriteTObject(densofLoosep);
TEfficiency* sofloosep = new TEfficiency(*numsofLoosep, *densofLoosep);
f->WriteTObject(sofloosep);
//////


//medium
f->WriteTObject(numMed);
f->WriteTObject(denMed);
TEfficiency* medium = new TEfficiency(*numMed,*denMed);
f->WriteTObject(medium);


f->WriteTObject(numMedp);
f->WriteTObject(denMedp);
TEfficiency* mediump = new TEfficiency(*numMedp, *denMedp);
f->WriteTObject(mediump);
//////



//medium
f->WriteTObject(numGold);
f->WriteTObject(denGold);
TEfficiency* gold = new TEfficiency(*numGold,*denGold);
f->WriteTObject(gold);


f->WriteTObject(numGoldp);
f->WriteTObject(denGoldp);
TEfficiency* goldp = new TEfficiency(*numGoldp, *denGoldp);
f->WriteTObject(goldp);
//////



f->Write();
f->Close();

}
