import subprocess

def runcmd(cmd, verbose = False, *args, **kwargs):
  # Function to execute terminal commands.
  process = subprocess.Popen(
      cmd,
      stdout = subprocess.PIPE,
      stderr = subprocess.PIPE,
      text = True,
      shell = True
  )
  std_out, std_err = process.communicate()
  if verbose:
      print(std_out.strip(), std_err)
  pass