def prepData(filename):
	data = root_numpy.root2array(gPath+filename,treeName)
	data = pd.DataFrame(data)
	#make gen pdg ID labels for reco muons
	#-999 if unmatched
	pdgIds = [-999 if mu == -1 else data['GenPart_pdgId'][i][mu] for i, idxs in enumerate(data['Muon_genPartIdx']) for j, mu in enumerate(idxs)]
	pdgIds = np.array(pdgIds)

	#make jet btag CSVV2 column
	btags = [-999 if mu == -1 else data['Jet_btagCSVV2'][i][mu] for i, idxs in enumerate(data['Muon_jetIdx']) for j, mu in enumerate(idxs)]
	btags = np.array(btags)


	#get rid of 0 muon events
	data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])

	#expand the list so each row is a muon (not an event)
	muonMask = data.columns.str.contains('Muon_.*')
	expCols = data.loc[:,muonMask].columns
	data = expandList(data, expCols)

	#add in gen pgdIds and jet btags of reco muons
	data['Muon_genPdgId'] = pdgIds
	data['Jet_btagCSVV2'] = btags

	#drop muons with pt < 2
	data = data.drop([i for i, pt in enumerate(data['Muon_pt']) if pt < 2])
	return data