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
	// auto pionTree = selector.fChain->CloneTree(0);

	float deltaR_muGenPart = 0.05;
	for(int i = 0;i<selector.fChain->GetEntries();i++){
		selector.fChain->GetEntry(i);

		int nGenPart = selector.nGenPart;
		int nMu = selector.nMuon;

		

		if(nMu < 1) continue; //need at least 1 reco mu
		int nPmus;
		int nNPmus;
		int npis;
		int nes;
		int nothers;


		for(int mu = 0; mu < nMu; mu++){
			bool isMu = false;
			bool isPion = false;
			bool ise = false;
			bool isPrompt = false;
			bool isNotPrompt = false;

			nPmus = 0;
			nNPmus = 0;
			npis = 0;
			nes = 0;
			nothers = 0;

			for(int gp = 0; gp < nGenPart; gp++){
				float mu_eta = selector.Muon_eta[mu];
				float gp_eta = selector.GenPart_eta[gp];
				float mu_phi = selector.Muon_phi[mu];
				float gp_phi = selector.GenPart_phi[gp];


				float dp = std::abs(mu_phi - gp_phi);
				float deltaR  = std::sqrt((mu_eta - gp_eta)*(mu_eta - gp_eta) + dp*dp);

				if(deltaR <= deltaR_muGenPart){
					int pdgId = abs(selector.GenPart_pdgId[gp]);
					int motherIdx = abs(selector.GenPart_genPartIdxMother[gp]);

					isMu = pdgId == 13;
					isPion = pdgId == 211;
					ise = pdgId == 11;

					isPrompt = selector.GenPart_pdgId[motherIdx] == 23 || selector.GenPart_pdgId[motherIdx] == 24; //coming from Z or W
					isNotPrompt = selector.GenPart_pdgId[motherIdx] == 211; //coming from pions

					if(isMu && isPrompt) nPmus++;
					if(isMu && isNotPrompt) nNPmus++;
					if(ise) nes++;
					if(isPion) npis++; 
					else nothers++;

				}

			}
		}
		// if(nPmus > 1){
			cout << "muontree filled" << endl;
			muonTree->Fill();
		// }
		// else if(npis > 1) pionTree->Fill();
	}
	muonTree->Write();
	// pionTree->Write();
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
