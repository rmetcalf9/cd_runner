import stepNotImplementedClass
import stepGitCloneClass


def stepFactory(stepNum, stepKey, stepData):
  stepName = "{:03d}".format(stepNum) + "_" + stepKey
  stepType="freestyle"
  if "type" in stepData:
    stepType = stepData["type"]
  if stepType == "git-clone":
    return stepGitCloneClass.stepGitCloneClass(stepName, stepType, stepData)
  return stepNotImplementedClass.stepNotImplementedClass(stepName, stepType, stepData)

