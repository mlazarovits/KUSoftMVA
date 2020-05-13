#include <iostream>


int plotEfficiency(string inSample, string plotType){
	TEfficiency* softId = NULL;
	TEfficiency* softIdLoose = NULL;
	TEfficiency* softMva = NULL;
	TEfficiency* model = NULL;
	vector<TEfficiency*> effs;
	string plotName;

	if(plotType == "efficiency"){
		plotName = "correct0";
	}
	else if(plotType == "purity"){
		plotName = "pure0";
	}
	else{
		cout << "Invalid plot type specified. Options are" << endl;
		cout << "efficiency     purity" << endl;
	}


	if(inSample == "dyjets"){
		softId = (TEfficiency*)TFile::Open("mva/DYfullB_SoftId.root")->Get(plotName.c_str());
		softId->SetTitle("DYJets_softId");
		
		softIdLoose = (TEfficiency*)TFile::Open("mva/DYfullB_SoftLoose.root")->Get(plotName.c_str());
		softIdLoose->SetTitle("DYJets_softId+LooseId");
		
		model = (TEfficiency*)TFile::Open("mva/model5_DY.root")->Get(plotName.c_str());
		model->SetTitle("DYJets_NN");
	}

	else if(inSample == "qcd"){
		softId = (TEfficiency*)TFile::Open("mva/QCDfullB_SoftId.root")->Get(plotName.c_str());
		softId->SetTitle("QCD_softId");
		
		softIdLoose = (TEfficiency*)TFile::Open("mva/QCDfullB_SoftLoose.root")->Get(plotName.c_str());
		softIdLoose->SetTitle("QCD_softId+LooseId");
		
		model = (TEfficiency*)TFile::Open("mva/model5_QCD.root")->Get(plotName.c_str());
		model->SetTitle("QCD_NN");
	}

	else if(inSample == "ttjets"){
		softId = (TEfficiency*)TFile::Open("mva/TTfullB_SoftId.root")->Get(plotName.c_str());
		softId->SetTitle("TTJets_softId");
		
		softIdLoose = (TEfficiency*)TFile::Open("mva/TTfullB_SoftLoose.root")->Get(plotName.c_str());
		softIdLoose->SetTitle("TTJets_softId+LooseId");
		
		softMva = (TEfficiency*)TFile::Open("mva/TTfullB_SoftMva.root")->Get(plotName.c_str());
		softMva->SetTitle("TTJets_softMva");
		
		model = (TEfficiency*)TFile::Open("mva/model5_TT.root")->Get(plotName.c_str());
		model->SetTitle("TTJets_NN");
	}

	else if(inSample == "all"){
		softId = (TEfficiency*)TFile::Open("mva/CombB_SoftId.root")->Get(plotName.c_str());
		softId->SetTitle("combSamples_softId");
		
		softIdLoose = (TEfficiency*)TFile::Open("mva/CombB_SoftLoose.root")->Get(plotName.c_str());
		softIdLoose->SetTitle("combSamples_softId+LooseId");

		model = (TEfficiency*)TFile::Open("mva/model5_COMB.root")->Get(plotName.c_str());
		model->SetTitle("combSamples_NN");
	}
	else{
		cout << "Invalid sample specified. Options are:" << endl;
		cout << "dyjets  qcd   ttjets   all" << endl;
		return 0;
	}

	effs.push_back(softId);
	effs.push_back(softIdLoose);
	effs.push_back(softMva);
	effs.push_back(model);





	TCanvas* cv = new TCanvas("cv","cv",800,600);
	TLegend* leg = new TLegend(0.65,0.2,0.95,0.4);
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
		if(effs[i]){
			effs[i]->Draw("same");
			cv->Update();
			gr_effs.push_back(effs[i]->GetPaintedGraph());
		}
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

	string g_PlotTitle = inSample+" Efficiency";
	mg->GetXaxis()->SetTitle("Muon pT (GeV)");
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


	TString filename = ("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/margaret_work/mva/plots/"+inSample+"_efficiencies.root").c_str();

	TFile* file = new TFile(filename,"RECREATE");
	cout << "file: " << filename << " created" << endl;
	file->cd();
	cv->Write();
	
	return 0;
	

}