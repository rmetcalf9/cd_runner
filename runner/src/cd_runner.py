import os
import sys
import yaml
import configValidator
import baseapp_for_restapi_backend_with_swagger
import directoryFns

print("Start of cd_runner")

globalConfigFile=baseapp_for_restapi_backend_with_swagger.readFromEnviroment(
  env=os.environ,
  envVarName="CDRUNNER_GLOBCONFIGFILE",
  defaultValue=None,
  acceptableValues=None,
  nullValueAllowed=False
)
#"example_globalConfig.yml"

expectedNumberOfParams = 1
if ((len(sys.argv) - 1) != expectedNumberOfParams):
  print("Error wrong number of paramaters - expected " + str(expectedNumberOfParams) + " got " + str(len(sys.argv) - 1))
  exit(1)

def loadConfigFile(configFile, validateFunction):
  with open(configFile, 'r') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    config = yaml.safe_load(file)

  if config is None:
    raise Exception("Nothing in config")
  validateFunction(config)
  return config

globalConfig = loadConfigFile(globalConfigFile, validateFunction=configValidator.validateGlobalConfig)
runConfig = loadConfigFile(sys.argv[1], validateFunction=configValidator.validateRunConfig)

print("Run config name: " + runConfig["name"])

runDir = directoryFns.createRunDirectoryOrFailIfItAlreadyExists(globalConfig=globalConfig)

try:
  logDir = directoryFns.createLogDirectoryForRun(globalConfig=globalConfig, runConfig=runConfig)
  checkoutGitRepository(config=config, globalConfig=globalConfig, runDir=runDir)
  runSteps = loadRunSteps(config=config)
  runnerObject = createRunnerObject(runConfig=runConfig, runSteps=runSteps, runDir=runDir, logDir=logDir)
  runnerObject.runAllSteps()
finally:
  directoryFns.cleanup(runDir=runDir)

print("End of cd_runner")
