#ifndef MAKETREES
#define MAKETREES

//make signal (soft prompt muons - truth matched) and background (soft NP muons) trees
#include <iostream>
#include <fstream>
#include <sstream>
#include <ostream>
#include <istream>
#include <stdio.h>
#include <dirent.h>
#include <vector>

#include "TFile.h"
#include "TBranch.h"
#include "TTree.h"
#include "TLeaf.h"
#include <TSystem.h>

#include "softLepMINI.h"


using namespace std;

template<class selectortype>
void makeTrees2(selectortype& selector, string ofilename){
	auto ofile = new TFile(ofilename.c_str(),"RECREATE");
	auto PmuonTree = selector.fChain->CloneTree(0);
	auto bTree = selector.fChain->CloneTree(0);
	auto tauTree = selector.fChain->CloneTree(0);
	auto othersTree = selector.fChain->CloneTree(0);

	// float deltaR_muGenPart = 0.05;
	int nPmus;
	int nNPmus;
	int nBs;
	int nTaus;
	int nothers;

	for(int i = 0;i<selector.fChain->GetEntries();i++){
		selector.fChain->GetEntry(i);

		int nGenPart = selector.nGenPart;
		int nMu = selector.nMuon;


		if(nMu < 1) continue; //need at least 1 reco mu
		

		

			nPmus = 0;
			nNPmus = 0;
			nBs = 0;
			nTaus = 0;
			nothers = 0;
			// if(i < 10) cout << "mu idx " << mu << endl;


		for(int mu = 0; mu < nMu; mu++){

			
			if(selector.Muon_genPartFlav[mu] == 0) continue; //don't fill tree with unmatched muons
			else if(selector.Muon_genPartFlav[mu] == 1) nPmus += 1;
			else if(selector.Muon_genPartFlav[mu] == 15) nTaus += 1;
			else if(selector.Muon_genPartFlav[mu] == 4) nBs += 1;
			else nothers += 1;

		}



		if(nPmus > 1) PmuonTree->Fill(); //prompt muons
		else if(nTaus > 1) tauTree->Fill(); //muons from taus
		else if(nBs > 1) bTree->Fill(); //muons from b's
		else if(nothers > 1) othersTree->Fill(); //other


	}

	PmuonTree->SetName("PromptMuons");
	tauTree->SetName("TauOrigin");
	bTree->SetName("bJetOrigin");
	othersTree->SetName("Others");

	PmuonTree->Write();
	tauTree->Write();
	bTree->Write();
	othersTree->Write();


	ofile->Write();
	ofile->Close();

}


int main(int argc, char* argv[]){
	char inputFileName[400];
	char outputFileName[400];
	char selectorClassName[400];
	char inputListName[400];

	bool doFile = false;
	bool doList = false;

	if ( argc < 3 ){
	    cout << "Error at Input: please specify an input file name, a list of input ROOT files and/or a folder path"; 
	    cout << " , an output filename, and a selector class name:" << endl; 
	    cout << "  Example:      ./makeTrees.x -ifile=MINIfile.root -ofile=output.root"  << endl;
	    // cout << "  FOR CONDOR USE ONLY Example:      ./MakeReducedNtuple_NANO.x -ilist=input.list -ofile=output.root -selector=TSelector_ClassName"  << endl;
	    // cout << "  Example:      ./MakeReducedNtuple_NANO.x -ifold=folder_path -ofile=output.root   -selector=TSelector_ClassName" << endl;
	    // cout << " additional tags for object based reduced tree: -selector=TSelector_ClassName "<<endl; 
	    return 1;
	}

	for(int i = 0; i < argc; i++){
		if(strncmp(argv[i], "-ifile",6)==0){
			sscanf(argv[i],"-ifile=%s", inputFileName);
			doFile = true;
		}

		if(strncmp(argv[i],"-ilist",6)==0){
			sscanf(argv[i],"-ilist=%s",inputListName);
			doList = true;
		}

		if(strncmp(argv[i],"-ofile",6)==0){
			sscanf(argv[i],"-ofile=%s",outputFileName);
		}

		// if(strncmp(argv[i],"-selector",9)==0){
		// 	sscanf(argv[i],"-selector=%s",selectorClassName);
		// }
	}

	gROOT->ProcessLine("#include <vector>");

	vector<string> filenames;

	char Buffer[500];
	char myRootFile[2000];

	if(doList){
		ifstream *inputFile = new ifstream(inputListName);
		while( !(inputFile->eof()) ){
			inputFile->getline(Buffer,500);
			if(! strstr(Buffer,"#") && !(strspn(Buffer," ") == strlen(Buffer))){
				sscanf(Buffer,"%s",myRootFile);
				if(!(gSystem->AccessPathName(myRootFile))){
					filenames.push_back(myRootFile);
				}
				else if(gSystem->AccessPathName(myRootFile)){
					cout << "Error: file " << myRootFile << " doesn't exist" << endl;
				}
			}
		}
		inputFile->close();
		delete inputFile;
	}

	if(doFile){
		if(!(gSystem->AccessPathName(inputFileName))){
			filenames.push_back(inputFileName);
		}
		else if(gSystem->AccessPathName(inputFileName)){
			cout << "Error: file " << inputFileName << " doesn't exist" << endl;
		}
	}

	TChain* chain = (TChain*)new TChain("Events"); //name of tree

	int nFile = filenames.size();
	if(nFile < 1){
		cout << "no valid files specified" << endl;
		return 2;
	}
	for(int i = 0; i < nFile; i++){
		chain->Add(filenames[i].c_str());
		cout << "Adding file " << filenames[i] << endl;
	}

	//convert char arrays to strings
	// string _selectorClassName(selectorClassName);
	string _ofilename(outputFileName);

	// if(_selectorClassName.compare("softLepMINI") == 0){
	cout << "preparing all trees" << endl;
	softLepMINI s(chain);
	makeTrees2(s,_ofilename);
	// }
	// else if(_selectorClassName.compare("softLepBackground") == 0){
	// 	cout << "preparing background tree" << endl;
	// 	softLepBackground s(chain);
	// 	makeTrees(s,_ofilename);
	// }
	// else{
	// 	cout << "Error: invalid selector class specified" << endl;
	// }

	return 0;

}



	





#endif
