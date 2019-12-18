"""
Steps to program auto complete:
1.- Install reeadline using pip
2.- Install rlcompleter
3.- Create a new system environment variable called "PYTHONSTARTUP"
4.- Set the path to point out this script
5.- Close Python and open it to enjoy tab auto-complete :)

$ pip install pyreadline
$ pip install fancycompleter
"""

import rlcompleter, readline
import fancycompleter
import sys
import os

readline.parse_and_bind('tab:complete')
fancycompleter.interact(persist_history=True)


# Clear function to clear python console
def clear():
    - os.system('cls')


if sys.version[0] == str(3):
    from importlib import reload
