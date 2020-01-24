import stepBaseClass


class stepNotImplementedClass(stepBaseClass.stepBaseClass):
  def __init__(self, name, stepType):
    super().__init__(name, stepType)

  # function not needed as base class defaults to true
  def isImplemented(self):
    return False

  def run(self, stepLogger):
    stepLogger("Step type not implemented")
    return stepBaseClass.STEPOUTCOME_NOTIMPLEMENTED