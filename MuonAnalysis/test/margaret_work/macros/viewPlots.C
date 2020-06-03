#include <iostream>
#include "TLatex.h"

void viewPlots(string inVar){
	string dypath="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root";
	
	string qcdpath="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root";
	
	string ttpath="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root";

	TFile* fDY = TFile::Open(dypath.c_str());
	TFile* fQCD = TFile::Open(qcdpath.c_str());
	TFile* fTT = TFile::Open(ttpath.c_str());

	TString filename = ("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots/"+inVar+"2018.root").c_str();

	TFile* oFile = new TFile(filename,"RECREATE");

	TCanvas* cv = new TCanvas("cv","cv",800,600);
	TLegend* leg = new TLegend(0.35,0.2,0.95,0.4);

	cv->SetGridx();
	cv->SetGridy();
	cv->SetLogy();
	gStyle->SetOptStat(0);

	fQCD->cd();
	TTree* qcdTree = (TTree*)fQCD->Get("Events");
	qcdTree->SetBranchStatus("*",0);
	qcdTree->SetBranchStatus(inVar.c_str(),1);
	
	qcdTree->Draw((inVar+">>histQCD").c_str(),"","goff");
	TH1F* histQCD = (TH1F*)gDirectory->Get("histQCD");
	histQCD->SetTitle("QCD 2018");
	leg->AddEntry(histQCD);
	histQCD->SetLineColor(kGreen);
	histQCD->Draw("same");
	delete qcdTree;


	fDY->cd();
	TTree* dyTree = (TTree*)fDY->Get("Events");
	dyTree->SetBranchStatus("*",0);
	dyTree->SetBranchStatus(inVar.c_str(),1);

	dyTree->Draw((inVar+">>histDY").c_str(),"","goff");
	TH1F* histDY = (TH1F*)gDirectory->Get("histDY");
	histDY->SetTitle("DY+jets 2018");
	leg->AddEntry(histDY);
	histDY->SetLineColor(kRed);
	histDY->Draw("same");
	delete dyTree;

	


	fTT->cd();
	TTree* ttTree = (TTree*)fTT->Get("Events");
	ttTree->SetBranchStatus("*",0);
	ttTree->SetBranchStatus(inVar.c_str(),1);
	
	ttTree->Draw((inVar+">>histTT").c_str(),"","goff");
	TH1F* histTT = (TH1F*)gDirectory->Get("histTT");
	histTT->SetTitle("ttbar 2018");
	leg->AddEntry(histTT);
	histTT->SetLineColor(kBlue);
	histTT->Draw("same");
	delete ttTree;

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
	l.DrawLatex(0.40,0.92,inVar.c_str());
	cv->Update();

	oFile->cd();
	cv->Write();











}
