import stepBaseClass


class stepGitCloneClass(stepBaseClass.stepBaseClass):
  def __init__(self, name, stepType, data):
    super().__init__(name, stepType, data)

  def run(self, stepLogger):
    stepLogger("Git clone steps do nothing and pass through")
    return stepBaseClass.STEPOUTCOME_COMPLETEDSUCESSFULLY