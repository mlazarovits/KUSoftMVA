#include <iostream>

// #include "../include/prod2016MC_reducedNANO_Triggers.h"
// #include "../include/prod2017MC_reducedNANO_Triggers.h"
// #include "../include/prod2018MC_reducedNANO_Triggers.h"
#include "../interface/SoftIdEfficiency.hh"
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
	vector<TEfficiency*> TTJets;
	TriggerSet wjets16_mu(fTTJets);
	TTJets.SetSampleName("TTJets 2018");
	TTJets.AddID("Muon_mvaID");
	TTJets.AddTrigger("Muon_softID");
	TTJets.AddTrigger("Muon_softMvaID");
	TTJets.SetVar("Muon_pt");
	TTJets.SetOutputName("TTJets_softIDeffs.root");

	TTJets_eff = TTJets.Analyze();
	TTJets.makePlots(TTJets_eff);
}




// else if(sampleName=="QCD"){
// 	if(fQCD == NULL) return;
// 	vector<TEfficiency*> QCD;
// 	TriggerSet wjets16_ele(fQCD);
// 	QCD.SetSampleName("WJetsToLNu 2016 Loose ID");
// 	QCD.AddTrigger("HLT_Ele27_WPTight_Gsf");
// 	QCD.AddTrigger("HLT_Photon175");
// 	QCD.AddTrigger("HLT_Ele115_CaloIdVT_GsfTrkIdT");
// 	QCD.AddTrigger("HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50");
// 	QCD.AddTrigger("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165");
// 	QCD.AddTrigger("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165");
// 	QCD.SetVar("Electron_pt");
// 	QCD.SetOutputName("WJets16_AllTrigs_SingleEle_loose.root");

// 	wjets16_ele_effs = QCD.Analyze();
// 	QCD.makePlots(wjets16_ele_effs);
// }

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