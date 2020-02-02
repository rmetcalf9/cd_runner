STEPOUTCOME_COMPLETEDSUCESSFULLY=0
STEPOUTCOME_EXCEPTION=1
STEPOUTCOME_NOTIMPLEMENTED=2

class replacementToken:
  str=None
  def __init__(self, str):
    self.str = str.strip()

  def getOutput(self):
    return {
      "newVal": "__TODO__" + self.str + "_",
      "replaced": True
    }

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

  def getReplacedEnvVar(self, curVal, runEnv):
    print("curVal", curVal)

    totalReplaced = 0
    replacementMade = True

    # tokenisedArray is a list of string and replacmentToken objects
    tokenisedArray = []

    remainingStringToScan = curVal
    firstRepPos = remainingStringToScan.find("${{")
    while (firstRepPos != -1):
      remaingStringPart = remainingStringToScan[(firstRepPos+3):]
      closeBracketInRemainingStringPart = remaingStringPart.find("}}")
      if (closeBracketInRemainingStringPart == -1):
        #There are no closing brackets, so output string as is
        tokenisedArray.append(remainingStringToScan)
        remainingStringToScan = ""
      else:
        tokenisedArray.append(remainingStringToScan[:(firstRepPos)])
        tokenisedArray.append(replacementToken(remaingStringPart[:closeBracketInRemainingStringPart]))
        remainingStringToScan = remaingStringPart[(closeBracketInRemainingStringPart+2):]

      firstRepPos = remainingStringToScan.find("${{")

    if len(remainingStringToScan) > 0:
      tokenisedArray.append(remainingStringToScan)

    newVal = ""
    for x in tokenisedArray:
      if (isinstance(x, str)):
        newVal += x
      else:
        retVal = x.getOutput()
        newVal += retVal["newVal"]
        if retVal["replaced"]:
          totalReplaced += 1

    print("newVal:", newVal)
    return {
      "newVal": newVal,
      "numberOfReplacementsMade": totalReplaced
    }

  def replaceEnvVars(self, runEnv, stepLogger):
    num_Replaced = { "num": 0 }

    for curDataItem in self.data:
      if isinstance(self.data[curDataItem], list):
        resList = []
        for x in self.data[curDataItem]:
          retVal = self.getReplacedEnvVar(curVal=x, runEnv=runEnv)
          resList.append(retVal["newVal"])
          num_Replaced["num"] += retVal["numberOfReplacementsMade"]
        self.data[curDataItem] = resList
      else:
        retVal = self.getReplacedEnvVar(curVal=self.data[curDataItem], runEnv=runEnv)
        self.data[curDataItem] = retVal["newVal"]
        num_Replaced["num"] += retVal["numberOfReplacementsMade"]

    stepLogger(" - replaced " + str(num_Replaced["num"]) + " environment vars found in step yaml")
    return

  def run(self, stepLogger):
    raise Exception("Not overridden")