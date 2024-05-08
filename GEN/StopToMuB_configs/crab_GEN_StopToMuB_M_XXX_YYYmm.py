from CRABClient.UserUtilities import config
config = config()

MASS = '###MASS###'
CTAU = '###CTAU###'

config.General.requestName = f'StopToMuB_M_{MASS}_{CTAU}mm_v0'
config.General.workArea = '/eos/user/r/rlopezru/DisplacedDimuons/StopToMuB_CMSSW_12_4_20/GEN/crabprojects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = f'cmsRunconfigs/StopToMuB-M_{MASS}_ctau_{CTAU}mm_TuneCP5_13p6TeV_pythia8_cff.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = f'StopToMuB_M_{MASS}_{CTAU}mm_13p6TeV_2022MC_CMSSW_12_4_20_v0'
config.Data.outputDatasetTag = 'GENSIM'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/rlopezru/'
config.Data.publication = True

config.Site.storageSite = 'T2_ES_IFCA'
