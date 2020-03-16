


To setup cmssw release:

	cmsrel CMSSW_10_6_8

	cd CMSSW_10_6_8/src
	
	cmsenv
	
	scram b

To grab the project (inside CMSSW_10_6_8/src)
either clone mine repository, or fork and clone your fork

	git clone https://github.com/Jphsx/KUSoftMVA.git

To create Ntuples for MiniAOD

	cd test/
	./startMini.sh

To create Ntuples for NanoAOD

	cd test/
	./startNano.sh
	
