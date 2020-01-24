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
  joblogdir = logBase + runConfig["name"]

  logDir = joblogdir + "/" + '{0:%Y-%m-%d_%H%M}'.format(datetime.datetime.now())
  if os.path.isdir(logDir):
    if runConfig["overwriteExistingLogs"]:
      print("Found old log directory - removing")
      shutil.rmtree(logDir)
    else:
      raise Exception("A log directory already exists - aborting (Rerunning too quickly)")

  if os.path.isdir(joblogdir):
    if runConfig["numberOfPrevLogDirsToKeep"] is None:
      # We don't keep any previous logs so delete them all
      print("Removing previous log directories")
      shutil.rmtree(joblogdir)
      os.mkdir(joblogdir)
    else:
      logDirList = os.listdir(joblogdir)
      if len(logDirList) >= runConfig["numberOfPrevLogDirsToKeep"]:
        logDirList.sort()
        numDirsToDelete = len(logDirList) - (runConfig["numberOfPrevLogDirsToKeep"] - 1)
        dirsToDelete = []
        for x in logDirList:
          if len(dirsToDelete) < numDirsToDelete:
            dirsToDelete.append(joblogdir + "/" + x)
        for x in dirsToDelete:
          print("Deleting old log dir - " + x)
          shutil.rmtree(x)
  else:
    os.mkdir(joblogdir)
  os.mkdir(logDir)
  return logDir


def cleanup(runDir):
  shutil.rmtree(runDir)