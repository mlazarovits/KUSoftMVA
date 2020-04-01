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

#include "softLepSignal.h"


using namespace std;

template<class selectortype>
void makeTrees(selectortype& selector, string ofilename){
	auto ofile = new TFile(ofilename.c_str(),"RECREATE");
	auto muonTree = selector.fChain->CloneTree();
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

	//error for not enough arguments

	for(int i = 0; i < argc; i++){
		if(strncmp(argv[i], "-ifile",6)==0){
			sscanf(argv[i],"-ifile=%s", inputFileName);
			cout << argv[i] << " " << inputFileName << endl;
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
				filenames.push_back(myRootFile);
			}
		}
		inputFile->close();
		delete inputFile;
	}

	if(doFile){
		filenames.push_back(inputFileName);
	}

	TChain* chain = (TChain*)new TChain("Events"); //name of tree

	int nFile = filenames.size();
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
