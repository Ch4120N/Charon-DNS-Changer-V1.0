import os
import sys


def clear_screen():
    os.system('cls') if (sys.platform.lower() ==
                         "win32") else os.system('clear')
