#ifndef SoftIdEfficiency_HH
#define SoftIdEfficiency_HH

#include <string>
#include <iostream>
#include <TFile.h>
#include <TTree.h>
#include <TEfficiency.h>
#include <TLeaf.h>
// #include "../include/prod2016MC_reducedNANO_Triggers.h"
// #include "../include/prod2017MC_reducedNANO_Triggers.h"
// #include "../include/prod2018MC_reducedNANO_Triggers.h"
#include "softLepSignal.h"
#include <TLatex.h>


using namespace std;

class SoftIdEfficiency{
public:
	
	SoftIdEfficiency(TFile* file, bool i_debug=false);
	SoftIdEfficiency(TChain* chain);
	virtual ~SoftIdEfficiency(){};

	void AddFile(const string& filename);
	int GetNFile() const;
	string GetFile(int n);

	void SetSampleName(const string& samplename);
	string GetSampleName() const;

	void SetOutputName(const string& outname);
	string GetOutputName() const;

	void AddID(string ID);
	vector<string> GetIDs();

	void SetVar(string var);
	string GetVar();


	vector<TEfficiency*> Analyze(string Option);
	TEfficiency* Analyze2D();

	void makePlot(vector<TEfficiency*> effs);
	void make2DPlot(TEfficiency* eff);

	void SetCuts(string cuts);


	

private:
	
	float calcHT(TLeaf* nJet_leaf, TLeaf* Jet_pt_leaf, TLeaf* Jet_eta_leaf, TLeaf* Jet_phi_leaf, TLeaf* Jet_mass_leaf);
	TLorentzVector calcMHT(TLeaf* nJet_leaf, TLeaf* Jet_pt_leaf, TLeaf* Jet_eta_leaf, TLeaf* Jet_phi_leaf, TLeaf* Jet_mass_leaf);
	Double_t calcInvMass2Muons(int Muon1, int Muon2);	
	Double_t calcPt2Muons(int Muon1, int Muon2);
	void initializeAnalyze();
	std::vector<Double_t> makeEffBins(TString inputvar);

	std::vector<Int_t> Decimal2Binary(Int_t num);


	// bool GoldenMuonSelection();
	// bool DoubleMuonSelection();


	string m_samplename;
	string m_outname;
	TTree* m_tree;
	string m_var;
	string m_cuts;

	float etacut;

	TLeaf* l_nMuon;
	TLeaf* l_Muon_mediumId;
	TLeaf* l_Muon_mediumPromptId;
	TLeaf* l_Muon_tightId;
	TLeaf* l_Muon_miniIsoId;
	TLeaf* l_Muon_minipfRelIso_all;
	TLeaf* l_Muonpt;
	TLeaf* l_Muoneta;
	TLeaf* l_Muonphi;
	TLeaf* l_Muonmass;
	TLeaf* l_Muon_sip3d;
	TLeaf* l_GenPart_statusFlags;


	
	TLeaf* l_var;
	TLeaf* l_weight;

	vector<string> m_IDs;
	
	vector<string> m_filenames;

	bool debug=false;

	




};
#endif
// #define 

inline SoftIdEfficiency::SoftIdEfficiency(TFile* file,bool i_debug=false){
	m_tree = (TTree*)file->Get("Events");
	if(m_tree == NULL){
		cout << "Error: No tree found" << endl;
	}
	debug = i_debug;
}

inline SoftIdEfficiency::SoftIdEfficiency(TChain* chain){
	m_tree = chain;
	if(m_tree == NULL){
		cout << "Error: No tree found" << endl;
	}
}



inline void SoftIdEfficiency::AddFile(const string& filename){
	m_filenames.push_back(filename);
}

inline int SoftIdEfficiency::GetNFile() const {
  return m_filenames.size();
}
inline string SoftIdEfficiency::GetFile(int n){
  int N = GetNFile();
  if(n < 0 || n >= N)
    return "NO FILE";
  return m_filenames[n];
}




inline void SoftIdEfficiency::SetSampleName(const string& samplename){
	m_samplename = samplename;
}

inline string SoftIdEfficiency::GetSampleName() const{
	return m_samplename;
}

inline void SoftIdEfficiency::SetOutputName(const string& outname){
	m_outname = outname;
}
inline string SoftIdEfficiency::GetOutputName() const {
	return m_outname;
}




inline void SoftIdEfficiency::AddID(string ID){
	m_IDs.push_back(ID);
}

inline vector<string> SoftIdEfficiency::GetIDs(){
	return m_IDs;
}

