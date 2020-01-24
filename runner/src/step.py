import stepNotImplementedClass


def stepFactory(stepNum, stepKey, stepData):
  stepName = "{:03d}".format(stepNum) + "_" + stepKey
  stepType="freestyle"
  if "type" in stepData:
    stepType = stepData["type"]
  return stepNotImplementedClass.stepNotImplementedClass(stepName, stepType)

