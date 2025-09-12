import os
import sys
import subprocess

def clear_screen():
    os.system('cls') if (sys.platform.lower() ==
                         "win32") else os.system('clear')

def colorizeInput(text:str):
    print(text, end='', flush=True)
    return input()

def execute(command:str):
    return subprocess.getoutput(command)