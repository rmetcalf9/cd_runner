STEPOUTCOME_COMPLETEDSUCESSFULLY=0
STEPOUTCOME_EXCEPTION=1
STEPOUTCOME_NOTIMPLEMENTED=2



class stepBaseClass():
  name=None
  type=None
  def __init__(self, name, type):
    self.name = name
    self.type = type

  def isImplemented(self):
    return True

  def getName(self):
    return self.name

  def getType(self):
    return self.type

  def replaceEnvVars(self, runEnv, stepLogger):
    return

  def run(self, stepLogger):
    raise Exception("Not overridden")