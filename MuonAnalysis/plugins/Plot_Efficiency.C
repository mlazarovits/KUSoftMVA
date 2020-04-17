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
	if(gSystem->OpenDirectory("plots") == 0){
		gSystem->mkdir("plots");
		cout << "Created plots folder." << endl;
	}

	
	string gPathname = "/home/t3-ku/mlazarov/CMSSW_10_6_8/src/KUSoftMVA/MuonAnalysis/test/";
	TFile* fTTJets = TFile::Open((gPathname+"OutputFiles/TTJets2018_NANO.root").c_str());
	TFile* fQCD = NULL;
	TFile* fDYJets = NULL;
	


if(sampleName=="TTJets"){
	if(fTTJets == NULL) return;
	SoftIdEfficiency TTJets(fTTJets);
	TTJets.SetSampleName("TTJets 2018 Medium ID");

	TTJets.AddID("Muon_mvaId");
	TTJets.AddID("Muon_softId");
	TTJets.AddID("Muon_softMvaId");

	TTJets.SetVar("Muon_pt");
	TTJets.SetOutputName("TTJets_softIDeffs_1L.root");

	vector<TEfficiency*> TTJets_eff = TTJets.Analyze();
	TTJets.make2DPlots(TTJets_eff);
}




else if(sampleName=="QCD"){
	if(fQCD == NULL) return;
	vector<TEfficiency*> QCD_effs;
	TriggerSet QCD(fQCD);
	QCD.SetSampleName("QCD 2018");

	QCD.AddID("Muon_mvaId");
	QCD.AddID("Muon_softId");
	QCD.AddID("Muon_softMvaId");

	QCD.SetVar("Muon_pt");
	QCD.SetOutputName("QCD_softIDeffs.root");

	vector<TEfficiency*> QCD_effs = QCD.Analyze();
	QCD.makePlots(QCD_effs);
}

// else if(sampleName=="DYJets"){
// 	if(fDYJets == NULL) return;
// 	vector<TEfficiency*> DYJets;
// 	TriggerSet wjets17_ele(fDYJets);
// 	wjets17_ele.SetSampleName("WJetsToLNu 2017 Loose ID");
// 	wjets17_ele.AddTrigger("HLT_Ele32_WPTight_Gsf_L1DoubleEG"); //with HLT_Ele35_WPTight_Gsf_L1EGMT requirement
// 	wjets17_ele.AddTrigger("HLT_Ele35_WPTight_Gsf");
// 	wjets17_ele.AddTrigger("HLT_Photon200");
// 	wjets17_ele.AddTrigger("HLT_Ele115_CaloIdVT_GsfTrkIdT");
// 	wjets17_ele.AddTrigger("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165");
// 	wjets17_ele.SetVar("Electron_pt");
// 	wjets17_ele.SetOutputName("WJets17_AllTrigs_SingleEle_loose.root");

// 	wjets17_ele_effs = wjets17_ele.Analyze();
// 	wjets17_ele.makePlots(wjets17_ele_effs);
// }




else{
	cout << "Invalid sampleName" << endl;
	return;
}




	
}