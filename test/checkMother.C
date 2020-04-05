void checkMother(){
	TFile* file = TFile::Open("OutputFiles/DYJetsToLL2018_NANO.root");
	TTree* tree = (TTree*)file->Get("Events");
	int nEntries = tree->GetEntries();

	for(int i = 0;i < 100; i++){
		tree->GetEntry(i);
		// if(tree->GetLeaf("nMuon")->GetValue == 0) continue;
		cout << "event: " << i << endl;
		int nGenPart = tree->GetLeaf("nGenPart")->GetValue();
		int idx;
		int nPis = 0;
		
		int nMu = 0;
		for(int j = 0; j < nGenPart; j++){
			if(fabs(tree->GetLeaf("GenPart_pdgId")->GetValue(j)) == 211) nPis+=1;
			if(fabs(tree->GetLeaf("GenPart_pdgId")->GetValue(j)) != 13) continue;
			idx = tree->GetLeaf("GenPart_genPartIdxMother")->GetValue(j);
			// if(tree->GetLeaf("GenPart_genPartIdxMother")->GetValue() != 0) continue;
			
			cout << "Generator pdg id: " << tree->GetLeaf("GenPart_pdgId")->GetValue(j) << endl;
			cout << "Generator muon mother id: " << tree->GetLeaf("GenPart_genPartIdxMother")->GetValue(idx) << endl;
			nMu += 1;

		}
		cout << "nGenMu " << nMu << endl;
		cout << "nGenPis " << nPis << endl;
		if(nMu > 0) cout << "nRecoMus: " << tree->GetLeaf("nMuon")->GetValue() << "\n" << endl;


	}
}
