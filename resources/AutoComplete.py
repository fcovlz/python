"""
Steps to program auto complete:
1.- Install reeadline using pip
2.- Install rlcompleter
3.- Create a new system environment variable called "PYTHONSTARTUP"
4.- Set the path to point out this script
5.- Close Python and open it to enjoy tab auto-complete :)
"""

import rlcompleter, readline
readline.parse_and_bind('tab:complete')