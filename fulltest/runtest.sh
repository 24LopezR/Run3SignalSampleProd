#!/bin/bash
cd StopToMuB/
for cfg in *; do (echo $cfg; cmsRun $cfg &> log_$cfg.log); done
cd ..
cd SMuonToMuGravitino/
for cfg in *; do (echo $cfg; cmsRun $cfg &> log_$cfg.log); done
