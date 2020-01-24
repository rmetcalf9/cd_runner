STEPOUTCOME_COMPLETEDSUCESSFULLY=0
STEPOUTCOME_EXCEPTION=1
STEPOUTCOME_NOTIMPLEMENTED=2



class stepBaseClass():
  name=None
  type=None
  data=None
  def __init__(self, name, type, data):
    self.name = name
    self.type = type
    self.data = data

  def isImplemented(self):
    return True

  def getName(self):
    return self.name

  def getType(self):
    return self.type

  def getReplacedEnvVar(self, curVal, runEnv, num_Replaced):
    print("curVal", curVal)
    return curVal

  def replaceEnvVars(self, runEnv, stepLogger):
    num_Replaced = { "num": 0 }

    for curDataItem in self.data:
      if isinstance(self.data[curDataItem], list):
        resList = []
        for x in self.data[curDataItem]:
          resList.append(self.getReplacedEnvVar(curVal=x, runEnv=runEnv, num_Replaced=num_Replaced))
        self.data[curDataItem] = resList
      else:
        self.data[curDataItem] = self.getReplacedEnvVar(curVal=self.data[curDataItem], runEnv=runEnv, num_Replaced=num_Replaced)

    stepLogger(" - replaced " + str(num_Replaced["num"]) + " environment vars found in step yaml")
    return

  def run(self, stepLogger):
    raise Exception("Not overridden")