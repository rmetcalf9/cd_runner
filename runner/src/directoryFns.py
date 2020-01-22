import os
import shutil
import datetime

def createRunDirectoryOrFailIfItAlreadyExists(globalConfig):
  runDir =  globalConfig["basedir"] + "/currentrun"
  if os.path.isdir(runDir):
    raise Exception("A current run directory already exists - aborting")
  os.mkdir(runDir)
  return runDir

def createLogDirectoryForRun(globalConfig, runConfig):
  logBase = globalConfig["basedir"] + "/logs/"
  if not os.path.isdir(logBase):
    os.mkdir(logBase)
  logDir = logBase + runConfig["name"] + "_" + '{0:%Y-%m-%d_%H%M}'.format(datetime.datetime.now())
  if os.path.isdir(logDir):
    raise Exception("A log directory already exists - aborting (Rerunning too quickly)")
  os.mkdir(logDir)
  return logDir


def cleanup(runDir):
  shutil.rmtree(runDir)