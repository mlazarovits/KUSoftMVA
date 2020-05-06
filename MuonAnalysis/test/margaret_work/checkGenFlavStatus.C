void checkGenFlavStatus(){
	TFile* file = TFile::Open("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent200.root");
	TTree* tree = (TTree*)file->Get("Events");
	int nEntries = tree->GetEntries();

	TH1F* dR_hist = new TH1F("dR_hist","dR_hist",100,0,10);
	// TH1F* genIdx_hist = new TH1F("genIdx_hist","genIdx_hist",100,-50,50);
	TH2F* dRdPt_hist = new TH2F("dRdPt_hist","dRdPt_hist",10,0,10,11,0,1.1);

	std::vector<float> dRs;
	std::vector<float> dPtRels;

	for(int i = 0;i < nEntries; i++){
		tree->GetEntry(i);
		// if(tree->GetLeaf("nMuon")->GetValue == 0) continue;
		// cout << "event: " << i << endl;
		int nGenPart = tree->GetLeaf("nGenPart")->GetValue();
		int nMuons = tree->GetLeaf("nMuon")->GetValue();

		int idx;
		int nPis = 0;
		int nMu = 0;
		int genPartFlavor;
		float mu_eta;
		float mu_phi;
		float gp_eta;
		float gp_phi;
		float deltaR;
		float dp;
		float deltaPt;
		float deltaPtRel;
		float dR;
		// int genIdx = -999;
		float dPtRel;
		float dPt;

		

		if(nMuons < 1) continue;

		for(int mu = 0; mu < nMuons; mu++){
			genPartFlavor = int(tree->GetLeaf("Muon_genPartFlav")->GetValue(mu));
			if(genPartFlavor != 0) continue;
			mu_eta = tree->GetLeaf("Muon_eta")->GetValue(mu);
			mu_phi = tree->GetLeaf("Muon_phi")->GetValue(mu);

		


			for(int gP = 0; gP < nGenPart; gP++){

				gp_eta = tree->GetLeaf("GenPart_eta")->GetValue(gP);
				gp_phi = tree->GetLeaf("GenPart_eta")->GetValue(gP);
				dp = std::abs(mu_phi - gp_phi);
				deltaR  = std::sqrt((mu_eta - gp_eta)*(mu_eta - gp_eta) + dp*dp);

				deltaPt = std::abs(tree->GetLeaf("GenPart_pt")->GetValue(gP) - tree->GetLeaf("Muon_pt")->GetValue(mu));
				deltaPtRel = deltaPt/tree->GetLeaf("Muon_pt")->GetValue(mu);

				dRs.push_back(deltaR);
				dPtRels.push_back(deltaPtRel);

				

				
			}

			dR_hist->Fill(*min_element(dRs.begin(),dRs.end()));
			dRdPt_hist->Fill(*min_element(dRs.begin(),dRs.end()),*min_element(dPtRels.begin(),dPtRels.end()));
			dRs.clear();
			dPtRels.clear();
			
		}


	}
	cout << "# dR entries: " << dR_hist->Integral() << endl;
	cout << "# dRdPt_hist entries: " << dRdPt_hist->Integral() << endl; 
	TCanvas* cv = new TCanvas();
	TCanvas* cv2 = new TCanvas();

	cv->cd();
	dRdPt_hist->GetYaxis()->SetTitle("delta pT rel");
	dRdPt_hist->GetXaxis()->SetTitle("dR");
	dRdPt_hist->Draw("colz");
	
	cv2->cd();
	dR_hist->GetXaxis()->SetTitle("dR");
	dR_hist->Draw();
	







}
