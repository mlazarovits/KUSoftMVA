


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
	

if no conda environment has been set up

	cp /home/t3-ku/mlazarov/softwareBuilds/py3_pandsNroot.yml .
	conda env create -f py3_pandsNroot.yml
this `.yml` file has almost all the dependencies needed (except uproot, see below)


activate conda env

	conda activate py3_pandas_root
make sure all dependencied are installed
	
	conda list uproot
	conda list sklearn
	conda list keras
if uproot is not installed

	conda install -c conda-forge uproot
else

	conda install [dependency]

run script

	cd KUSoftMVA/MuonAnalysis
	./scripts/machinelearn.sh

