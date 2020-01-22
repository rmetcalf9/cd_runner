import os
import shutil


def createRunDirectoryOrFailIfItAlreadyExists(globalConfig):
  runDir =  globalConfig["basedir"] + "/currentrun"
  if os.path.isdir(runDir):
    raise Exception("A current run directory already exists - aborting")
  os.mkdir(runDir)
  return runDir

def cleanup(runDir):
  shutil.rmtree(runDir)