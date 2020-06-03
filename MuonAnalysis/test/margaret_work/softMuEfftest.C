void dyMinitest(){
	TFile* file = TFile::Open("OutputFiles/DYJetsToLL2018_MINI_numEvent10000.root");
	TEfficiency* eff = new TEfficiency("effSoft","effSoft",40,0,20);
	TTreeReader nanoReader("Events",file);

	TTreeReaderValue< vector<pat::Muon> > PATmuons(nanoReader,"patMuons_slimmedMuons__PAT.obj")
	TTreeReaderValue< Int_t  > nRecoPV("recoVertexs_offlineSlimmedPrimaryVertices__PAT.obj_");


	//Loop over all samples in tree
	bool isSoft;
	while(nanoReader.Next()){
		nMus = (*PATmuons).size();
		vector<pat::Muon> mus = (*PATmuons);

		if(nMus>=1){
			isSoft = mus.isSoft;

		}
	}




}