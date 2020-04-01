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

#include "softLepSignal.h"


using namespace std;

template<class selectortype>
void makeTrees(selectortype& selector, string ofilename){
	auto ofile = new TFile(ofilename.c_str(),"RECREATE");
	auto muonTree = selector.fChain->CloneTree(0);
	for(int i = 0;i<selector.fChain->GetEntries();i++){
		selector.fChain->GetEntry(i);
		if(selector.GenPart_statusFlags != 0 && i < 10) cout << selector.GenPart_statusFlags << endl;
		muonTree->Fill();
	}
	muonTree->Write();
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

	if ( argc < 4 ){
	    cout << "Error at Input: please specify an input file name, a list of input ROOT files and/or a folder path"; 
	    cout << " , an output filename, and a selector class name:" << endl; 
	    cout << "  Example:      ./makeTrees.x -ifile=input.root -ofile=output.root -selector=TSelector_ClassName"  << endl;
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

		if(strncmp(argv[i],"-selector",9)==0){
			sscanf(argv[i],"-selector=%s",selectorClassName);
		}
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
	string _selectorClassName(selectorClassName);
	string _ofilename(outputFileName);

	if(_selectorClassName.compare("softLepSignal") == 0){
		cout << "preparing signal tree" << endl;
		softLepSignal s(chain);
		makeTrees(s,_ofilename);
	}
	// else if(_selectorClassName.compare("softLepBackground") == 0){
	// 	cout << "preparing background tree" << endl;
	// 	softLepBackground s(chain);
	// 	makeTrees(s,_ofilename);
	// }
	else{
		cout << "Error: invalid selector class specified" << endl;
	}

	return 0;

}



	





#endif
