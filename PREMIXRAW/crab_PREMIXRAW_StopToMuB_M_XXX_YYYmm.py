from CRABClient.UserUtilities import config
config = config()

MASS = '###MASS###'
CTAU = '###CTAU###'

config.General.requestName = f'StopToMuB_M_{MASS}_{CTAU}mm_PREMIXRAW_v0'
config.General.workArea = '/eos/user/r/rlopezru/DisplacedDimuons/StopToMuB_CMSSW_12_4_20/PREMIXRAW/crabprojects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = f'StopToMuB-M_XXX_ctau_YYYmm_TuneCP5_13p6TeV_pythia8_PREMIXRAW_cff.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '###INPUTDATASET###'
config.Data.outputDatasetTag = 'PREMIXRAW'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_*","T2_*"]
config.Site.storageSite = 'T2_ES_IFCA'
