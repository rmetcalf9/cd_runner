import os
import step

def createRunnerObject(runConfig, runSteps, runDir, logDir):
  def loggerFactory(stepName):
    stepLogDir = logDir + "/" + stepName
    if not os.path.isdir(stepLogDir):
      os.mkdir(stepLogDir)
    logFile = stepLogDir + "/output.log"
    def makeLog(logMessage):
      print(logMessage, file=open(logFile, "a"))
    return makeLog
  return runnerObject(loggerFactory=loggerFactory, runSteps=runSteps)


class runnerObject():
  loggerFactory = None # fn to create a logger for each step
  steps = None
  def __init__(self, loggerFactory, runSteps):
    self.loggerFactory = loggerFactory
    self.steps = []

    for stepKey in runSteps["steps"]:
      self.steps.append(step.stepFactory(stepNum=len(self.steps)+1, stepKey=stepKey, stepData=runSteps["steps"][stepKey]))

    ## self.loggerFactory("000_Test")("Test log message")

  def isFullyImplemented(self):
    for x in self.steps:
      if not x.isImplemented():
        return False
    return True

  def getUnimplementedStepTypeList(self):
    unimpStepTypes = {}
    for x in self.steps:
      if not x.isImplemented():
        if x.getType() not in unimpStepTypes:
          unimpStepTypes[x.getType()] = []
        unimpStepTypes[x.getType()].append(x)
    return list(unimpStepTypes.keys())
