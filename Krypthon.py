# Krypthon encryption algorithm
# Developed by Javier Escartin

from gui.MenuMain import MenuMain
from gui.Terminal import Terminal
import os
import sys
import time

# main function of main programm running Krypthon.py
def main():
    running = True
    default_columns = "80"
    default_rows = "24"
    Terminal.setSizeTerminal("180", "124")

    menuMain = MenuMain()
    while running != False:
        running = menuMain.run()

    #console.cleanConsole()
    Terminal.print("\t\t\t\t\t\t\t\t\t\t\t\tClosing KRYPTHON system...", "red")
    time.sleep(.300)
    Terminal.print("\t\t\t\t\t\t\t\t\t\t\t\tClosing KRYPTHON system...", "red")
    time.sleep(.300)
    Terminal.print("\t\t\t\t\t\t\t\t\t\t\t\tClosing KRYPTHON system...", "red")
    time.sleep(1)
    Terminal.print('', "reset")
    width = default_columns
    height = default_rows
    Terminal.setSizeTerminal(default_columns, default_rows)
    #Terminal.defaultSizeTerminal()
                                                                






if __name__ == '__main__':
    main()