import numpy as np
import sys
import uproot

file = sys.arvg[1]

events = uproot.open(file)['Events']

promptGenPdgIds = []
bGenPdgIds = []
tauGenPdgIds = []
uGenPdgIds = []


memChunks = [i for i in events.mempartitions(1e8,entrystart=0,entrystop=1e6)] #read 100 MB at a time, max 1mil events

for mem in memChunks:
	memStart = mem[0]
	memStop = mem[1]
	muonGenPartFlav = events.array('Muon_genPartFlav',entrystart=memStart,entrystop=memStop)
	genData = events.array('GenPart_pdgId',entrystart=memStart,entrystop=memStop)
	dataMu = events.array('Muon_genPartIdx',entrystart=memStart,entrystop=memStop)
	genDataMom = events.array('GenPart_genPartMotherIdx',entrystart=memStart,entrystop=memStop)
	for i, idxs in enumerate(dataMu):
		if len(idxs) < 1: continue
		for j, mu in enumerate(idxs):
			if muonGenPartFlav[i][j] == 1:
				promptGenPdgIds.append(genData[i][genDataMom[i][mu]])
			elif muonGenPartFlav[i][j] == 5:
				bGenPdgIds.append(genData[i][genDataMom[i][mu]])
			elif muonGenPartFlav[i][j] == 15:
				tauGenPdgIds.append(genData[i][genDataMom[i][mu]])
			elif muonGenPartFlav[i][j] == 0:
				uGenPdgIds.append(genData[i][genDataMom[i][mu]])

promptGenPdgIds = np.array(promptGenPdgIds)
bGenPdgIds = np.array(bGenPdgIds)
tauGenPdgIds = np.array(tauGenPdgIds)
uGenPdgIds = np.array(uGenPdgIds)

print('promptPdgIds:',np.unique(promptGenPdgIds))
print('bGenPdgIds:',np.unique(bGenPdgIds))
print('tauGenPdgIds:',np.unique(tauGenPdgIds))
print('uGenPdgIds:',np.unique(uGenPdgIds))








