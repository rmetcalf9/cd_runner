import unittest
import ExecuteShell
import python_Testing_Utilities

class test_ExecuteShell(unittest.TestCase):

  def test_Echo(self):

    result = ExecuteShell.executeAndWait(
      cmd = "echo \"Test 123\"",
      timeout = 0.5
    )
    self.assertEqual(result.stdout,b'Test 123\n')
    self.assertEqual(result.stderr,None)
    self.assertEqual(result.returncode,0)

  def test_withworkingdir(self):

    result = ExecuteShell.executeAndWait(
      cmd = "ls",
      timeout = 0.5,
      workingdir = "./test"
    )
    returnedRes = result.stdout.split(b"\n")
    expectedRes = [b'TestingHelper', b'acceptance', b'unit', b'']
    print(returnedRes)
    python_Testing_Utilities.assertObjectsEqual(
      unittestTestCaseClass=self,
      first=returnedRes,
      second=expectedRes,
      msg="Wrong result returned",
      ignoredRootKeys=[]
    )
    self.assertEqual(result.stderr,None)
    self.assertEqual(result.returncode,0)