inline void SoftIdEfficiency::SetVar(string var){
	m_var = var;
}

inline string SoftIdEfficiency::GetVar(){
	return m_var;
}




inline void SoftIdEfficiency::SetCuts(string cuts){
	m_cuts = cuts;
}






inline float SoftIdEfficiency::calcHT(TLeaf* nJet_leaf, TLeaf* Jet_pt_leaf, TLeaf* Jet_eta_leaf, TLeaf* Jet_phi_leaf, TLeaf* Jet_mass_leaf){
	double HT = 0.;
	for(int i = 0; i < nJet_leaf->GetValue(); i++){
		HT+=Jet_pt_leaf->GetValue(i);
	}
	return HT;
}


inline TLorentzVector SoftIdEfficiency::calcMHT(TLeaf* nJet_leaf, TLeaf* Jet_pt_leaf, TLeaf* Jet_eta_leaf, TLeaf* Jet_phi_leaf, TLeaf* Jet_mass_leaf){
	TLorentzVector MHT(0.,0.,0.,0.);
	for(int i = 0; i < nJet_leaf->GetValue(); i++){
		TLorentzVector dummy;
		dummy.SetPtEtaPhiM(Jet_pt_leaf->GetValue(i),Jet_eta_leaf->GetValue(i),Jet_phi_leaf->GetValue(i),Jet_mass_leaf->GetValue(i));
		MHT -= dummy;
	}
	return MHT;
}

inline Double_t SoftIdEfficiency::calcInvMass2Muons(int Muon1, int Muon2){
	TLorentzVector lep1;
	TLorentzVector lep2;
	lep1.SetPtEtaPhiM(l_Muonpt->GetValue(Muon1),l_Muoneta->GetValue(Muon1),l_Muonphi->GetValue(Muon1),l_Muonmass->GetValue(Muon1));
	lep2.SetPtEtaPhiM(l_Muonpt->GetValue(Muon2),l_Muoneta->GetValue(Muon2),l_Muonphi->GetValue(Muon2),l_Muonmass->GetValue(Muon2));
	Double_t invmass = (lep1 + lep2).M();
	return invmass;
}

inline Double_t SoftIdEfficiency::calcPt2Muons(int Muon1, int Muon2){
	TLorentzVector lep1;
	TLorentzVector lep2;
	lep1.SetPtEtaPhiM(l_Muonpt->GetValue(Muon1),l_Muoneta->GetValue(Muon1),l_Muonphi->GetValue(Muon1),l_Muonmass->GetValue(Muon1));
	lep2.SetPtEtaPhiM(l_Muonpt->GetValue(Muon2),l_Muoneta->GetValue(Muon2),l_Muonphi->GetValue(Muon2),l_Muonmass->GetValue(Muon2));
	Double_t pt = (lep1 + lep2).Pt();
	return pt;
}


inline std::vector<Int_t> SoftIdEfficiency::Decimal2Binary(Int_t num){
	int i;
	std::vector<Int_t> binary;
	while(num != 0){
		binary.push_back(num % 2);
		num /= 2;
	}
	std::reverse(binary.begin(),binary.end());
	return binary;
}




inline void SoftIdEfficiency::initializeAnalyze(){
	l_nMuon = m_tree->GetLeaf("nMuon");
	l_Muonpt = m_tree->GetLeaf("Muon_pt");
	l_Muoneta = m_tree->GetLeaf("Muon_eta");
	l_Muonphi = m_tree->GetLeaf("Muon_phi");
	l_Muonmass = m_tree->GetLeaf("Muon_mass");
	l_Muon_mediumId = m_tree->GetLeaf("Muon_mediumId");
	l_Muon_mediumPromptId = m_tree->GetLeaf("Muon_mediumPromptId");
	l_Muon_tightId = m_tree->GetLeaf("Muon_tightId");
	l_Muon_miniIsoId = m_tree->GetLeaf("Muon_miniIsoId");
	l_Muon_minipfRelIso_all = m_tree->GetLeaf("Muon_miniPFRelIso_all");
	l_Muon_sip3d = m_tree->GetLeaf("Muon_sip3d");
	// l_GenPart_statusFlags = m_tree->GetLeaf("GenPart_statusFlags");

	
	l_var = m_tree->GetLeaf(m_var.c_str());
	l_weight = m_tree->GetLeaf("Generator_weight");
}



