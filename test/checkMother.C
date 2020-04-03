void checkMother(){
	TFile* file = TFile::Open("OutputFiles/DYJetsToLL2018_NANO.root");
	TTree* tree = (TTree*)file->Get("Events");
	int nEntries = tree->GetEntries();

	for(int i = 0;i < 100; i++){
		tree->GetEntry(i);
		// if(tree->GetLeaf("nMuon")->GetValue == 0) continue;
		
		
		int nGenPart = tree->GetLeaf("nGenPart")->GetValue();
		
		int nMu = 0;
		for(int j = 0; j < nGenPart; j++){
			if(tree->GetLeaf("GenPart_pdgId")->GetValue(j) != 13 || tree->GetLeaf("GenPart_pdgId")->GetValue(j) != -13) continue;
			if(tree->GetLeaf("GenPart_genPartIdxMother")->GetValue() != 0) continue;
			cout << "event: " << i << endl;
			cout << "Generator pdg id: " << tree->GetLeaf("GenPart_pdgId")->GetValue(j) << endl;
			cout << "Generator muon mother id: " << tree->GetLeaf("GenPart_genPartIdxMother")->GetValue(j) << endl;
			nMu += 1;
		}
		if(nMu != 0) cout << "nMuons: " << tree->GetLeaf("nMuon")->GetValue();



	}
}