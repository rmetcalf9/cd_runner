import os


def checkRequiredConfigOptions(config, optionList, configname):
  for x in optionList:
    if x not in config:
      raise Exception("Invalid " + configname + " - missing " + x + " param")

def checkBooleanOptions(config, optionList, configname):
  for x in optionList:
    if not isinstance(config[x], bool):
      raise Exception("Invalid " + configname + " - " + x + " must be True or False")

def validateRunConfig(config):
  booleanOptionsList = ["requireAllStepsToBeImplemented"]
  noneOrNumberParams = ["numberOfPrevLogDirsToKeep"]

  checkRequiredConfigOptions(
    config=config,
    optionList=booleanOptionsList + noneOrNumberParams + ["name", "overwriteExistingLogs", "svnsource", "yamlfile"],
    configname="run config"
  )

  checkBooleanOptions(config=config, optionList=booleanOptionsList, configname="global config")

  for x in noneOrNumberParams:
    if not isinstance(config[x], int):
      if config[x].upper() == "NONE":
        config[x] = None
      else:
        raise Exception("Invalid run config - " + x + " must be an integer")

  if not config["yamlfile"].startswith("/"):
    raise Exception("Invalid run config - yamlfile must start with slash")


def validateGlobalConfig(config):
  booleanOptionsList = ["skipFinalCleanup"]

  checkRequiredConfigOptions(
    config=config,
    optionList=["basedir", "skipFinalCleanup"] + booleanOptionsList,
    configname="global config"
  )

  checkBooleanOptions(config=config, optionList=booleanOptionsList, configname="global config")

  if not os.path.isdir(config["basedir"]):
    raise Exception("Invalid global config - basedir does not exist " + config["basedir"])

