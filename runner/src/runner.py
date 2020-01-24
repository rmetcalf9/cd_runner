import os
import stepBaseClass
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
  mainLogFile = logDir + "/output.log"
  def mainLogger(logMessage):
    print(logMessage, file=open(mainLogFile, "a"))
  return runnerObject(loggerFactory=loggerFactory, runSteps=runSteps, mainLogger=mainLogger, runConfig=runConfig)


class runnerObject():
  loggerFactory = None # fn to create a logger for each step
  steps = None
  mainLogger = None
  runConfig = None
  def __init__(self, loggerFactory, runSteps, mainLogger, runConfig):
    self.loggerFactory = loggerFactory
    self.steps = []
    self.mainLogger = mainLogger
    self.runConfig = runConfig

    for stepKey in runSteps["steps"]:
      self.steps.append(step.stepFactory(stepNum=len(self.steps)+1, stepKey=stepKey, stepData=runSteps["steps"][stepKey]))

    ##

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

  def runStep(self, step, runEnv):
    stepLogger = self.loggerFactory(step.getName())
    stepLogger("Start of step")
    stepLogger(" - Name:" + step.getName())
    stepLogger(" - Type:" + step.getType())

    try:
      step.replaceEnvVars(runEnv, stepLogger)
      self.mainLogger("Running " + step.getName() + " (" + step.getType() + ")")
      retVal = step.run(stepLogger)
    except Exception as e:
      self.mainLogger(" STEP EXCEPTION")
      stepLogger(str(e))
      return stepBaseClass.STEPOUTCOME_EXCEPTION

    stepLogger("End")
    return retVal

  def runAllSteps(self):
    if self.runConfig["requireAllStepsToBeImplemented"]:
      self.mainLogger("requireAllStepsToBeImplemented is set")
      if not self.isFullyImplemented():
        self.mainLogger("Unimplemented step types:" + str(self.getUnimplementedStepTypeList()))
        self.mainLogger("Run not started due to some unimplemented steps in the yaml")
        return

    self.mainLogger("Start of run")
    runEnv = {}
    for curStep in self.steps:
      lastStatus = self.runStep(step=curStep, runEnv=runEnv)
      if lastStatus != stepBaseClass.STEPOUTCOME_COMPLETEDSUCESSFULLY:
        if lastStatus == stepBaseClass.STEPOUTCOME_NOTIMPLEMENTED:
          self.mainLogger("Run terminated due to unimplemented step")
        else:
          self.mainLogger("Run terminated due step not completing successfully")
        return
    self.mainLogger("End of run - all steps complete")
