import root_numpy
import numpy as np
import pandas as pd

#expand list in terms of muon - takes a long time
def expandList(df, columnNames):
	outDf = pd.DataFrame()
	for col in columnNames:
		arr = pd.Series(np.array([j for i in df[col] for j in i]))
		outDf[col] = arr
	return outDf


def makeData(filename,definedIds):
	treeName = 'Events'
	gPath = '/home/t3-ku/mlazarov/softMVA/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/'
	data = root_numpy.root2array(gPath+filename+'.root',treeName)
	data = pd.DataFrame(data)
	#make gen pdg ID labels for reco muons
	#-999 if unmatched
	pdgIds = np.array([-999 if mu == -1 else data['GenPart_pdgId'][i][mu] for i, idxs in enumerate(data['Muon_genPartIdx']) for j, mu in enumerate(idxs)])
	#get rid of 0 muon events
	data = data.drop([i for i, nMu in enumerate(data['nMuon']) if nMu == 0])
	#expand the list so each row is a muon (not an event)
	muonMask = data.columns.str.contains('Muon_.*')
	expCols = data.loc[:,muonMask].columns
	data = expandList(data, expCols)
	#add in gen pgdIds and jet btags of reco muons
	data['Muon_genPdgId'] = pdgIds
	#drop muons with pt < 2
	data = data.drop([i for i, pt in enumerate(data['Muon_pt']) if pt < 2])
	data = data.reset_index()
	#drop muons matched to anything not in our defined classes: 13, 221, 321, 2211, or 999
	data = data.drop([i for i, ID in enumerate(data['Muon_genPdgId']) if abs(ID) not in definedIds])
	data = data.reset_index()
	# df = df.drop([i for i, ID in enumerate(df['genPdgId']) if abs(ID) not in definedIds])
	data.to_csv(filename+'.csv')
	return data


