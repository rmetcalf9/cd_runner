import unittest
from unittest.mock import Mock
import stepBaseClass
import python_Testing_Utilities

class test_stepBaseClass(unittest.TestCase):

  def test_replaceEnvVars_simple(self):
    stepData = {
      "notListNoReplace": "ABC123",
      "listNoReplace": [ "AA", "BB" ],
      "notListReplace": "ABC${{tobereplaced}}123",
      "listReplace": ["AA", "C${{tobereplaced2}}"],
      "notFoundNoReplace": "ABC${{nottobereplaced}}123",
      "brokenNoCLose": "ABC${{123",
      "brokenNoCloseAtStart": "${{123"
    }
    obj = stepBaseClass.stepBaseClass(
      name=None,
      type=None,
      data=stepData
    )
    replaceData = {
      "tobereplaced": "REPLACED!!!",
      "tobereplaced2": "xx34!!!"
    }
    mockStepLogger = Mock()
    obj.replaceEnvVars(runEnv=replaceData, stepLogger=mockStepLogger)

    ExpectedLogMessage = " - replaced 2 environment vars found in step yaml"
    mockStepLogger.assert_called_once_with(ExpectedLogMessage)

    expectedFinalStepData = {
      "notListNoReplace": "ABC123",
      "listNoReplace": [ "AA", "BB" ],
      "notListReplace": "ABCREPLACED!!!123",
      "listReplace": ["AA", "Cxx34!!!"],
      "notFoundNoReplace": "ABC${{nottobereplaced}}123",
      "brokenNoCLose": "ABC${{123",
      "brokenNoCloseAtStart": "${{123"
    }
    python_Testing_Utilities.assertObjectsEqual(
      unittestTestCaseClass=self,
      first=obj.data,
      second=expectedFinalStepData,
      msg="Wrong final data",
      ignoredRootKeys=[]
    )

#TODO Test two vars on one line
