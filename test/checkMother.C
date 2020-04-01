void checkMother(TFile* file){
	TTree* tree = (TTree*)file->Get("Events");
	int nEntries = tree->GetEntries();

	for(i = 0;i < nEntries; i++){
		tree->GetEntry(i);
		// if(tree->GetLeaf("nMuon")->GetValue == 0) continue;
		int nGenPart = tree->GetLeaf("nGenPart");
		

		for(j = 0; j < nGenPart; j++){
			if(tree->GetLeaf("GenPart_pdgId")->GetValue(j) == 13 || tree->GetLeaf("GenPart_pdgId")->GetValue(j) == -13){
				cout << "Generator muon mother id: " << tree->GetLeaf("GenPart_genPartIdxMother")->GetValue(j) << endl;
			}
		}
	}
}