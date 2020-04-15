


To setup cmssw release:

	cmsrel CMSSW_10_6_11_patch1

	cd CMSSW_10_6_11_patch1/src
	
	git cms-addpkg PhysicsTools/PatAlgos

	cmsenv
	
	scram b

To grab the project (inside CMSSW_10_6_8/src)
either clone my repository, or fork and clone your fork

	git clone https://github.com/Jphsx/KUSoftMVA.git

To create Ntuples for MiniAOD

	cd test/
	./startMini.sh

To create Ntuples for NanoAOD

	cd test/
	./startNano.sh
	
