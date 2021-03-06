#! /bin/bash

export X509_USER_PROXY="~/xrootdCert"

if test -z "${_CONDOR_SCRATCH_DIR}"; then
    export _CONDOR_SCRATCH_DIR=.
fi

MUPRO=/net/hidsk0001/d00/scratch/mojoe137/CMSSW_4_4_5_patch1/src/Analyzers/UPCTriggerAnalyzer/condor/upcMuonCondor/
cd $MUPRO
eval `scram runtime -sh`

cd ${_CONDOR_SCRATCH_DIR}
cmsRun /net/hidsk0001/d00/scratch/mojoe137/CMSSW_4_4_5_patch1/src/Analyzers/UPCTriggerAnalyzer/test/upcTreezCondorWDiTrk_cfg.py $MUPRO$1 ${_CONDOR_SCRATCH_DIR}/$2
hadoop fs -rm /cms/store/user/pkenny/UPCData/UPCTrees/$2
hadoop fs -put ${_CONDOR_SCRATCH_DIR}/$2 /cms/store/user/pkenny/UPCData/UPCTrees/
