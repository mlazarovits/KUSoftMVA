#define matchnew_cxx
// The class definition in matchnew.h has been generated automatically
// by the ROOT utility TTree::MakeSelector(). This class is derived
// from the ROOT class TSelector. For more information on the TSelector
// framework see $ROOTSYS/README/README.SELECTOR or the ROOT User Manual.


// The following methods are defined in this file:
//    Begin():        called every time a loop on the tree starts,
//                    a convenient place to create your histograms.
//    SlaveBegin():   called after Begin(), when on PROOF called only on the
//                    slave servers.
//    Process():      called for each event, in this function you decide what
//                    to read and fill your histograms.
//    SlaveTerminate: called at the end of the loop on the tree, when on PROOF
//                    called only on the slave servers.
//    Terminate():    called at the end of the loop on the tree,
//                    a convenient place to draw/fit your histograms.
//
// To use this file, try the following session on your Tree T:
//
// root> T->Process("matchnew.C")
// root> T->Process("matchnew.C","some options")
// root> T->Process("matchnew.C+")
//


#include "matchnew.h"
#include <TH2.h>
#include <TStyle.h>

void matchnew::Begin(TTree * /*tree*/)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();
}

void matchnew::SlaveBegin(TTree * /*tree*/)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

}

Bool_t matchnew::Process(Long64_t entry)
{
   // The Process() function is called for each entry in the tree (or possibly
   // keyed object in the case of PROOF) to be processed. The entry argument
   // specifies which entry in the currently loaded tree is to be processed.
   // When processing keyed objects with PROOF, the object is already loaded
   // and is available via the fObject pointer.
   //
   // This function should contain the \"body\" of the analysis. It can contain
   // simple or elaborate selection criteria, run algorithms on the data
   // of the event and typically fill histograms.
   //
   // The processing can be stopped by calling Abort().
   //
   // Use fStatus to set the return value of TTree::Process().
   //
   // The return value is currently not used.

   fReader.SetLocalEntry(entry);

   for(int i=0; i< *nMuon; i++){
	//pre cut plots
	//if unmatched
	if(Muon_genPartIdx[i] == -1){
		rawunmatchPt.Fill(Muon_pt[i]);
		rawmatchfraction.Fill(0);
	}
	//if matched
	if(Muon_genPartIdx[i] != -1){
		rawmatchPt.Fill(Muon_pt[i]);
		rawmatchfraction.Fill(1);
	}
	
	//post cut plots
	if( Muon_pt[i] > 2 ){
		//if unmatched
		if(Muon_genPartIdx[i] == -1){
			unmatchPt.Fill(Muon_pt[i]);
			matchfraction.Fill(0);
		}
		//if matched
		if(Muon_genPartIdx[i] != -1){
			matchPt.Fill(Muon_pt[i]);
			matchfraction.Fill(1);

			//label composition
			int idx = Muon_genPartIdx[i];
			int pdg = abs(GenPart_pdgId[ idx ]);
			double DR=dR(Muon_eta[i],Muon_phi[i], GenPart_eta[idx], GenPart_phi[idx]);
			double DPTREL=(GenPart_pt[idx] -Muon_pt[i])/(GenPart_pt[idx]);
			DPTREL = abs( DPTREL);
			
			int genflav=Muon_genPartFlav[i];			
			
			if( pdg == 11 ){//elec
				labelcomp.Fill(1);
				egf.Fill(getflav(genflav));
				dre.Fill(DR);
				dpte.Fill(DPTREL);
			}
			if( pdg == 13 ){//mu
				labelcomp.Fill(0);
				mugf.Fill(getflav(genflav));
				drmu.Fill(DR);
				dptmu.Fill(DPTREL);
			}
			if( pdg == 211){//pi
				labelcomp.Fill(2);
				pigf.Fill(getflav(genflav));
				drpi.Fill(DR);
				dptpi.Fill(DPTREL);
			}
			if( pdg == 321){//K
				labelcomp.Fill(3);
				kgf.Fill(getflav(genflav));
				drk.Fill(DR);
				dptk.Fill(DPTREL);
			}
			if( pdg == 2212){//p
				labelcomp.Fill(4);
				pgf.Fill(getflav(genflav));
				drp.Fill(DR);
				dptp.Fill(DPTREL);
			}
			//denom
			denomgf.Fill(getflav(genflav));
			//std::cout<<"( "<<pdg<<" "<<getflav(genflav)<<" )";
		

		}



	}




   }
   
	


   return kTRUE;
}

void matchnew::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.

}

