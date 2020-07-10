using namespace std;
void makeTChain(string inSample, string trainTest){
TChain* chain = new TChain("Events");
TFile* ofile = new TFile((trainTest+"_"+inSample+".root").c_str(),"RECREATE");

int nStart;
int nStop;
string pathName;
if(inSample == "dyjets") {
	pathName = "/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/jsingera/MVA/DYJetsToLL_M-50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/MVA_DY2018/200512_144407/0000/";
	if(trainTest == "Train"){
		nStart = 1;
		nStop = 70;
	}
	else if(trainTest == "Test"){
		nStart = 71;
		nStop = 210;
	}
}
else if(inSample == "ttjets"){
	pathName = "/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/jsingera/MVA/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/MVA_TT2018/200512_182436/0000/";
        if(trainTest == "Train"){
                nStart = 1;
                nStop = 10;
        }
        else if(trainTest == "Test"){
                nStart = 21;
                nStop = 25;
        }
}

else if(inSample == "qcd"){
        pathName = "/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/jsingera/MVA/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/MVA_QCD2018/200513_003848/0000/";
	if(trainTest == "Train"){
                nStart = 1;
                nStop = 10;
        }
        else if(trainTest == "Test"){
                nStart = 21;
                nStop = 28;
        }
}
int nFile = 0;
for(int i = nStart; i < nStop; i++){
	if(gSystem->AccessPathName((pathName+"defaultout_"+to_string(i)+".root").c_str())) continue;
	else chain->AddFile((pathName+"defaultout_"+to_string(i)+".root").c_str());
nFile += 1;

}
cout << nFile << " files" << endl;



//cout << "b" << endl;
chain->CloneTree(-1,"fast");
//cout << "c" << endl;
ofile->Write();



}
