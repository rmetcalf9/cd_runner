import os


def validateRunConfig(config):
  if "name" not in config:
    raise Exception("Invalid run config - missing name param")

def validateGlobalConfig(config):
  if "basedir" not in config:
    raise Exception("Invalid global config - missing basedir param")
  if not os.path.isdir(config["basedir"]):
    raise Exception("Invalid global config - basedir does not exist " + config["basedir"])

