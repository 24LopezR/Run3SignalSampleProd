#!/bin/bash
echo "GENSIM"
cmsRun StopToMuB-M_500_ctau_100000mm_TuneCP5_13p6TeV_pythia8_GENSIM_cff.py &> log_GS.log
echo "PREMIXRAW"
cmsRun StopToMuB-M_XXX_ctau_YYYmm_TuneCP5_13p6TeV_pythia8_PREMIXRAW_cff.py &> log_PREMIXRAW.log
echo "AODSIM"
cmsRun StopToMuB-M_XXX_ctau_YYYmm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py &> log_AODSIM.log