inline std::vector<Double_t> SoftIdEfficiency::makeEffBins(TString inputvar){
	//set bins of TEff object
	// Int_t nBins;
	std::vector<Double_t> effbins;
	
	if(strstr(inputvar, "pt")){
		effbins.push_back(2.0);
		// for(int i = 1; i < 60; i++){
		// 	effbins.push_back(effbins.at(i-1) + 0.5);
		// }
		for(int i = 1; i < 41; i++){
			effbins.push_back(effbins.at(i-1) +1.0);
			// cout << effbins[i] << endl;
		}
		
	}
	else if(strstr(inputvar, "eta")){

		// nBins = 200;
		// effbins.push_back(-3.05);
		// for(int i = 1; i < nBins+2; i++){
		// 	effbins.push_back(effbins.at(i-1) + 0.05);
		// 	// cout << effbins.at(i) << endl;
		// }
		//SOS binning
		// nBins = 5;
		effbins.push_back(0.0);
		// for(int i = 1; i < 2; i++){
		effbins.push_back(effbins.at(0) + 0.8);
		effbins.push_back(effbins.at(1) + 0.45);
		effbins.push_back(effbins.at(2) + 0.35);
		effbins.push_back(effbins.at(3) + 0.5);
		effbins.push_back(effbins.at(4) + 0.3);
		effbins.push_back(effbins.at(5) + 0.1);
		// }
	}
	else if(strstr(inputvar,"statusFlags")){
		effbins.push_back(0.0);
		for(int i = 1; i < 15; i++){
			effbins.push_back(effbins.at(i-1) + 1.0);
		}

	}
	else{
		cout << "Invalid variable for binning specified" << endl;
	}
	return effbins;
}




inline TEfficiency* SoftIdEfficiency::Analyze2D(){
	// vector<TEfficiency*> vec_eff;
	// vector<TLeaf*> vec_lID;
	TEfficiency* eff;
	TLeaf* l_ID;
	
	initializeAnalyze();

	int nEntries;
	if(l_var == NULL){
		cout << "Error: Variable " << m_var.c_str() << " not found" << endl;
		return eff;
	}

	vector<Double_t> effbinsx = makeEffBins("pt");
	Int_t nBinsx = effbinsx.size()-2;
	std::vector<Double_t> effbinsy = makeEffBins("eta");
	Int_t nBinsy = effbinsy.size()-2;


	//create TEfficiency objects and get ID leaves
	string title = (m_var+" vs."+m_IDs.at(0)+" Efficiency").c_str();
	string x_label = (";"+m_var).c_str();
	string y_label = ";#epsilon";
	eff = new TEfficiency(m_IDs.at(0).c_str(),(m_IDs.at(0)).c_str(),nBinsx,&effbinsx.at(0),nBinsy,&effbinsy.at(0));
	
	l_ID = m_tree->GetLeaf(m_IDs.at(0).c_str());

	
	if(l_ID == NULL){
		cout << "Error: ID " << m_IDs.at(0) << " not found" << endl;
		return eff;
	}
	

	if(debug == true) nEntries = 1E3;
	else if (debug == false) nEntries = m_tree->GetEntries();

	

	for(int evt = 0; evt < nEntries; evt++){
		

		m_tree->GetEntry(evt);
		if (evt % 1000 == 0) {
			fprintf(stdout, "\r  Processed events: %8d of %8d ", evt, nEntries);
		}
	    fflush(stdout);


	    int nMuon = l_nMuon->GetValue();
	    if(nMuon != 1) continue;
		
		
		bool bPassed = l_ID->GetValue();
		eff->Fill((bPassed),l_Muonpt->GetValue(1),fabs(l_Muoneta->GetValue(1)));  //subleading lepton
		
			
	}
	cout << endl;

	return eff;
}



