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
    try:
        kwargs = {
            "shell": True,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "text": True
        }

        if (sys.platform.lower() == 'win32'):
            kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW

        result = subprocess.run(command, **kwargs)

        if result.returncode == 0:
            return True
        else:
            return False

    except:
        return False