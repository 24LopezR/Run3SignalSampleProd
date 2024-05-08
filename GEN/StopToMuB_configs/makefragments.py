import os

#mass_points = [100, 500, 1000, 1250, 1500]
mass_points = [500]
ctau_points = [1, 10, 100, 1000, 10000, 100000, 1000000]

template = 'StopToMuB-M_XXX_ctau_YYYmm_TuneCP5_13p6TeV_pythia8_cff.py'
outdir = '../../../Configuration/Generator/python/'

for M in mass_points:
    for ct in ctau_points:

        with open(template, 'r') as f_in:
            text_in = f_in.read()
        text_out = text_in.replace('###MASS###', str(M))
        text_out = text_out.replace('###CTAU###', str(ct))

        outfilename = f'StopToMuB-M_{M}_ctau_{ct}mm_TuneCP5_13p6TeV_pythia8_cff.py'
        print(outdir+outfilename)
        with open(outdir+outfilename, 'w') as f_out:
            f_out.write(text_out)

        command = f'cmsDriver.py Configuration/Generator/python/{outfilename} --python_filename {outfilename} --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout OUTPUT --conditions 124X_mcRun3_2022_realistic_postEE_v1 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --no_exec --mc -n 989898 --nThreads 8 &>log_{M}_{ct} &'
        #print(command)
        #os.system(command)