inline vector<TEfficiency*> SoftIdEfficiency::Analyze(string Option){
	vector<TEfficiency*> vec_eff;
	vector<TLeaf*> vec_lID;
	
	initializeAnalyze();

	int nEntries;
	if(l_var == NULL){
		cout << "Error: Variable " << m_var.c_str() << " not found" << endl;
		return vec_eff;
	}

	vector<Double_t> effbins = makeEffBins(m_var.c_str());
	Int_t nBins = effbins.size()-2;
	

	//create TEfficiency objects and get ID leaves
	for(int i = 0; i < m_IDs.size(); i++){
		string title = (m_var+" vs."+m_IDs.at(i)+" Efficiency").c_str();
		string x_label = (";"+m_var).c_str();
		string y_label = ";#epsilon";
		TEfficiency* eff = new TEfficiency(m_IDs.at(i).c_str(),(m_IDs.at(i)).c_str(),nBins,&effbins.at(0));
		
		TLeaf* l_ID = m_tree->GetLeaf(m_IDs.at(i).c_str());

		
		if(l_ID == NULL){
			cout << "Error: ID " << m_IDs.at(i) << " not found" << endl;
			return vec_eff;
		}
		vec_eff.push_back(eff);
		vec_lID.push_back(l_ID);
	}

	if(debug == true) nEntries = 1E3;
	else if (debug == false) nEntries = m_tree->GetEntries();

	

	for(int evt = 0; evt < nEntries; evt++){
		

		m_tree->GetEntry(evt);
		if (evt % 1000 == 0) {
			fprintf(stdout, "\r  Processed events: %8d of %8d ", evt, nEntries);
		}
	    fflush(stdout);


	    // float HT = calcHT(l_nJet, l_Jet_pt, l_Jet_eta, l_Jet_phi, l_Jet_mass);
	    // TLorentzVector MHT = calcMHT(l_nJet, l_Jet_pt, l_Jet_eta, l_Jet_phi, l_Jet_mass);
 // cout << "a1" << endl;
	    int nMuon = l_nMuon->GetValue();
	     // cout << "a" << endl;
	    float nMediumMuons = 0;
	    float nTightMuons = 0;
	    int bitwiseStatusFlag;
	    std::vector<int> statusFlags;


	    // if(nMuon < 1) continue;
		// cout << "b" << endl;


		int genIdx;
		int genID;
	    for(int mu = 0; mu < nMuon; mu++){
	    	// genIdx = m_tree->GetLeaf("Muon_genPartIdx")->GetValue(mu);
	    	// genID = m_tree->GetLeaf("GenPart_pdgId")->GetValue(genIdx);


		    if(m_tree->GetLeaf("Muon_mediumId")->GetValue(mu)){
		    	nMediumMuons += 1;
		    }
		    if(m_tree->GetLeaf("Muon_tightId")->GetValue(mu)){
		    	nTightMuons += 1;
		    }	
		    bitwiseStatusFlag = m_tree->GetLeaf("GenPart_statusFlags")->GetValue(mu);
		    statusFlags = Decimal2Binary(bitwiseStatusFlag);
		    // if(m_tree->GetLeaf("Muon_softMvaId")->GetValue(mu) == 1){
			   //  cout << m_tree->GetLeaf("Muon_softMvaId")->GetValue(mu) << endl;
		    // }
		   
		}	
		 // cout << "c" << endl;


//efficiency = # true muons passed ID/ # true muons
// TH1D hNum("num_hist","num_hist",40,0,40);
// TH1D hDen("den_hist","den_hist",40,0,40);
// int nEvt = Events->GetEntries();
// for(int i = 0; i < nEvt; i++){
// Events->GetEntry(i);
// int nMuon = Events->GetLeaf("nMuon")->GetValue();
// for(int mu = 0; mu < nMuon; mu++){
// int genIdx = Events->GetLeaf("Muon_genPartIdx")->GetValue(mu);
// int genID = Events->GetLeaf("GenPart_pdgId")->GetValue(genIdx);
// if(abs(genID) != 13) continue;
// if(Events->GetLeaf("Muon_softId")->GetValue(mu)){
// hNum.Fill(Events->GetLeaf("Muon_pt")->GetValue(mu));
// hDen.Fill(Events->GetLeaf("Muon_pt")->GetValue(mu));
// }
// else hDen.Fill(Events->GetLeaf("Muon_pt")->GetValue(mu));
// }
// }
// TEfficiency* eff = new TEfficiency(hNum,hDen);
// eff->Draw();


//purity = # true muons passed ID/# reco muons

// TH1D hNum("num_hist","num_hist",40,0,40);
// TH1D hDen("den_hist","den_hist",40,0,40);
// int nEvt = Events->GetEntries();
// bool bReal;
// for(int i = 0; i < nEvt; i++){
// Events->GetEntry(i);
// int nMuon = Events->GetLeaf("nMuon")->GetValue();
// for(int mu = 0; mu < nMuon; mu++){
// int genIdx = Events->GetLeaf("Muon_genPartIdx")->GetValue(mu);
// int genID = Events->GetLeaf("GenPart_pdgId")->GetValue(genIdx);
// if(abs(genID) == 13) bReal = true;
// else bReal = false;
// if(Events->GetLeaf("Muon_softId")->GetValue(mu) && bReal){
// hNum.Fill(Events->GetLeaf("Muon_pt")->GetValue(mu));
// hDen.Fill(Events->GetLeaf("Muon_pt")->GetValue(mu));
// }
// else hDen.Fill(Events->GetLeaf("Muon_pt")->GetValue(mu));
// }
// }
// TEfficiency* eff1 = new TEfficiency(hNum,hDen);
// eff1->Draw();

//eff = softId
//eff1 = mvaId





		
		// if(nMediumMuons < 2) continue; 
		// if(nTightMuons < 1) continue; 
		// cout << l_var->GetValue(0) << endl;
				
		bool bReal;
		bool bPassed;
		for(int nID = 0; nID < m_IDs.size(); nID++){
			 // cout << "d" << endl;
			for(int nMu = 0; nMu < nMuon; nMu++){
				genIdx = m_tree->GetLeaf("Muon_genPartIdx")->GetValue(nMu);
		    	genID = m_tree->GetLeaf("GenPart_pdgId")->GetValue(genIdx);

		    	
				if(m_tree->GetLeaf("Muon_pt")->GetValue(nMu) < 2.) continue;

				

				if(Option == "purity"){
					if(abs(genID) == 13){
						bReal = true;
					}
					else bReal = false;
					if(nID == 0){
						bPassed = (vec_lID.at(nID)->GetValue(nMu) && m_tree->GetLeaf("Muon_looseId")->GetValue(nMu) && bReal);
					}
					else bPassed = (vec_lID.at(nID)->GetValue(nMu) && bReal);
				}
				else if(Option == "efficiency"){
					if(abs(genID) != 13) continue;
					if(nID == 0){
						bPassed = (vec_lID.at(nID)->GetValue(nMu) && m_tree->GetLeaf("Muon_looseId")->GetValue(nMu));
					}
					else bPassed = (vec_lID.at(nID)->GetValue(nMu));
				}
				
				else cout << "Invalid plot type specified: " << Option << "\n can only plot purity and efficiency"<< endl;
				
				vec_eff.at(nID)->Fill((bPassed),l_var->GetValue(nMu));

				
			}


		}
	}
	cout << endl;

	return vec_eff;
}


