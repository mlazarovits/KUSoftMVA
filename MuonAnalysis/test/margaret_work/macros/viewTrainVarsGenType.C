#include <iostream>
#include "TLatex.h"

void viewTrainVarsGenType(string opt){
	string opts[] = {"dyjets","all","qcd","ttbar"};
	string* it = std::find(std::begin(opts), std::end(opts),opt);
	if(it == std::end(opts)){
		cout << "Error: invalid option " << opt << " specified" << endl;
		cout << "Valid options are: dyjets, qcd, ttbar, all" << endl;
		return;
	}
	

	string path;
	TFile* file;
	TTree* tree;
	TChain* chain;

	if(opt == "dyjets"){
		path ="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root";
		file = TFile::Open(path.c_str());
		tree = (TTree*)file->Get("Events");
	}
	else if(opt == "qcd"){
		path ="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root";
	file = TFile::Open(path.c_str());
	tree = (TTree*)file->Get("Events");
	}
	else if(opt == "ttbar"){
		path ="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root";
		file = TFile::Open(path.c_str());
		tree = (TTree*)file->Get("Events");
	}
	else if(opt == "all"){
		chain = new TChain("Events");
		chain->AddFile("/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root");
		chain->AddFile("/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root");
		chain->AddFile("/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root");
		tree = chain->GetTree();
	}

	

	

	std::vector<string> trainVars = {"Muon_pt","Muon_eta","Muon_chi2LocalMomentum",
		"Muon_chi2LocalPosition","Muon_trkRelChi2","Muon_trkKink","Muon_glbKink",
		"Muon_segmentCompatibility","Muon_timeAtIpInOutErr","Muon_innerTrackNormalizedChi2",
		"Muon_innerTrackValidFraction","Muon_nTrackerLayersWithMeasurement",
		"Muon_outerTrackCharge","Muon_innerTrackCharge","Muon_pfRelIso03_chg",
		"Muon_pfRelIso03_all","Muon_isGood","Muon_isHighPurity","Muon_nPixelLayers",
		"Muon_miniPFRelIso_chg","Muon_miniPFRelIso_all"};

	
	gStyle->SetOptStat(0);

	

	TString outFilename = ("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots/trainVars/"+opt+"byGenTypeMuons2018.root").c_str();
	TFile* oFile = new TFile(outFilename,"RECREATE");

	

	
	
	
	for(int i = 0; i < trainVars.size(); i++){
		cout << "Plotting " << trainVars[i] << " for " << opt << " muons" << endl;

		TCanvas* cv = new TCanvas(trainVars[i].c_str(),trainVars[i].c_str(),800,600);
		TLegend* leg = new TLegend(0.55,0.4,0.75,0.6);
		


		cv->SetGridx();
		cv->SetGridy();
		cv->SetLogy();


		if(opt != "all") tree->Draw((trainVars[i]+">>treehist").c_str(),"","goff");
		else chain->Draw((trainVars[i]+">>treehist").c_str(),"","goff");
		TH1F* treehist = (TH1F*)gDirectory->Get("treehist");

		TH1F* hUnm = new TH1F("hUnm","hUnm",treehist->GetNbinsX(),treehist->GetXaxis()->GetXmin(),treehist->GetXaxis()->GetXmax());
		TH1F* hTrue = new TH1F("hTrue","hTrue",treehist->GetNbinsX(),treehist->GetXaxis()->GetXmin(),treehist->GetXaxis()->GetXmax());
		TH1F* hPion = new TH1F("hPion","hPion",treehist->GetNbinsX(),treehist->GetXaxis()->GetXmin(),treehist->GetXaxis()->GetXmax());
		TH1F* hKaon = new TH1F("hKaon","hKaon",treehist->GetNbinsX(),treehist->GetXaxis()->GetXmin(),treehist->GetXaxis()->GetXmax());
		TH1F* hAll = new TH1F("hAll","hAll",treehist->GetNbinsX(),treehist->GetXaxis()->GetXmin(),treehist->GetXaxis()->GetXmax());

		delete treehist;

		
		int nEvts;
		if(opt != "all") nEvts = tree->GetEntries();
		else nEvts = chain->GetEntries();
	
		for(int evt = 0; evt < nEvts; evt++){
			if(opt != "all") tree->GetEntry(evt);
			else chain->GetEntry(evt);

			int nMus;
			if(opt != "all") nMus = tree->GetLeaf(trainVars[i].c_str())->GetNdata();
			else nMus = chain->GetLeaf(trainVars[i].c_str())->GetNdata();

			for(int mu = 0; mu < nMus; mu++){
				float var;
				if(opt != "all") var = tree->GetLeaf(trainVars[i].c_str())->GetValue(mu);
				else var = chain->GetLeaf(trainVars[i].c_str())->GetValue(mu);
				int genIdx;
				if(opt != "all") genIdx = tree->GetLeaf("Muon_genPartIdx")->GetValue(mu);
				else genIdx = chain->GetLeaf("Muon_genPartIdx")->GetValue(mu);

				hAll->Fill(var);
				
				
				if(genIdx == -1){
					hUnm->Fill(var);
					continue;
				}
				

				int genPdgId;
				if(opt != "all") tree->GetLeaf("GenPart_pdgId")->GetValue(genIdx);
				else chain->GetLeaf("GenPart_pdgId")->GetValue(genIdx);
				if(abs(genPdgId) == 13){
					hTrue->Fill(var);
					continue;
				}
				
				else if(abs(genPdgId) == 211){
					hPion->Fill(var);
					continue;
				}

				
				else if(abs(genPdgId) == 321){
					hKaon->Fill(var);
					continue;
				}

				
			}
		}
	
		hAll->SetTitle("all reco muons");
		hUnm->SetTitle("unmatched muons");
		hTrue->SetTitle("true muons");
		hPion->SetTitle("pions");
		hKaon->SetTitle("kaons");


		leg->AddEntry(hAll);
		leg->AddEntry(hUnm);
		leg->AddEntry(hTrue);
		leg->AddEntry(hPion);
		leg->AddEntry(hKaon);
	

		hAll->SetLineColor(kBlue);
		hUnm->SetLineColor(kRed);
		hTrue->SetLineColor(kGreen);
		hPion->SetLineColor(kMagenta);
		hKaon->SetLineColor(kCyan);

		hAll->Draw();
		hUnm->Draw("same");
		hTrue->Draw("same");
		hPion->Draw("same");
		hKaon->Draw("same");



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
		l.DrawLatex(0.40,0.92,(trainVars[i]+" "+opt+" Sample").c_str());
		cv->Update();



		oFile->cd();
		cv->Write();
		cv->Close();

		delete hUnm;
		delete hTrue;
		delete hPion;
		delete hKaon;
		delete hAll;

	}
	oFile->Close();
	return;

	
	
	
	
	

	











}
