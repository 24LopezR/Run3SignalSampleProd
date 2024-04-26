#!/bin/bash
echo "GENSIM"
cmsRun HTo2LongLivedTo4mu_MH-1600_MFF-50_CTau-100000mm_TuneCP5_13p6TeV_pythia8_GENSIM_cff.py &> log_GS.log
echo "PREMIXRAW"
cmsRun HTo2LongLivedTo4mu_TuneCP5_13p6TeV_pythia8_PREMIXRAW_cff.py &> log_PREMIXRAW.log
echo "AODSIM"
cmsRun HTo2LongLivedTo4mu_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py.py &> log_AODSIM.log
