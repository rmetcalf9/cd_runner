import os


def validateRunConfig(config):
  requiredParams = ["name", "overwriteExistingLogs", "numberOfPrevLogDirsToKeep"]
  for x in requiredParams:
    if x not in config:
      raise Exception("Invalid run config - missing " + x + " param")

  noneOrNumberParams = ["numberOfPrevLogDirsToKeep"]
  for x in noneOrNumberParams:
    if config[x].upper() == "NONE":
      config[x] = None
    else:
      config[x] = int(config[x])

def validateGlobalConfig(config):
  if "basedir" not in config:
    raise Exception("Invalid global config - missing basedir param")
  if not os.path.isdir(config["basedir"]):
    raise Exception("Invalid global config - basedir does not exist " + config["basedir"])

