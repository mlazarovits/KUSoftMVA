void checkGenFlavStatus(){
	TFile* file = TFile::Open("/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent20000.root");
	TTree* tree = (TTree*)file->Get("Events");
	int nEntries = tree->GetEntries();

	TH1F* dR_hist = new TH1F("dR_hist","dR_hist",100,0,10);
	TH1F* genIdx_hist = new TH1F("genIdx_hist","genIdx_hist",100,-50,50);


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

		for(int mu = 0; mu < nMuons; mu++){
			genPartFlavor = int(tree->GetLeaf("Muon_genPartFlav")->GetValue(mu));
			if(genPartFlavor != 0) continue;
			mu_eta = tree->GetLeaf("Muon_eta")->GetValue(mu);
			mu_phi = tree->GetLeaf("Muon_phi")->GetValue(mu);

			float dR = 0;
			int genIdx;
			for(int gP = 0; gP < nGenPart; gP++){

				gp_eta = tree->GetLeaf("GenPart_eta")->GetValue(gP);
				gp_phi = tree->GetLeaf("GenPart_eta")->GetValue(gP);
				dp = std::abs(mu_phi - gp_phi);
				deltaR  = std::sqrt((mu_eta - gp_eta)*(mu_eta - gp_eta) + dp*dp);

				if(deltaR <= dR) dR = deltaR;
				else continue;
				genIdx = gP;


				
			}
			dR_hist->Fill(dR);
			genIdx_hist->Fill(genIdx);

			
		}

	}

	dR_hist->Draw();
	genIdx_hist->Draw();





}
