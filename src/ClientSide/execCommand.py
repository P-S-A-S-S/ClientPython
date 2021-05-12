import subprocess
import json
def execCommand(cmd):
    try:
        out = subprocess.check_output([cmd], shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        return out
    except  subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')