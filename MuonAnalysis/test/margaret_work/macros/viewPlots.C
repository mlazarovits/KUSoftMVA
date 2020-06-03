#include <iostream>

void viewPlots(string inVar){
	string dypath="/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root";
	
	string qcdpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root';
	
	string ttpath='/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/TTJets2018_MINI_numEvent100000.root';

	TFile* fDY = TFile::Open(dypath.c_str());
	TFile* fQCD = TFile::Open(qcdpath.c_str());
	TFile* fTT = TFile::Open(ttpath.c_str());

	TString filename = ("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots/"+inVar+"2018.root").c_str();

	TFile* oFile = new TFile(filename,"RECREATE");

	TCanvas* cv = new TCanvas("cv","cv",800,800);
	TLegend* leg = new TLegend(0.35,0.2,0.95,0.4);

	cv->SetGridx();
	cv->SetGridy();


	fDY->cd();
	Events->Draw((inVar+">>histDY").c_str(),"","goff");
	histDY->SetLineColor(kRed);
	histDY->Draw();
	leg->AddEntry(histDY);

	fQCD->cd();
	Events->Draw((inVar+">>histQCD").c_str(),"","goff");
	histQCD->SetLineColor(kBlue);
	histQCD->Draw("same");
	leg->AddEntry(histQCD);


	fTT->cd();
	Events->Draw((inVar+">>histTT").c_str(),"","goff");
	histTT->SetLineColor(kGreen);
	histTT->Draw("same");
	leg->AddEntry(histTT);

	leg->Draw("same"):

	file->cd();
	cv->Write();











}