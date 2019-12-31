from gui.Menu import Menu
from gui.Terminal import Terminal
import time

import os.path

class MenuCiphers(Menu):

    def __init__(self):
        self._genders = []
        self._columns = self.COLUMNS
        self._rows = self.ROWS
        self._managerData = None
        self._running = True
        self._pages = 0
        self._currentPage = 0
        self._rightArrowFree = False
        self._leftArrowFree = False
        self.MenuTitle()

    # Print the head of table
    def MenuTitle(self):
        Terminal.clean()
        Terminal.print()
        Terminal.print()
        Terminal.print("\t  Menu ", "yellow")
        Terminal.print("\t\t   ___   ___  __   __  ___   _____   _  _    ___     ___   ___     _     ___   _  _  __   __", "yellow")
        Terminal.print("\t\t  / __| | _ \ \ \ / / | _ \ |_   _| | || |  / _ \   / __| | _ \   /_\   | _ \ | || | \ \ / /", "yellow")
        Terminal.print("\t\t | (__  |   /  \ V /  |  _/   | |   | __ | | (_) | | (_ | |   /  / _ \  |  _/ | __ |  \ V / ", "yellow")
        Terminal.print("\t\t  \___| |_|_\   |_|   |_|     |_|   |_||_|  \___/   \___| |_|_\ /_/ \_\ |_|   |_||_|   |_|  ", "yellow")
        Terminal.print()
        Terminal.print()
        self._rows = self._rows - 6
        Terminal.print("\t\t\t --> (1) Cipher Reverse - ", "yellow")
        Terminal.print("\t\t\t --> (2) Cipher Caesar - ", "yellow")
        Terminal.print("\t\t\t --> (3) Cipher Transposition - ", "yellow")
        Terminal.print("\t\t\t --> (4) Cipher Affine - ", "yellow")
        Terminal.print("\t\t\t --> (5) Cipher Simple Substitution - ", "yellow")
        Terminal.print("\t\t\t --> (6) Cipher AES - ", "yellow")
        Terminal.print("\t\t\t --> (7) Cipher KRYPTHON - ", "yellow")
        Terminal.print("\t\t\t --> (0) Close", "yellow")
        self._rows = self._rows - 4
        Terminal.print()
        self.textGetOption()



    def run(self):
        self.setOption("1")

        while self._running != False:

            # If the option of input is for go back to Menu Main
            if self.getOption() == '0':
                self._running = False
            # If the option of input is for use Cipher Reverse option
            elif self.getOption() == '1':
                self.option_cipher_reverse()
            # If the option of input is for use Cipher Caesar option
            elif self.getOption() == '2':
                self.option_cipher_caesar()
            # If the option of input is for use Cipher Transposition option
            elif self.getOption() == '3':
                self.option_cipher_transposition()
            # If the option of input is for use Cipher Affine option
            elif self.getOption() == '4':
                self.option_cipher_affine()
            # If the option of input is for use Cipher Simple Substitution option
            elif self.getOption() == '5':
                self.option_cipher_simpSub()
            # If the option of input is for use Cipher AES option
            elif self.getOption() == '6':
                self.option_cipher_AES()
            # If the option of input is for use Cipher KYPTHON option
            elif self.getOption() == '7':
                self.option_cipher_KYPTHON()
            # If the option of input is anything else not required (default)
            else:self._running = False

        return True
            
    def option_cipher_reverse(self):
        Terminal.print()
        Terminal.print("\t\t\t         CIPHER REVERSE  ", "yellow")
        Terminal.print("\t\t\t\t ---> (1) Encryption - ", "yellow")
        Terminal.print("\t\t\t\t ---> (2) Decryption - ", "yellow")
        Terminal.print()
        
        option = '0'
        while option == '0':
            option = input("\t\t\t\t Inside Option Menu:  ")
            # If the option of input is for go back to Menu Main
            if option == '1':
                self.cipher_reverse_encryption()
                option = '0'
            elif option == '2':
                self.cipher_reverse_decryption()
                option = '0'
            # If the option of input is anything else not required (default)
            else:
                Terminal.print("\t\t WARNING! Inside a right option", "red")
                Terminal.print()
                option == '0'
    
    def option_cipher_caesar(self):
        Terminal.print()
        Terminal.print("\t\t\t -->     CIPHER REVERSE - ", "yellow")
        Terminal.print("\t\t\t\t ---> (1) Encryption - ", "yellow")
        Terminal.print("\t\t\t\t ---> (2) Decryption - ", "yellow")
        Terminal.print("\t\t\t\t ---> (3) Cracking Cipher - ", "yellow")
        Terminal.print()
        
        option = '0'
        while option == '0':
            option = input("\t\t Inside Option Menu:  ")
            # If the option of input is for go back to Menu Main
            if option == '1':
                self.cipher_reverse_encryption()
            elif option == '2':
                self.cipher_reverse_decryption()
            # If the option of input is anything else not required (default)
            else:
                Terminal.print("\t\t Inside a right option", "red")
                Terminal.print()
                option == '0'

    def option_cipher_transposition(self):
        Terminal.print()
        Terminal.print("\t -->     CIPHER REVERSE - ", "yellow")
        Terminal.print("\t -----> (1) Encryption - ", "yellow")
        Terminal.print("\t -----> (2) Decryption - ", "yellow")
        Terminal.print("\t -----> (3) Cracking Cipher - ", "yellow")
        Terminal.print()
        
        option = '0'
        while option == '0':
            option = input("\t\t Inside Option Menu:  ")
            # If the option of input is for go back to Menu Main
            if option == '1':
                cipher_reverse_encryption()
            elif option == '2':
                cipher_reverse_decryption()
            # If the option of input is anything else not required (default)
            else:
                Terminal.print("\t\t Inside a right option", "red")
                Terminal.print()
                option == '0'

    def option_cipher_affine(self):
        Terminal.print()
        Terminal.print("\t -->     CIPHER REVERSE - ", "yellow")
        Terminal.print("\t -----> (1) Encryption - ", "yellow")
        Terminal.print("\t -----> (2) Decryption - ", "yellow")
        Terminal.print("\t -----> (3) Cracking Cipher - ", "yellow")
        Terminal.print()
        
        option = '0'
        while option == '0':
            option = input("\t\t Inside Option Menu:  ")
            # If the option of input is for go back to Menu Main
            if option == '1':
                cipher_reverse_encryption()
            elif option == '2':
                cipher_reverse_decryption()
            # If the option of input is anything else not required (default)
            else:
                Terminal.print("\t\t Inside a right option", "red")
                Terminal.print()
                option == '0'

    def option_cipher_simpSub(self):
        Terminal.print()
        Terminal.print("\t -->     CIPHER REVERSE - ", "yellow")
        Terminal.print("\t -----> (1) Encryption - ", "yellow")
        Terminal.print("\t -----> (2) Decryption - ", "yellow")
        Terminal.print("\t -----> (3) Cracking Cipher - ", "yellow")
        Terminal.print()
        
        option = '0'
        while option == '0':
            option = input("\t\t Inside Option Menu:  ")
            # If the option of input is for go back to Menu Main
            if option == '1':
                cipher_reverse_encryption()
            elif option == '2':
                cipher_reverse_decryption()
            # If the option of input is anything else not required (default)
            else:
                Terminal.print("\t\t Inside a right option", "red")
                Terminal.print()
                option == '0'

    def option_cipher_AES(self):
        Terminal.print()
        Terminal.print("\t -->     CIPHER REVERSE - ", "yellow")
        Terminal.print("\t -----> (1) Encryption - ", "yellow")
        Terminal.print("\t -----> (2) Decryption - ", "yellow")
        Terminal.print("\t -----> (3) Cracking Cipher - ", "yellow")
        Terminal.print()
        
        option = '0'
        while option == '0':
            option = input("\t\t Inside Option Menu:  ")
            # If the option of input is for go back to Menu Main
            if option == '1':
                cipher_reverse_encryption()
            elif option == '2':
                cipher_reverse_decryption()
            # If the option of input is anything else not required (default)
            else:
                Terminal.print("\t\t Inside a right option", "red")
                Terminal.print()
                option == '0'

    def option_cipher_KYPTHON(self):
        Terminal.print()
        Terminal.print("\t -->     CIPHER REVERSE - ", "yellow")
        Terminal.print("\t -----> (1) Encryption - ", "yellow")
        Terminal.print("\t -----> (2) Decryption - ", "yellow")
        Terminal.print("\t -----> (3) Cracking Cipher - ", "yellow")
        Terminal.print()
        
        option = '0'
        while option == '0':
            option = input("\t\t Inside Option Menu:  ")
            # If the option of input is for go back to Menu Main
            if option == '1':
                cipher_reverse_encryption()
            elif option == '2':
                cipher_reverse_decryption()
            # If the option of input is anything else not required (default)
            else:
                Terminal.print("\t\t Inside a right option", "red")
                Terminal.print()
                option == '0'
                   
    def cipher_reverse_encryption(self):
        print()
    
    def cipher_reverse_decryption(self):
        print()
