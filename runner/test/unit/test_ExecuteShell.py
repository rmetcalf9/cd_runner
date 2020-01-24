import unittest
import ExecuteShell

class test_ExecuteShell(unittest.TestCase):

  def test_Echo(self):

    result = ExecuteShell.executeAndWait(
      cmd = "echo \"Test 123\"",
      timeout = 0.5
    )
    self.assertEqual(result.stdout,b'Test 123\n')
    self.assertEqual(result.stderr,None)
    self.assertEqual(result.returncode,0)
