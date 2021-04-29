import subprocess

def execCommand(cmd):
    out = subprocess.check_output([cmd], shell=True).decode('utf-8')
    return out