import ExecuteShell

def checkoutGitRepository(runConfig, globalConfig, runDir):
  exportDir = runDir + "/co"
  cmd = "git clone " + runConfig["svnsource"] + " co"
  print("Starting clone...")
  result = ExecuteShell.executeAndWait(
    cmd=cmd,
    timeout=30.5,
    workingdir=runDir
  )
  print(" clone process exited")
  if result.returncode != 0:
    print(result.stdout)
    print(result.stderr)
    raise Exception("Failed to clone -" + str(result.returncode))
  return exportDir