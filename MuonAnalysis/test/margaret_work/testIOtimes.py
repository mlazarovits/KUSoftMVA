import uproot
import root_numpy
from time import process_time
import numpy as np
def expandList( df, columnNames):
                outDf = pd.DataFrame()
                for col in columnNames:
                        arr = pd.Series(np.array([j for i in df[col] for j in i]))
                        outDf[col] = arr
                return outDf


rnStart = process_time()
import pandas as pd
tmp = root_numpy.root2array('/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root','Events')
data = pd.DataFrame(tmp)
muonMask = data.columns.str.contains('Muon_.*')
expCols = data.loc[:,muonMask].columns
data = expandList(data,expCols)
rnStop = process_time()

urStart = process_time()
inFile = uproot.open('/home/t3-ku/janguian/CMSSW_10_6_11_patch1/src/KUSoftMVA/MuonAnalysis/test/OutputFiles/DYJetsToLL2018_MINI_numEvent100000.root')
urData = inFile['Events'].pandas.df("Muon_*")
urStop = process_time()
print("time for root_numpy:",rnStop-rnStart)
print("time for uproot:",urStop-urStart)
