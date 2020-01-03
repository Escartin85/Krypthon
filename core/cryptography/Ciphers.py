
from core.cryptography.CryptoMath import CryptoMath
import math
import sys, random

class Cipher():
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    SYMBOLS_ASCII = """! "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    SYMBOLS_ASCII_EXTENDED = 'ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒáíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀ÓßÔÒõÕµþÞÚÛÙýÝ¯´≡±‗¾¶§÷¸°¨·¹³²■'
    SYMBOLS_USED = ''

    def __init__(self, symbols_used):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
        self.loadSymbolsToUse()
        
    
    def loadSymbolsToUse(self):
        self.SYMBOLS_USED = self.SYMBOLS
        if symbols_used == 1:
            self.SYMBOLS_USED = self.LETTERS
        if symbols_used == 3:
            self.SYMBOLS_USED = self.SYMBOLS_ASCII
        if symbols_used == 4:
            self.SYMBOLS_USED = self.SYMBOLS_ASCII_EXTENDED

    def getSymbolsToUse(self):
        return self.SYMBOLS_USED
        
    def getMode(self):
        return self._mode
    
    def getText(self):
        return self._text
    
    def getEncryptedText(self):
        return self._encrypted_text
    
    def getKey(self):
        return self._key
    
    def getRandomKey(self):
        while True:
            keyA = random.randint(2, len(self.SYMBOLS_USED))
            keyB = random.randint(2, len(self.SYMBOLS_USED))
            if cryptomath.gcd(keyA, len(self.SYMBOLS_USED)) == 1:
                return keyA * len(self.SYMBOLS_USED) + keyB

class CipherReverse(Cipher):
    def __init__(self, text=''):
        self._text = text
        self._encrypted_text = ''

    def reverseAll(self, text):
        self._text = text
        self._encrypted_text = ''
        count = len(text) - 1
        while count >= 0:
            self._encrypted_text = self._encrypted_text + text[count]
            count = count - 1
        return self._encrypted_text

# Caesar Cipher
class CipherCaesar(Cipher):
    def __init__(self):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''

    def cracking_brute_force(self, text, visualMode=True):
        self._text = ''
        self._encrypted_text = text
        # loop through every possible key:
        for key in range(len(self.SYMBOLS_USED)):
            # it is important to set translated to the blank string so that the
            # previous iteration's value for translated is cleared:
            translated = ''
                
            for symbol in self._encrypted_text:
                # Only symbols in the SYMBOLS string can be encrypted/decrypted.
                if symbol in self.SYMBOLS_USED:
                    symbolIndex = self.SYMBOLS_USED.find(symbol)
                    translatedIndex = symbolIndex - key
                    
                    # handle wraparound, if needed:
                    if translatedIndex < 0:
                        translatedIndex = translatedIndex + len(self.SYMBOLS_USED)
                    # append the decrypted symbol
                    translated = translated + self.SYMBOLS_USED[translatedIndex]
                else:
                    # append the symbol without encrypting/decrypting:
                    translated = translated + symbol
            if visualMode == True:
                # Display every possible decryption:
                print('Key #%s: %s' % (key, translated))

        # return the translated string:
        return self._encrypted_text

    def encrypt(self, text, key):
        self._text = text
        self._mode = 'encrypt'
        self._key = key
        self._encrypted_text = self.modeEncryptDecrypt(self._mode)
        # return the translated string:
        return self._encrypted_text

    def decrypt(self, text, key):
        self._text = text
        self._mode = 'decrypt'
        self._key = key
        self._encrypted_text = self.modeEncryptDecrypt(self._mode)
        # return the translated string:
        return self._encrypted_text

    def modeEncryptDecrypt(self, mode):
        translatedText = ''
        for symbol in self._text:
            # Only symbols in the SYMBOLS string can be encrypted/decrypted.
            if symbol in self.SYMBOLS_USED:
                symbolIndex = self.SYMBOLS_USED.find(symbol)

                # perform encryption/decryption:
                if mode == 'encrypt':
                    translatedIndex = symbolIndex + int(self._key)
                elif mode == 'decrypt':
                    translatedIndex = symbolIndex - int(self._key)
                
                # handle wraparound, if needed:
                if translatedIndex >= len(self.SYMBOLS_USED):
                    translatedIndex = translatedIndex - len(self.SYMBOLS_USED)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(self.SYMBOLS_USED)
                
                translatedText = translatedText + self.SYMBOLS_USED[translatedIndex]
            else:
                # append the symbol without encrypting/decrypting:
                translatedText = translatedText + symbol
        return translatedText

# Caesar Transposition
class CipherTransposition(Cipher):  
    
    def __init__(self):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
        
    def encrypt(self, text, key):
        self._text = text
        self._key = key
        # each string in ciphertext represents a column in the grid
        self._encrypted_text = [''] * self._key

        # loop through each column in ciphertext:
        for column in range(self._key):
            currentIndex = column

            # keep looping until currentIndex goes past the message length:
            while currentIndex < len(self._text):
                # place the character at currentIndex in message at the
                # end of the current column in the ciphertext list:
                self._encrypted_text[column] += self._text[currentIndex]

                # move currentIndex over:
                currentIndex += self._key
        
        # convert the ciphertext list into a single string value and return it
        return ''.join(self._encrypted_text)

    def decrypt(self, textEncrypt, key):
        # the transposition decrypt function will simulate the "columns" and
        # "rows" of the grid that the plaintext is written on by using a list
        # of strings. First, we need to calculate a few values.
        self._encrypted_text = textEncrypt
        self._key = key
        
        # the number of "columns" in our transposition grid:
        numOfColumns = int(math.ceil(len(self._encrypted_text) / float(key))) 
        # tje number of "rows" in our grid
        numOfRows = key
        # the number of "shaded boxes" in the last "column" of the grid
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(self._encrypted_text)

        # each string in plaintext represents a column in the grid
        self._text = [''] * numOfColumns

        # the column and row variables point to where in the grid the next
        # character in the encrypted message will go:
        column = 0
        row = 0

        for symbol in self._encrypted_text:
            self._text[column] += symbol
            # point to the next column
            column += 1 

            # if there are no more columns OR we're at a shaded box, go back
            # to the first column and the next row:
            if(column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                column = 0
                row += 1
        
        return ''.join(self._text)


    def cracking_brute_force(self, text, visualMode=True):
        print('Hacking...')

        # Python programs can be stopped at any time by pressing Ctrl-C (on
        # Windows) or Ctrl-D (on Mac and Linux)
        #print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
        # Brute-force by looping through every possible key.
        #for key in range(1, len(text)):
        #    print('Trying key #%s...' % (key))

        #    decryptedText = transpositionCipher.decryptMessage(key, text)

        #    if detectEnglish.isEnglish(decryptedText):
                # Ask user if this is the correct decryption.
         #       print()
        #        print('Possible encryption hack:')
        #        print('Key %s: %s' % (key, decryptedText[:100]))
        #        print()
        #        print('Enter D if done, anything else to continue hacking:')
        #        response = input('> ')

        #        if response.strip().upper().startswith('D'):
        #            return decryptedText

        return None

# Caesar Affine
class CipherAffine(Cipher):
    def __init__(self):
        # the string to be encrypted/decrypted
        self._text = text
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        self._keyA = ''
        self._keyB = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
    
    def getKeyParts(self, key):
        keyA = int(key) // len(self.SYMBOLS_USED)
        keyB = int(key) % len(self.SYMBOLS_USED)
        return (keyA, keyB)


    def checkKeys(self, key, mode='encrypt'):
        self._mode = mode
        self._key = key
        keyA, keyB = self.getKeyParts(self._key)
        self._keyA = keyA
        self._keyB = keyB
        if keyA == 1 and mode == 'encrypt':
            sys.exit('Cipher is weak if key A is 1. Choose a different key.')
            return False
        if keyB == 0 and mode == 'encrypt':
            sys.exit('Cipher is weak if key B is 0. Choose a different key.')
            return False
        if keyA < 0 or keyB < 0 or keyB > len(self.SYMBOLS_USED) - 1:
            sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(self.SYMBOLS_USED) - 1))
            return False
        if CryptoMath.gcd(keyA, len(self.SYMBOLS_USED)) != 1:
            sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(self.SYMBOLS_USED)))
            return False
        return True

    def encrypt(self, text, keyA, keyB):
        self._text = text
        self._key = key
        self._encrypted_text = ''
        self._mode = 'encrypt'
        #keyA, keyB = self.getKeyParts(self._key)
        #self.checkKeys(keyA, keyB, self._mode)
        for symbol in self._text:
            if symbol in self.SYMBOLS_USED:
                # Encrypt the symbol:
                symbolIndex = self.SYMBOLS_USED.find(symbol)
                self._encrypted_text += self.SYMBOLS_USED[(symbolIndex * self._keyA + self._keyB) % len(self.SYMBOLS_USED)]
            else:
                # Append the symbol without encrypting.
                self._encrypted_text += symbol 
        return self._encrypted_text

    def decrypt(self, text, key):
        self._encrypted_text = textEncrypt
        self._key = key
        self._mode = 'decrypt'
        self._text = ''
        keyA, keyB = self.getKeyParts(self._key)
        self.checkKeys(keyA, keyB, self._mode)
        modInverseOfKeyA = cryptomath.findModInverse(keyA, len(self.SYMBOLS_USED))

        for symbol in self._text:
            if symbol in self.SYMBOLS:
                # Decrypt the symbol:
                symbolIndex = self.SYMBOLS_USED.find(symbol)
                self._text += self.SYMBOLS_USED[(symbolIndex - keyB) * modInverseOfKeyA % len(self.SYMBOLS_USED)]
            else:
                # Append the symbol without decrypting.
                self._text += symbol 
        return self._text

    def cracking_brute_force(self, text, visualMode=True):
        print()

# Caesar Simple Substitution
class CipherSimpSub(Cipher):
    def __init__(self):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
    
    def getRandomKeyLetters(self):
        key = list(self.LETTERS)
        random.shuffle(key)
        return ''.join(key)

    def keyIsValid(self, key):
        keyList = list(key)
        lettersList = list(self.LETTERS)
        keyList.sort()
        lettersList.sort()

        return keyList == lettersList

    def translateMessage(self, key, text, mode):
        self._text = text
        translated = ''
        charsA = self.LETTERS
        charsB = key
        if mode == 'decrypt':
            # For decrypting, we can use the same code as encrypting. We
            # just need to swap where the key and LETTERS strings are used.
            charsA, charsB = charsB, charsA

        # Loop through each symbol in message:
        for symbol in self._text:
            if symbol.upper() in charsA:
                # Encrypt/decrypt the symbol:
                symIndex = charsA.find(symbol.upper())
                if symbol.isupper():
                    translated += charsB[symIndex].upper()
                else:
                    translated += charsB[symIndex].lower()
            else:
                # Symbol is not in LETTERS; just add it
                translated += symbol

        return translated

    def encrypt(self, text, key='LFWOAYUISVKMNXPBDCRJTQEGHZ'):
        return self.translateMessage(key, text, 'encrypt')

    def decrypt(self, text, key='LFWOAYUISVKMNXPBDCRJTQEGHZ'):
        return self.translateMessage(key, text, 'decrypt')

    def cracking_brute_force(self, text, visualMode=True):
        print()

# Caesar AES
class CipherAES(Cipher):
    def __init__(self):
        # the string to be encrypted/decrypted
        self._text = text
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
    
    def encrypt(self, text, key):
        print()

    def decrypt(self, text, key):
        print()

    def cracking_brute_force(self, text, visualMode=True):
        print()

# Caesar KRYPTHON
class CipherKRYPTHON(Cipher):
    def __init__(self):
        # the string to be encrypted/decrypted
        self._text = text
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
    
    def encrypt(self, text, key):
        print()

    def decrypt(self, text, key):
        print()

    def cracking_brute_force(self, text, visualMode=True):
        print()