


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
this `.yml` file has almost all the dependencies needed (see below for one-time installations for some dependencies)
before moving on to the next step, do NOT create a `cmsenv` within a cmssw release to run the `machinelearn.sh` script. this will set confounding environment variables. the `.yml` file has all the dependencies needed to run this script. if a `cmsenv` has been set, open a new terminal window to unset these environment variables


activate conda env

	conda activate py3_pandas_root
make sure all dependencied are installed
	
	conda list uproot
	conda list sklearn
	conda list keras
if uproot is not installed

	conda install -c conda-forge uproot
else do the following for all other dependencies

	conda install [dependency]

run script

	cd KUSoftMVA/MuonAnalysis
	./scripts/machinelearn.sh

