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

void Plot_Efficiency(TString sampleName){
	if(gSystem->OpenDirectory("/home/t3-ku/mlazarov/CMSSW_10_6_8/src/KUSoftMVA/MuonAnalysis/plots/") == 0){
		gSystem->mkdir("/home/t3-ku/mlazarov/CMSSW_10_6_8/src/KUSoftMVA/MuonAnalysis/plots/");
		cout << "Created plots folder." << endl;
	}

	
	string gPathname = "/home/t3-ku/mlazarov/CMSSW_10_6_8/src/KUSoftMVA/MuonAnalysis/test/";
	TFile* fTTJets = TFile::Open((gPathname+"OutputFiles/TTJets2018_NANO.root").c_str());
	TFile* fQCD = NULL;
	TFile* fDYJets = NULL;
	


if(sampleName=="TTJets"){
	if(fTTJets == NULL) return;
	SoftIdEfficiency TTJets(fTTJets);
	string name = "TTJets_softIDeffs_1L_looseID_GenStatusFlag";
	TTJets.SetSampleName(name);

	TTJets.AddID("Muon_mvaId");
	TTJets.AddID("Muon_softId");
	TTJets.AddID("Muon_softMvaId");

	TTJets.SetVar("GenPart_statusFlags");
	TTJets.SetOutputName(name+".root");

	vector<TEfficiency*> TTJets_eff = TTJets.Analyze();
	TTJets.makePlot(TTJets_eff);
}




else if(sampleName=="QCD"){
	if(fQCD == NULL) return;
	SoftIdEfficiency QCD(fQCD);
	string name = "QCD_softIDeffs";
	QCD.SetSampleName(name);
	
	QCD.AddID("Muon_mvaId");
	QCD.AddID("Muon_softId");
	QCD.AddID("Muon_softMvaId");

	QCD.SetVar("Muon_pt");
	QCD.SetOutputName(name+".root");

	vector<TEfficiency*> QCD_effs = QCD.Analyze();
	QCD.makePlot(QCD_effs);
}

else if(sampleName=="DYJets"){
	if(fDYJets == NULL) return;
	string name = "DYJets_softIDeffs_looseID";
	SoftIdEfficiency DYJets(fDYJets);

	DYJets.SetSampleName(name);
	DYJets.AddID("Muon_mvaId");
	DYJets.AddID("Muon_softId");
	DYJets.AddID("Muon_softMvaId");

	DYJets.SetVar("Muon_pt");

	DYJets.SetOutputName(name+".root");

	vector<TEfficiency*> DYJets_effs = DYJets.Analyze();
	DYJets.makePlot(DYJets_effs);
}




else{
	cout << "Invalid sampleName" << endl;
	return;
}




	
}