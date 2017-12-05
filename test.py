import sys
import os
import subprocess

#Program for to close windows application
import time
import subprocess

def open_program(path_name):

    return subprocess.Popen(path_name)

def close_program(p):
    p.terminate()

p=open_program(r"C:\WINDOWS\system32\cmd.exe")
time.sleep(3)
close_program(p)
