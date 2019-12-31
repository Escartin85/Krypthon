from gui.Menu import Menu
from gui.MenuCiphers import MenuCiphers
#from menuUsers import MenuUsers
from gui.Terminal import Terminal
#from menuMovies import MenuMovie
#from menuGenders import MenuGenders
import os.path

class MenuMain(Menu):
    def __init__(self):
        #self._menuUsers = 0
        #self._menuMovies = 0
        #self._menuGenders = 0
        self._option = 0
        self._columns = self.COLUMNS
        self._rows = self.ROWS
        self._running = True


    def run(self):
        
        while self._running != False:
            self.menu = 0
            #self.menuMovies = 0
            #self.menuCategories = 0
            #self.menuSearch = 0
            self._option = 0
            self._columns = self.COLUMNS
            self._rows = self.ROWS
            self._running = True

            self.menu_title()
            
            if self.getOption() == '1':
                self._menu = MenuCiphers()
                self._running = self._menu.run()
            #elif self.getOption() == '2':
                #self._menuMovies = MenuMovie()
                #self._running = self._menuMovies.run()
            #elif self.getOption() == '3':
                #self._menuGenders = MenuGenders()
                #self._running = self._menuGenders.run()
            elif self.getOption() == '0':
                self._running = False
            else:
                Terminal.print("\t\t\t --> ERROR = The option doesn't exist")
                input()
                self._running = True

        return False
    
    def title(self):
        Terminal.print()
        Terminal.print("\t\t\t\t ██╗  ██╗██████╗ ██╗   ██╗██████╗ ████████╗██╗  ██╗ ██████╗ ███╗   ██╗ ", "red")
        Terminal.print("\t\t\t\t ██║ ██╔╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║ ", "red")
        Terminal.print("\t\t\t\t █████╔╝ ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ███████║██║   ██║██╔██╗ ██║ ", "red")
        Terminal.print("\t\t\t\t ██╔═██╗ ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══██║██║   ██║██║╚██╗██║ ", "red")
        Terminal.print("\t\t\t\t ██║  ██╗██║  ██║   ██║   ██║        ██║   ██║  ██║╚██████╔╝██║ ╚████║ ", "red")
        Terminal.print("\t\t\t\t ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ", "red")
        Terminal.print("\t\t\t\t\t\t\t\t\t\t\t\t\t - Developer by", "cyan")
        Terminal.print("\t\t\t\t\t\t\t\t  __  __             ___          _                         ", "cyan")
        Terminal.print("\t\t\t\t\t\t\t\t |  \/  |  _ _      | _ )  __ _  | |_   _ __    __ _   _ _  ", "cyan")
        Terminal.print("\t\t\t\t\t\t\t\t | |\/| | | '_|  _  | _ \ / _` | |  _| | '  \  / _` | | ' \ ", "cyan")
        Terminal.print("\t\t\t\t\t\t\t\t |_|  |_| |_|   (_) |___/ \__,_|  \__| |_|_|_| \__,_| |_||_|", "cyan")
                                                            


    def credits(self):
        Terminal.print()
        Terminal.print("\t MIT License", "cyan")
        Terminal.print("\t Copyright (c) 2019 Mr. Batman", "cyan")
        Terminal.print("\t Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation", "cyan")
        Terminal.print("\t files (the ""Software""), to deal in the Software without restriction, including without limitation the rights to use, copy,", "cyan")
        Terminal.print("\t modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the", "cyan")
        Terminal.print("\t Software is furnished to do so, subject to the following conditions:", "cyan")
        Terminal.print("\t The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.", "cyan")
        Terminal.print("\t THE SOFTWARE IS PROVIDED ""AS IS"", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE", "cyan")
        Terminal.print("\t WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT", "cyan")
        Terminal.print("\t HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,", "cyan")
        Terminal.print("\t OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.", "cyan")
        Terminal.print()

    def menu_title(self):
        self.title()
        self.credits()
        Terminal.print()
        Terminal.print("\t\t  __  __                         __  __          _        ", "yellow")                                                                                                           
        Terminal.print("\t\t |  \/  |  ___   _ _    _  _    |  \/  |  __ _  (_)  _ _  ", "yellow")                                                                                                           
        Terminal.print("\t\t | |\/| | / -_) | ' \  | || |   | |\/| | / _` | | | | ' \ ", "yellow")                                                                                                           
        Terminal.print("\t\t |_|  |_| \___| |_||_|  \_,_|   |_|  |_| \__,_| |_| |_||_|", "yellow")    
        Terminal.print()
        Terminal.print()
        self._rows = self._rows - 16
        Terminal.print("\t\t\t --> (1) CRYPTHOGRAPHY - Encryption/Decryption using Ciphers.", "yellow")
        Terminal.print("\t\t\t --> (0) Close", "yellow")

        Terminal.print()

        for y in range(1, self._rows - 4):
            self._rows = self._rows - 1
            Terminal.print()

        self.textGetOption()