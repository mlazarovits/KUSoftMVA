#include <iostream>

// #include "../include/prod2016MC_reducedNANO_Triggers.h"
// #include "../include/prod2017MC_reducedNANO_Triggers.h"
// #include "../include/prod2018MC_reducedNANO_Triggers.h"
#include "../interface/SoftIdEfficiency.h"
#include "TEfficiency.h"
#include "TGraphAsymmErrors.h"
#include "TMultiGraph.h"
#include "TCanvas.h"
#include "TGraph.h"


using namespace std;

void Plot_Efficiency(TString sampleName,string plotType){
	if(gSystem->OpenDirectory("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots") == 0){
		gSystem->mkdir("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots");
		cout << "Created plots folder." << endl;
	}

	
	string gPathname = "/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/";
	TFile* fTTJets = TFile::Open((gPathname+"OutputFiles/TTJets2018_MINI_numEvent100000.root").c_str());
	TFile* fQCD = TFile::Open((gPathname+"OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root").c_str());
	TFile* fDYJets = TFile::Open((gPathname+"OutputFiles/DYJetsToLL2018_MINI_numEvent100.root").c_str());
	
	TFile *allFiles = TFile::Open((gPathname+"OutputFiles/allSamples_MINI_100000.root").c_str());
	// TChain* allFiles = new TChain("Events");
	// allFiles->Add((gPathname+"OutputFiles/TTJets2018_MINI_numEvent100000.root").c_str());
	// allFiles->Add((gPathname+"OutputFiles/QCD_pt_600to800_2018_MINI_numEvent100000.root").c_str());
	// allFiles->Add((gPathname+"OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root").c_str());


if(sampleName=="TTJets"){
	if(fTTJets == NULL) return;
	SoftIdEfficiency TTJets(fTTJets);
	string name = "TTJets_softID"+plotType;
	TTJets.SetSampleName(name);

	TTJets.AddID("Muon_softId");  //with loose ID
	TTJets.AddID("Muon_softId");
	TTJets.AddID("Muon_softMvaId");


	TTJets.SetVar("Muon_pt");
	TTJets.SetOutputName(name+".root");

	vector<TEfficiency*> TTJets_eff = TTJets.Analyze(plotType);
	TTJets.makePlot(TTJets_eff);
}


else if(sampleName=="QCD"){
	if(fQCD == NULL) return;
	SoftIdEfficiency QCD(fQCD);
	string name = "QCD_softIDeffs_pt";
	QCD.SetSampleName(name);
	
	QCD.AddID("Muon_softId");
	QCD.AddID("Muon_softMvaId");

	QCD.SetVar("Muon_pt");
	QCD.SetOutputName(name+".root");

	vector<TEfficiency*> QCD_effs = QCD.Analyze(plotType);
	QCD.makePlot(QCD_effs);
}

else if(sampleName=="DYJets"){
	if(fDYJets == NULL) return;
	SoftIdEfficiency DYJets(fDYJets);
	string name = "DYJets_softIDeffs_looseID_pt";

	DYJets.SetSampleName(name);
	DYJets.AddID("Muon_softId");
	DYJets.AddID("Muon_softMvaId");

	DYJets.SetVar("Muon_pt");
	DYJets.SetOutputName(name+".root");

	vector<TEfficiency*> DYJets_effs = DYJets.Analyze(plotType);
	DYJets.makePlot(DYJets_effs);
}

else if(sampleName=="allFiles"){
	if(allFiles == NULL) return;
	string name = "AllSamples_softIDeffs_looseID";
	SoftIdEfficiency allSamples(allFiles);

	allSamples.SetSampleName(name);
	allSamples.AddID("Muon_softId");
	allSamples.AddID("Muon_softMvaId");

	allSamples.SetVar("Muon_pt");

	allSamples.SetOutputName(name+".root");

	vector<TEfficiency*> allSamples_effs = allSamples.Analyze(plotType);
	allSamples.makePlot(allSamples_effs);
}




else{
	cout << "Invalid sampleName" << endl;
	return;
}




	
}
