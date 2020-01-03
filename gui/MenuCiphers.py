from gui.Menu import Menu
from gui.Terminal import Terminal
from core.cryptography.Ciphers import *
import time

import os.path

class MenuCiphers(Menu):

    CIPHERS_NAME = ['Reverse', 'Caesar', 'Transposition', 'Affine', 'Simple Substitution', 'Vigenere', 'AES', 'KRYPTHON']
    def __init__(self):
        self._columns = self.COLUMNS
        self._rows = self.ROWS
        self._managerData = None
        self._running = True
        self._optionMenu = 0
        self._optionSubMenu = 0
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
        Terminal.print("\t\t\t --> (1) Cipher %s - " % (self.CIPHERS_NAME[0]), "yellow")
        Terminal.print("\t\t\t --> (2) Cipher %s - " % (self.CIPHERS_NAME[1]), "yellow")
        Terminal.print("\t\t\t --> (3) Cipher %s - " % (self.CIPHERS_NAME[2]), "yellow")
        Terminal.print("\t\t\t --> (4) Cipher %s - " % (self.CIPHERS_NAME[3]), "yellow")
        Terminal.print("\t\t\t --> (5) Cipher %s - " % (self.CIPHERS_NAME[4]), "yellow")
        Terminal.print("\t\t\t --> (6) Cipher %s - " % (self.CIPHERS_NAME[5]), "yellow")
        Terminal.print("\t\t\t --> (7) Cipher %s - " % (self.CIPHERS_NAME[6]), "yellow")
        Terminal.print("\t\t\t --> (8) Cipher %s - " % (self.CIPHERS_NAME[7]), "yellow")
        Terminal.print("\t\t\t --> (0) Close", "yellow")
        self._rows = self._rows - 4
        Terminal.print()
        self.inputNumberOptionMenu('menu', 'Crypthography', 0, 8)


    def title_sub_menu(self):
        option = self.getOptionMenu('menu') - 1
        Terminal.print()
        Terminal.print("\t\t\t         CIPHER %s  " % (self.CIPHERS_NAME[option]), "yellow")
        Terminal.print("\t\t\t\t ---> (1) Encryption - ", "yellow")
        Terminal.print("\t\t\t\t ---> (2) Decryption - ", "yellow")
        Terminal.print("\t\t\t\t ---> (0) Back Cryothography Menu - ", "yellow")
        Terminal.print()
        self.inputNumberOptionMenu('submenu', self.CIPHERS_NAME[option], 0, 2)
        
    def run(self):

        while self._running != False:

            option = self.getOptionMenu('menu')
            # If the option of input is for go back to Menu Main
            if option == 0:
                self._running = False
                continue
            
            optionSubMenu = 1
            while optionSubMenu != 0:
                self.title_sub_menu()
                optionSubMenu = self.getOptionMenu('submenu')
                if optionSubMenu == 0:
                    continue
                self.option_cipher()
            
            self.MenuTitle()
            

        return True

    def input_symbols_option(self):
        Terminal.print("\t\t\t         SYMBOLS option to use ", "yellow")
        Terminal.print("\t\t\t\t -> (1) LETTERS = %s" % (Cipher.LETTERS), "yellow")
        Terminal.print("\t\t\t\t -> (2) SYMBOLS = %s" % (Cipher.SYMBOLS), "yellow")
        Terminal.print("\t\t\t\t -> (3) SYMBOLS_ASCII = %s" % (Cipher.SYMBOLS_ASCII), "yellow")
        Terminal.print("\t\t\t\t -> (4) SYMBOLS_ASCII_EXTENDED = %s" % (Cipher.SYMBOLS_ASCII_EXTENDED), "yellow")
        Terminal.print("\t\t\t\t         *) Any other key load SYMBOLS by default", "yellow")
        Terminal.print()
        symbol_option = input("\t\t\t\t Choise SYMBOLS option to use in the text:  ")
        if symbol_option == '1' or symbol_option == '2' or symbol_option == '3' or symbol_option == '4':
            self._symbol_to_use = int(symbol_option)
        else:self._symbol_to_use = 2
        

    def input_original_text(self):
        text_isRight = False
        text_final = []
        while text_isRight != True:
            text = input("\t\t\t\t Inside Text:  ")
            symbolsNotAllowed = []
            symbolsToUse = ''
            if self._symbol_to_use == 1:
                symbolsToUse = Cipher.LETTERS
            elif self._symbol_to_use == 2:
                symbolsToUse = Cipher.SYMBOLS
            elif self._symbol_to_use == 3:
                symbolsToUse = Cipher.SYMBOLS_ASCII
            elif self._symbol_to_use == 4:
                symbolsToUse = Cipher.SYMBOLS_ASCII_EXTENDED
            
            for symbol in text:
                if symbol in symbolsToUse:
                    text_final.append(symbol)
                else:
                    symbolsNotAllowed.append(symbol)
            
            if len(symbolsNotAllowed) != 0:
                text_isRight = False
                Terminal.print()
                symbolsNotAllowed = ''.join(symbolsNotAllowed)
                Terminal.print("\t\t\t\t  WARNING! The input text doesn't allow characters %s " % (symbolsNotAllowed), "red")
                Terminal.print()
            else:
                text_isRight = True
        
        return ''.join(text_final)

    def option_cipher(self):
        option = self.getOptionMenu('menu')
        optionSub = self.getOptionMenu('submenu')
        #print('Option %s' % (option))
        #print('OptionSub %s' % (optionSub))

        self.input_symbols_option()
        text_original = self.input_original_text()
        text_translated = ''
        neededKey = True
        autoKey = True
        # If the option of input is for use Cipher Reverse option
        if option == 1:
            cipher = CipherReverse()
            neededKey = False
            autoKey = False
            if optionSub == 1 or optionSub == 2:
                text_translated = cipher.reverseAll(text_original)
                self.show_processed_text_original(text_original)
                self.show_processed_text_translated(text_translated)
        
        # If the option of input is for use Cipher Caesar option
        elif option == 2:
            cipher = CipherCaesar()
            key = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
            if key == 0:
                autoKey = True
                key = cipher.getRandomKey()      
            # if the option of the sub Menu Caesar is encryption mode
            if optionSub == 1:
                text_translated = cipher.encrypt(text_original, key)
            # if the option of the sub Menu Caesar is decryption mode
            if optionSub == 2:
                text_translated = cipher.decrypt(text_original, key)
        
        # If the option of input is for use Cipher Transposition option
        elif option == 3:
            cipher = CipherTransposition()
            # if the option of the sub Menu Transposition is encryption mode
            if optionSub == 1:
                text_translated = cipher.encrypt(text_original)
            # if the option of the sub Menu Transposition is decryption mode
            if optionSub == 2:
                text_translated = cipher.decrypt(text_original)
        
        # If the option of input is for use Cipher Affine option
        elif option == 4:
            cipher = CipherAffine()
            # if the option of the sub Menu Affine is encryption mode
            if optionSub == 1:
                text_translated = cipher.encrypt(text_original)
            # if the option of the sub Menu Affine is decryption mode
            if optionSub == 2:
                text_translated = cipher.decrypt(text_original)
        
        # If the option of input is for use Cipher Simple Substitution option
        elif option == 5:
            cipher = CipherSimpSub()
            # if the option of the sub Menu Simple Substitution is encryption mode
            if optionSub == 1:
                text_translated = cipher.encrypt(text_original)
            # if the option of the sub Menu Simple Substitution is decryption mode
            if optionSub == 2:
                text_translated = cipher.decrypt(text_original)
        
        # If the option of input is for use Cipher Vinegere option
        elif option == 6:
            cipher = CipherVinegere()
            # if the option of the sub Menu Vinegere is encryption mode
            if optionSub == 1:
                text_translated = cipher.encrypt(text_original)
            # if the option of the sub Menu Vinegere is decryption mode
            if optionSub == 2:
                text_translated = cipher.decrypt(text_original)
        
        # If the option of input is for use Cipher AES option
        elif option == 7:
            cipher = CipherAES()
            # if the option of the sub Menu AES is encryption mode
            if optionSub == 1:
                text_translated = cipher.encrypt(text_original)
            # if the option of the sub Menu AES is decryption mode
            if optionSub == 2:
                text_translated = cipher.decrypt(text_original)
        
        # If the option of input is for use Cipher KRYPTHON option
        elif option == 8:
            cipher = CipherKRYPTHON()
            # if the option of the sub Menu KRYPTHON is encryption mode
            if optionSub == 1:
                text_translated = cipher.encrypt(text_original)
            # if the option of the sub Menu KRYPTHON is decryption mode
            if optionSub == 2:
                text_translated = cipher.decrypt(text_original)
        
        self.show_processed_text_original(text_original)
        if neededKey == True:
            self.show_processed_text_key(keyUsed, autoKey)
        self.show_processed_text_translated(text_translated)


    def show_processed_text_original(self, originalText):
        print()
        Terminal.print("\t\t\t\t\t Orginal Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (originalText), "blod")
    
    def show_processed_text_key(self, key, auto=False):
        optionMenu = self.getOptionMenu('submenu') - 1
        textInLine = ''
        if self.getOptionMenu('submenu') - 1 == 1:
            textInLine = 'encrypt'
        else:textInLine = 'decrypt'
        if auto == True:
            Terminal.print("\t\t\t\t\t Key AutoGenerated to %sting with %s: %s" %(textInLine, self.CIPHERS_NAME[optionMenu], key), "reset")
        else:Terminal.print("\t\t\t\t\t Key used to %sting with %s: %s" %(textInLine, self.CIPHERS_NAME[optionMenu], key), "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (key), "blod")

    def show_processed_text_translated(self, translatedText):
        optionMenu = self.getOptionMenu('submenu') - 1
        textInLine = ''
        if self.getOptionMenu('submenu') - 1 == 1:
            textInLine = 'encrypt'
        else:textInLine = 'decrypt'
        Terminal.print("\t\t\t\t\t Text %sed: " % (textInLine), "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (translatedText), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()
    

    
    
    def cipher_caesar_encryption(self):
        print()
        text = input("\t\t\t\t Inside Text to Encrypt[Caesar]:  ")
        key = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
        cipher = CipherCaesar()
        if key == 0:
            key = cipher.getRandomKey()       
        encrypt_text = cipher.encrypt(text, key)
        print()
        Terminal.print("\t\t\t\t\t Orginal Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (text), "blod")
        Terminal.print("\t\t\t\t\t Encrypt[Caesar] Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (encrypt_text), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()
    
    def cipher_caesar_decryption(self):
        print()
        text = input("\t\t\t\t Inside Text to Decrypt[Caesar]:  ")
        key = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
        cipher = CipherCaesar()
        if key == 0:
            key = cipher.getRandomKey()     
        encrypt_text = cipher.decrypt(text, key)
        print()
        Terminal.print("\t\t\t\t\t Encrypt Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (text), "blod")
        Terminal.print("\t\t\t\t\t Dencrypt[Caesar] Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (encrypt_text), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()
    
    def cipher_caesar_brute_force(self):
        print()
        text = input("\t\t\t\t Inside Text to Cracking[Caesar]:  ")
        cipher = CipherCaesar()
        cipher.cracking_brute_force(text)
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()

    def cipher_transposition_encryption(self):
        print()
        text = input("\t\t\t\t Inside Text to Encrypt[Transposition]:  ")
        key = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
        
        cipher = CipherTransposition()
        if key == 0:
            key = cipher.getRandomKey()
        encrypt_text = cipher.encrypt(text, key)
        print()
        Terminal.print("\t\t\t\t\t Original Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (text), "blod")
        Terminal.print("\t\t\t\t\t Encrypt Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (encrypt_text), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()

    def cipher_transposition_decryption(self):
        print()
        encrypt_text = input("\t\t\t\t Inside Text to Encrypt[Transposition]:  ")
        key = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
        cipher = CipherTransposition()
        if key == 0:
            key = cipher.getRandomKey()
        text = cipher.decrypt(encrypt_text, key)
        print()
        Terminal.print("\t\t\t\t\t Encrypt Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (encrypt_text), "blod")
        Terminal.print("\t\t\t\t\t Dencrypt[Caesar] Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (text), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()
    
    def cipher_transposition_brute_force(self):
        print()

    def cipher_affine_encryption(self):
        print()
        encrypt_text = input("\t\t\t\t Inside Text to Encrypt[Affine]:  ")
        key = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
        rightKey = False
        cipher = CipherAffine()
        while rightKey == False:
            if key == 0:
                key = cipher.getRandomKey()
            keyA, keyB = cipher.getKeyParts(key)
            rightKey = cipher.checkKeys()
            text = cipher.decrypt(encrypt_text, key)
        print()
        Terminal.print("\t\t\t\t\t Encrypt Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (encrypt_text), "blod")
        Terminal.print("\t\t\t\t\t Dencrypt[Affine] Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (text), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()

    def cipher_affine_decryption(self):
        print()
    
    def cipher_affine_brute_force(self):
        print()

    def cipher_simpSub_encryption(self):
        print()
        text = input("\t\t\t\t Inside Text to Encrypt[SimpSub]:  ")
        
        rightKey = False
        cipher = CipherSimpSub()
        key = 'L'
        while rightKey == False:
            if key != '0':
                key = input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  ")
            if key == '0':
                key = cipher.getRandomKeyLetters()
            if not cipher.keyIsValid(key):
                Terminal.print("ERROR ! There is an error in the key or symbol set.", "red")
            else:rightKey = True
            
        encrypt_text = cipher.encrypt(text, key)
        print()
        Terminal.print("\t\t\t\t\t Original Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (text), "blod")
        Terminal.print("\t\t\t\t\t Encrypt[SimpSub] Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (encrypt_text), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()

    def cipher_simpSub_decryption(self):
        print()
    
    def cipher_simpSub_brute_force(self):
        print()

    def cipher_AES_encryption(self):
        print()

    def cipher_AES_decryption(self):
        print()

    def cipher_KYPTHON(self):
        print()