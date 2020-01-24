import time
import subprocess

def executeAndWait(cmd, timeout):
  job_env = dict()
  # job_env = os.environ.copy()
  start_time = time.time()
  proc = subprocess.Popen(
    cmd,
    stdin=None,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    shell=True,
    cwd=None,
    preexec_fn=None,
    env=job_env
  )
  returncode = None
  while (returncode == None):
    returncode = proc.poll()
    if (time.time() - start_time) > timeout:
      os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
      # valid return codes are between 0-255. I have hijacked -1 for timeout
      returncode = -1
    time.sleep(0.2)
  stdout, stderr = proc.communicate()
  completed = subprocess.CompletedProcess(
    args=cmd,
    returncode=returncode,
    stdout=stdout,
    stderr=stderr,
  )
  return completed
