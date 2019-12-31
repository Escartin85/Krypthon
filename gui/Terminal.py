# this class will hold functions for interaction with a terminal or command prompt
# cleaning it working in all operative systems. And adding the customization of 
# the out with many diferents colors
# @Author: Javier Escartin Diaz
# @ID Student: 15017740

import os
import sys

# define class Terminal or Command Prompt
class Terminal():
    dDefault_columns = "80"
    dDefault_rows = "24"
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    YELLOW = "\033[1;33m"
    GREEN = '\033[1;32m'
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[1;m"
    GRAY = "\033[1;30m"
    default_columns = "80"
    default_rows = "24"
# constructor Terminal or Command Prompt
    def __init__(self):
        Terminal.loadDefaultSizes()
        Terminal.clean()

    @staticmethod
    def loadDefaultSizes():
        columns, rows = os.get_terminal_size(0)
        Terminal.dDefault_columns = columns
        Terminal.dDefault_rows = rows

    # reset the size was before run the program
    @staticmethod
    def defaultSizeTerminal():
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=self.default_columns, cols=self.default_rows))

    # resize the terminal by custome config
    @staticmethod
    def setSizeTerminal(customColumns="80", customRows="24"):
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=customRows, cols=customColumns))

    # Clean console or terminal depends of each different operative system.
    @staticmethod
    def clean():
        if os.name in ('nt', 'dos'):
            os.system('cls')
        elif os.name in ('linux', 'osx', 'posix'):
            os.system('clear')

    # printing text in colour
    @staticmethod
    def print(Text='', Color='reset'):
        if Color.lower() == "red": 
            print(Terminal.RED + Text + Terminal.RESET)
        elif Color.lower() == "blue": 
            print(Terminal.BLUE + Text + Terminal.RESET)
        elif Color.lower() == "cyan": 
            print(Terminal.CYAN + Text + Terminal.RESET)
        elif Color.lower() == "green": 
            print(Terminal.GREEN + Text + Terminal.RESET)
        elif Color.lower() == "blod": 
            print(Terminal.BOLD + Text + Terminal.RESET)
        elif Color.lower() == "reverse": 
            print(Terminal.REVERSE + Text + Terminal.RESET)
        elif Color.lower() == "gray": 
            print(Terminal.GRAY + Text + Terminal.RESET)
        elif Color.lower() == "yellow": 
            print(Terminal.YELLOW + Text + Terminal.RESET)
        elif Color.lower() == "reset": 
            print(Terminal.RESET + Text + Terminal.RESET)
        else:print(Terminal.RESET + Text + Terminal.RESET)