void matchnew::Terminate()
{
   // The Terminate() function is the last function to be called during
   // a query. It always runs on the client, it can be used to present
   // the results graphically or save the results to file.
	//TFile* f = new TFile("dy.root", "RECREATE");
	//TFile* f = new TFile("tt.root", "RECREATE");
	TFile* f = new TFile("qcd.root","RECREATE");
	//do some formatting and normalization
	labelcomp.Scale(1./labelcomp.Integral());

	rawmatchfraction.Scale(1./rawmatchfraction.Integral());
	matchfraction.Scale(1./matchfraction.Integral());

	//int nx=5;
	const char *label[5] = {"Muon","Electron","Pion","Kaon","Proton"};
	for (int i=1;i<=5;i++) labelcomp.GetXaxis()->SetBinLabel(i,label[i-1]);


	//format genflavs
	mugf.SetFillColor(kRed);
	egf.SetFillColor(kGreen);
	kgf.SetFillColor(kViolet);
	pigf.SetFillColor(kOrange);
	pgf.SetFillColor(kBlue);
	
	mugf.Divide(&denomgf);
	egf.Divide(&denomgf);
	kgf.Divide(&denomgf);
	pigf.Divide(&denomgf);
	pgf.Divide(&denomgf);


	const char *flav[5] ={"Prompt","Tau","Light","Charm","B"};
	for (int i=1;i<=5;i++) mugf.GetXaxis()->SetBinLabel(i,flav[i-1]);

	auto flavstack = new THStack("flavstack","Gen. Flav by Label");
	flavstack->Add(&mugf);
	flavstack->Add(&egf);
	flavstack->Add(&pigf);
	flavstack->Add(&kgf);
	flavstack->Add(&pgf);
	f->WriteTObject(flavstack);


	drmu.SetLineColor(kRed);
	//drmu.SetFillColor(kRed);
	dre.SetLineColor(kGreen);
	drpi.SetLineColor(kOrange);
	drk.SetLineColor(kViolet);
	drp.SetLineColor(kBlue);

	drmu.Scale(1./drmu.Integral());
	dre.Scale(1./dre.Integral());
	drpi.Scale(1./drpi.Integral());
	drk.Scale(1./drk.Integral());
	drp.Scale(1./drp.Integral());
	
	dptmu.SetLineColor(kRed);
	dpte.SetLineColor(kGreen);
	dptpi.SetLineColor(kOrange);
	dptk.SetLineColor(kViolet);
	dptp.SetLineColor(kBlue);
	
	dptmu.Scale(1./dptmu.Integral());
	dpte.Scale(1./dpte.Integral());
	dptpi.Scale(1./dptpi.Integral());
	dptk.Scale(1./dptk.Integral());
	dptp.Scale(1./dptp.Integral());


	f->WriteTObject(&rawmatchPt);
	f->WriteTObject(&rawunmatchPt);
	f->WriteTObject(&rawmatchfraction);

	f->WriteTObject(&matchPt);
	f->WriteTObject(&unmatchPt);
	f->WriteTObject(&matchfraction);

	f->WriteTObject(&labelcomp);

	f->WriteTObject(&mugf);
	f->WriteTObject(&egf);
	f->WriteTObject(&pigf);
	f->WriteTObject(&kgf);
	f->WriteTObject(&pgf);
	f->WriteTObject(&denomgf);

	f->WriteTObject(&drmu);
	f->WriteTObject(&dre);
	f->WriteTObject(&drpi);
	f->WriteTObject(&drk);
	f->WriteTObject(&drp);

	f->WriteTObject(&dptmu);
	f->WriteTObject(&dpte);
	f->WriteTObject(&dptpi);
	f->WriteTObject(&dptk);
	f->WriteTObject(&dptp);

	auto rawptstack = new THStack("rawptstack","Muon p_{T}");
	rawmatchPt.SetFillColor(kRed);
	rawunmatchPt.SetFillColor(kBlack);
   	rawptstack->Add(&rawmatchPt);
	rawptstack->Add(&rawunmatchPt);
	f->WriteTObject(rawptstack);

	auto ptstack = new THStack("ptstack","Muon p_{T}");
	matchPt.SetFillColor(kRed);
	unmatchPt.SetFillColor(kBlack);
   	ptstack->Add(&matchPt);
	ptstack->Add(&unmatchPt);
	f->WriteTObject(ptstack);
	

	//Draw final plots to canvas
	TCanvas* c1 = new TCanvas();
	rawptstack->Draw();
	c1->BuildLegend();

	TCanvas* c2 = new TCanvas();
	ptstack->Draw();
	c2->BuildLegend();

	TCanvas* c3 = new TCanvas();
	labelcomp.Draw("bar");

	TCanvas* c4 = new TCanvas();
	flavstack->Draw("nostackb");
	c4->BuildLegend();

	TCanvas* c5 = new TCanvas();
	//drk.SetTitle("Delta R");
	drk.Draw("hist C");
	dre.Draw("same hist C");
	drpi.Draw("same hist C");
	drmu.Draw("same hist C");
	drp.Draw("same hist C");
	c5->BuildLegend();
	drk.SetTitle("Delta R");
	c5->Update();

	TCanvas* c6 = new TCanvas();

	dptmu.Draw("hist C");
	dpte.Draw("same hist C");
	dptpi.Draw("same hist C");
	dptk.Draw("same hist C");
	dptp.Draw("same hist C");
	c6->BuildLegend();
	dptmu.SetTitle("Rel. dPt");
	c6->Update();

	TCanvas* c7 = new TCanvas();
	rawmatchfraction.Draw("bar");
	TCanvas* c8 = new TCanvas();
	matchfraction.Draw("bar");

	f->Write();
	f->Close();


}
