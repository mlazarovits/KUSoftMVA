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

	TString filename = "/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots/trainVars/unmatchedMuons2018.root";
	TFile* oFile = new TFile(filename,"RECREATE");

	
	// do plots over all samples, broken down by generator pdg id
	
	for(int i = 0; i < trainVars.size(); i++){
		cout << "Plotting " << trainVars[i] << endl;

		TCanvas* cv = new TCanvas(trainVars[i].c_str(),trainVars[i].c_str(),800,600);
		TLegend* leg = new TLegend(0.55,0.4,0.75,0.6);


		cv->SetGridx();
		cv->SetGridy();
		cv->SetLogy();


		qcdTree->Draw((trainVars[i]+">>treehistQCD").c_str(),"","goff");
		TH1F* treehistQCD = (TH1F*)gDirectory->Get("treehistQCD");

		TH1F* histQCD = new TH1F("histQCD","histQCD",treehistQCD->GetNbinsX(),treehistQCD->GetXaxis()->GetXmin(),treehistQCD->GetXaxis()->GetXmax());
		delete treehistQCD;
	
		for(int evt = 0; evt < qcdTree->GetEntries(); evt++){
			qcdTree->GetEntry(evt);

			int nMus = qcdTree->GetLeaf(trainVars[i].c_str())->GetNdata();

			for(int mu = 0; mu < nMus; mu++){
				float var = qcdTree->GetLeaf(trainVars[i].c_str())->GetValue(mu);
				int genIdx = qcdTree->GetLeaf("Muon_genPartIdx")->GetValue(mu);
				// int genPdgId = qcdTree->GetLeaf("GenPart_pdgId")->GetValue(genIdx);

				if(genIdx != -1) continue;
				histQCD->Fill(var);
			}
		}
	
		histQCD->SetTitle("QCD 2018");
		leg->AddEntry(histQCD);
	


		dyTree->Draw((trainVars[i]+">>treehistDY").c_str(),"","goff");
		TH1F* treehistDY = (TH1F*)gDirectory->Get("treehistDY");

		TH1F* histDY = new TH1F("histDY","histDY",treehistDY->GetNbinsX(),treehistDY->GetXaxis()->GetXmin(),treehistDY->GetXaxis()->GetXmax());
		delete treehistDY;
	
		for(int evt = 0; evt < dyTree->GetEntries(); evt++){
			dyTree->GetEntry(evt);

			int nMus = dyTree->GetLeaf(trainVars[i].c_str())->GetNdata();

			for(int mu = 0; mu < nMus; mu++){
				float var = dyTree->GetLeaf(trainVars[i].c_str())->GetValue(mu);
				int genIdx = dyTree->GetLeaf("Muon_genPartIdx")->GetValue(mu);
				// int genPdgId = dyTree->GetLeaf("GenPart_pdgId")->GetValue(genIdx);

				if(genIdx != -1) continue;

				histDY->Fill(var);
			}
		}
	
		histDY->SetTitle("DY+jets 2018");
		leg->AddEntry(histDY);
	

		ttTree->Draw((trainVars[i]+">>treehistTT").c_str(),"","goff");
		TH1F* treehistTT = (TH1F*)gDirectory->Get("treehistTT");

		TH1F* histTT = new TH1F("histTT","histTT",treehistTT->GetNbinsX(),treehistTT->GetXaxis()->GetXmin(),treehistTT->GetXaxis()->GetXmax());
		delete treehistTT;
	
		for(int evt = 0; evt < ttTree->GetEntries(); evt++){
			ttTree->GetEntry(evt);

			int nMus = ttTree->GetLeaf(trainVars[i].c_str())->GetNdata();

			for(int mu = 0; mu < nMus; mu++){
				float var = ttTree->GetLeaf(trainVars[i].c_str())->GetValue(mu);
				int genIdx = ttTree->GetLeaf("Muon_genPartIdx")->GetValue(mu);
				// int genPdgId = ttTree->GetLeaf("GenPart_pdgId")->GetValue(genIdx);

				if(genIdx != -1) continue;

				histTT->Fill(var);
			}
		}
	
		histTT->SetTitle("TTbar 2018");
		leg->AddEntry(histTT);


		if(histTT->GetMaximum() > histDY->GetMaximum() && histTT->GetMaximum() > histQCD->GetMaximum()){
			histTT->SetLineColor(kBlue);
			histTT->Draw("same");
			if(histDY->GetMaximum() > histQCD->GetMaximum()){
				histDY->SetLineColor(kRed);
				histDY->Draw("same");


				histQCD->SetLineColor(kGreen);
				histQCD->Draw("same");
			}
			else{
				histQCD->SetLineColor(kGreen);
				histQCD->Draw("same");

				histDY->SetLineColor(kRed);
				histDY->Draw("same");
			}
		}


		else if(histDY->GetMaximum() > histTT->GetMaximum() && histDY->GetMaximum() > histQCD->GetMaximum()){
			histDY->SetLineColor(kRed);
			histDY->Draw("same");
			if(histTT->GetMaximum() > histQCD->GetMaximum()){
				histTT->SetLineColor(kBlue);
				histTT->Draw("same");


				histQCD->SetLineColor(kGreen);
				histQCD->Draw("same");
			}
			else{
				histQCD->SetLineColor(kGreen);
				histQCD->Draw("same");

				histTT->SetLineColor(kBlue);
				histTT->Draw("same");
			}
		}

		else if(histQCD->GetMaximum() > histDY->GetMaximum() && histQCD->GetMaximum() > histTT->GetMaximum()){
			histQCD->SetLineColor(kGreen);
			histQCD->Draw("same");
			if(histDY->GetMaximum() > histTT->GetMaximum()){
				histDY->SetLineColor(kRed);
				histDY->Draw("same");


				histTT->SetLineColor(kBlue);
				histTT->Draw("same");
			}
			else{
				histTT->SetLineColor(kBlue);
				histTT->Draw("same");

				histDY->SetLineColor(kRed);
				histDY->Draw("same");
			}
		}

		



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
		cv->Close();

		delete histQCD;
		delete histDY;
		delete histTT;

	}
	oFile->Close();

	
	
	
	
	

	











}
