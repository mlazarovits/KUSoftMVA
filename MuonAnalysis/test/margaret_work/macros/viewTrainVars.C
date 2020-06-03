#include <iostream>
#include "TLatex.h"

void viewTrainVars(){
	string dypath="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root";
	
	string qcdpath="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root";
	
	string ttpath="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root";

	TFile* fDY = TFile::Open(dypath.c_str());
	TFile* fQCD = TFile::Open(qcdpath.c_str());
	TFile* fTT = TFile::Open(ttpath.c_str());

	std::vector<string> trainVars = {"Muon_pt","Muon_eta","Muon_chi2LocalMomentum",
		"Muon_chi2LocalPosition","Muon_trkRelChi2","Muon_trkKink","Muon_glbKink",
		"Muon_segmentCompatibility","Muon_timeAtIpInOutErr","Muon_innerTrackNormalizedChi2",
		"Muon_innerTrackValidFraction","Muon_nTrackerLayersWithMeasurement",
		"Muon_outerTrackCharge","Muon_innerTrackCharge","Muon_pfRelIso03_chg",
		"Muon_pfRelIso03_all","Muon_isGood","Muon_isHighPurity","Muon_nPixelLayers",
		"Muon_miniPFRelIso_chg","Muon_miniPFRelIso_all"};

	
	gStyle->SetOptStat(0);

	fQCD->cd();
	TTree* qcdTree = (TTree*)fQCD->Get("Events");
	fDY->cd();
	TTree* dyTree = (TTree*)fDY->Get("Events");
	fTT->cd();
	TTree* ttTree = (TTree*)fTT->Get("Events");

	

	for(int i = 0; i < 2; i++){
		cout << "Plotting " << trainVars[i] << endl;

		TString filename = ("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots/trueMuons"+trainVars[i]+"2018.root").c_str();
		TFile* oFile = new TFile(filename,"RECREATE");
		

		TCanvas* cv = new TCanvas("cv","cv",800,600);
		TLegend* leg = new TLegend(0.55,0.4,0.75,0.6);


		cv->SetGridx();
		cv->SetGridy();
		cv->SetLogy();




		qcdTree->Draw((trainVars[i]+">>treehistQCD").c_str(),"","goff");
		TH1F* treehistQCD = (TH1F*)gDirectory->Get("treehistQCD");

		TH1F* histQCD = new TH1F("histQCD","histQCD",treehistQCD->GetNbinsX(),treehistQCD->GetXaxis()->GetXmin(),treehistQCD->GetXaxis()->GetXmax());
		delete treehistQCD;
		// qcdTree->SetBranchStatus("*",0);
		// qcdTree->SetBranchStatus(trainVars[i].c_str(),1);
		for(int evt = 0; evt < qcdTree->GetEntries(); evt++){
			qcdTree->GetEntry(evt);
			// cout << "evt: " << evt << endl;
			int nMus = qcdTree->GetLeaf(trainVars[i].c_str())->GetNdata();
			// cout << "a" << endl;
			for(int mu = 0; mu < nMus; mu++){
				float var = qcdTree->GetLeaf(trainVars[i].c_str())->GetValue(mu);
				// cout << "mu: " << mu << endl;
				histQCD->Fill(var);
			}
		}
		cout << "b" << endl;
		histQCD->SetTitle("QCD 2018");
		cout << "c" << endl;
		leg->AddEntry(histQCD);
		histQCD->SetLineColor(kGreen);
		histQCD->Draw("same");
		cout << "d" << endl;


		// dyTree->Draw((trainVars[i]+">>histDY").c_str(),"","goff");
		// TH1F* histDY = (TH1F*)gDirectory->Get("histDY");
		// histDY->SetTitle("DY+jets 2018");
		// leg->AddEntry(histDY);
		// histDY->SetLineColor(kRed);
		// histDY->Draw("same");


		// ttTree->Draw((trainVars[i]+">>histTT").c_str(),"","goff");
		// TH1F* histTT = (TH1F*)gDirectory->Get("histTT");
		// histTT->SetTitle("ttbar 2018");
		// leg->AddEntry(histTT);
		// histTT->SetLineColor(kBlue);
		// histTT->Draw("same");



		leg->SetTextFont(132);
		leg->SetTextSize(0.03);
		leg->SetFillColor(kWhite);
		leg->SetLineColor(kWhite);
		leg->SetShadowColor(kWhite);



		leg->Draw("same");

		TLatex l;
		l.SetTextFont(132);
		l.SetNDC();
		l.SetTextSize(0.035);
		l.SetTextFont(42);
		l.SetTextSize(0.03);
		l.SetTextFont(61);
		l.DrawLatex(0.16,0.92,"CMS");
		l.SetTextFont(52);
		l.DrawLatex(0.21,0.92,"Preliminary");
		l.SetTextFont(132);
		l.SetNDC();
		l.SetTextSize(0.05);
		l.SetTextFont(132);
		l.DrawLatex(0.40,0.92,trainVars[i].c_str());
		cv->Update();



		oFile->cd();
		cv->Write();
		oFile->Close();
		cv->Close();

	}

	
	
	
	
	

	











}