inline void SoftIdEfficiency::make2DPlot(TEfficiency* eff){
	gStyle->SetPalette(kRainBow);
	gStyle->SetPaintTextFormat("0.2f");
	//GET EFFICIENCIES ON PLOT
	TCanvas* cv = new TCanvas("cv","cv",800,600);
	cv->cd();
	eff->Draw("colztext");
	cv->Update();
	
	TH2* h = eff->GetPaintedHistogram();
	
	
	cv->Update();

	TString g_PlotTitle = m_samplename+" Efficiencies";
	h->GetZaxis()->SetTitle((m_IDs.at(0)+" Efficiency").c_str());
	h->SetMaximum(1.0);
	h->SetMinimum(0.0);
	h->GetXaxis()->SetTitle("Subleading Muon pT (GeV)");
	h->GetYaxis()->SetTitle("Subleading Muon #eta");
	h->SetTitle(g_PlotTitle);

	Int_t gBin;
	Double_t error;
	Int_t nBinsx = h->GetNbinsX();
	Int_t nBinsy = h->GetNbinsY();

	
	for(int i = 1; i < nBinsx+1; i++){
		for(int j = 1; j < nBinsy+1; j++){
			gBin = h->GetBin(i,j);
			// cout << "X bin #: " << i << " Y bin #: " << j << endl;
			// cout << "global bin: " << gBin << endl;
			// cout << "Bin Content: " << h->GetBinContent(gBin) << endl;
			// cout << "Bin Error: " << h->GetBinError(gBin) << endl;
			// cout << "Efficiency: " << eff->GetEfficiency(gBin) << endl;
			// cout << "Eff error up: " << eff->GetEfficiencyErrorUp(gBin) << endl;
			// cout << "Eff error low: " << eff->GetEfficiencyErrorLow(gBin) << endl;
			// cout << "\n" << endl;

			if(eff->GetEfficiencyErrorUp(gBin) >= eff->GetEfficiencyErrorLow(gBin)){
				error = eff->GetEfficiencyErrorUp(gBin);
			}
			else if(eff->GetEfficiencyErrorUp(gBin) < eff->GetEfficiencyErrorLow(gBin)){
				error = eff->GetEfficiencyErrorLow(gBin);	
			}
			h->SetBinError(gBin,error);
			
		}
	}
	cv->Update();
	h->Draw("colztextE");

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
	l.DrawLatex(0.40,0.92,g_PlotTitle);
	cv->Update();

	if(!debug){
		TString filename = ("/home/t3-ku/mlazarov/CMSSW_10_6_8/src/KUSoftMVA/MuonAnalysis/plots/"+m_outname).c_str();

		TFile* file = new TFile(filename,"RECREATE");
		cout << "file: " << filename << " created" << endl;
		file->cd();
		cv->Write();
	}
	else{
		return;
	}
}


