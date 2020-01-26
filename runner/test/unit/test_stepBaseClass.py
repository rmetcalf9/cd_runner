import unittest
import stepBaseClass

class test_stepBaseClass(unittest.TestCase):

  def test_replaceEnvVars_simple(self):
    stepData = {
      "notListNoReplace": "ABC123",
      "listNoReplace": [ "AA", "BB" ],
      "notListNoReplace": "ABC${{tobereplaced}}123",
      "listNoReplace": ["AA", "C${{tobereplaced2}}"]
    }
    obj = stepBaseClass.stepBaseClass(
      name=None,
      type=None,
      data=stepData
    )
    replaceData = {
      "tobereplaced": "REPLACED!!!"
    }
    raise Exception("Test not implemented")