inline void SoftIdEfficiency::makePlot(vector<TEfficiency*> effs){
	TCanvas* cv = new TCanvas("cv","cv",800,600);
	TLegend* leg = new TLegend(0.35,0.2,0.95,0.4);
	vector<TGraphAsymmErrors*> gr_effs;
	TMultiGraph* mg = new TMultiGraph();


	cv->cd();
	cv->SetGridx();
	cv->SetGridy();
	cv->SetLeftMargin(0.13);
	cv->SetRightMargin(0.04);
	cv->SetBottomMargin(0.15);
	cv->SetTopMargin(0.085);

	effs[0]->Draw("AP");
	cv->Update();
	gr_effs.push_back(effs[0]->GetPaintedGraph());
	for(int i = 1; i < effs.size(); i++){
		effs[i]->Draw("same");
		cv->Update();
		gr_effs.push_back(effs[i]->GetPaintedGraph());
	}


	cout << "# of IDs: " << gr_effs.size() << endl;
	// double fmax = -1.;
	// int imax = -1;
	// for(int i = 0; i < gr_effs.size(); i++){
	// 	if(gr_effs[i]->GetMaximum() > fmax){
	// 		fmax = gr_effs[i]->GetMaximum();
	// 		imax = i;
	// 	}
	// }
	// cout << "imax: " << endl;
	// gr_effs[imax]->Draw();

	cv->Update();
	Int_t chopcolor = gr_effs.size();
	Int_t chopmarker = gr_effs.size();

	for(int i = 0; i < gr_effs.size(); i++){
		gr_effs[i]->SetMarkerSize(1.5);
		gr_effs[i]->SetLineWidth(2);
		gr_effs[i]->GetYaxis()->SetRangeUser(0.0,1.0);
		
		if(i / chopmarker == 0){
			gr_effs[i]->SetMarkerStyle(22); //triangle
		} 
		else if(i / chopmarker == 1){
			gr_effs[i]->SetMarkerStyle(21);//square
		}
		else if(i /chopmarker == 2){
			gr_effs[i]->SetMarkerStyle(20); //circle
		}
		if(i % chopcolor == 0){
			gr_effs[i]->SetMarkerColor(kBlue-7);
			gr_effs[i]->SetLineColor(kBlue-7);
		}
		else if(i % chopcolor == 1){
			gr_effs[i]->SetMarkerColor(kRed-7);
			gr_effs[i]->SetLineColor(kRed-7);
		}
		else if(i % chopcolor == 2){
			gr_effs[i]->SetMarkerColor(kGreen-7);
			gr_effs[i]->SetLineColor(kGreen-7);
		}
		else{
			gr_effs[i]->SetMarkerColor(kCyan-7);
			gr_effs[i]->SetLineColor(kCyan-7);
		}
		if(i == 0){
			gr_effs[i]->SetTitle("Muon_softId+looseId");
		}
		// gr_effs[i]->Draw("same");
		mg->Add(gr_effs[i]);
		// cv->Update();
		leg->AddEntry(gr_effs[i]);
	}
	leg->SetTextFont(132);
	leg->SetTextSize(0.03);
	leg->SetFillColor(kWhite);
	leg->SetLineColor(kWhite);
	leg->SetShadowColor(kWhite);

	mg->Draw("AP");
	leg->Draw("SAME");
	mg->GetYaxis()->SetRangeUser(0.0,1.0);
	cv->Update();

	string g_PlotTitle = m_samplename;
	mg->GetXaxis()->SetTitle(m_var.c_str());
	mg->GetYaxis()->SetTitle("#epsilon");
	

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
	l.DrawLatex(0.40,0.92,g_PlotTitle.c_str());
	cv->Update();

	if(!debug){
		TString filename = ("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/plots/"+m_outname).c_str();

		TFile* file = new TFile(filename,"RECREATE");
		cout << "file: " << filename << " created" << endl;
		file->cd();
		cv->Write();
	}
	else{
		return;
	}
	



}
