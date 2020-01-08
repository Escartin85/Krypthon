
from core.cryptography.CryptoMath import CryptoMath
from gui.Terminal import Terminal
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
        self.loadSymbolsToUse(symbols_used)
        
    
    def loadSymbolsToUse(self, symbols_used=2):
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
        return random.randint(2, len(self.SYMBOLS_USED))

class CipherReverse(Cipher):
    def __init__(self, symbols_used):
        self._text = ''
        self._encrypted_text = ''
        self.loadSymbolsToUse(symbols_used)

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
    def __init__(self, symbols_used):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
        self.loadSymbolsToUse(symbols_used)

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
    
    def __init__(self, symbols_used):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
        self.loadSymbolsToUse(symbols_used)
        
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


    

# Caesar Affine
class CipherAffine(Cipher):
    def __init__(self, symbols_used):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        self._keyA = ''
        self._keyB = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
        self.loadSymbolsToUse(symbols_used)
 
    def getRandomKey(self):
        while True:
            keyA = random.randint(2, len(self.SYMBOLS_USED))
            keyB = random.randint(2, len(self.SYMBOLS_USED))
            if CryptoMath.gcd(keyA, len(self.SYMBOLS_USED)) == 1:
                return keyA * len(self.SYMBOLS_USED) + keyB
    
    def getKeyParts(self, key):
        keyA = int(key) // len(self.SYMBOLS_USED)
        keyB = int(key) % len(self.SYMBOLS_USED)
        return (keyA, keyB)

    def checkKey(self, key, mode='encrypt'):
        keyA, keyB = self.getKeyParts(key)
        if keyA == 1 and mode == 'encrypt':
            Terminal.print("WARNING! Cipher is weak if key A is 1. Choose a different key." , "yellow")
            return False
        if keyB == 0 and mode == 'encrypt':
            Terminal.print("WARNING! Cipher is weak if key B is 0. Choose a different key." , "yellow")
            return False
        if keyA < 0 or keyB < 0 or keyB > len(self.SYMBOLS_USED) - 1:
            Terminal.print('WARNING! Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(self.SYMBOLS_USED) - 1), "yellow")
            return False
        if CryptoMath.gcd(keyA, len(self.SYMBOLS_USED)) != 1:
            Terminal.print('WARNING! Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(self.SYMBOLS_USED)), "yellow")
            return False
        return True

    def encrypt(self, text, key):
        self._text = text
        self._key = key
        self._keyA, self._keyB = self.getKeyParts(key)
        self._encrypted_text = ''
        self._mode = 'encrypt'
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
        self._encrypted_text = text
        self._key = key
        self._keyA, self._keyB = self.getKeyParts(key)
        self._mode = 'decrypt'
        self._text = ''
        modInverseOfKeyA = CryptoMath.findModInverse(self._keyA, len(self.SYMBOLS_USED))

        for symbol in self._encrypted_text:
            if symbol in self.SYMBOLS:
                # Decrypt the symbol:
                symbolIndex = self.SYMBOLS_USED.find(symbol)
                self._text += self.SYMBOLS_USED[(symbolIndex - self._keyB) * modInverseOfKeyA % len(self.SYMBOLS_USED)]
            else:
                # Append the symbol without decrypting.
                self._text += symbol 
        return self._text


# Caesar Simple Substitution
class CipherSimpSub(Cipher):
    def __init__(self, symbols_used):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
        self.loadSymbolsToUse(symbols_used)
    
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


# Caesar KRYPTHON
class CipherKRYPTHON(CipherCaesar):
    def __init__(self, symbols_used):
        # the string to be encrypted/decrypted
        self._text = ''
        self._encrypted_text = ''
        # the encryption/descryption key:
        self._key = ''
        # the mode to "encrypt" or "decrypt"
        self._mode = ''
        self.loadSymbolsToUse(symbols_used)
    def generatePrimNumbers(self, key):
        primNumbers = []
        count = 3
        maxNumber = len(self.SYMBOLS_USED)
        while count <= maxNumber:
            isprime = True
            
            for x in range(2, int(math.sqrt(count) + 1)):
                if count % x == 0: 
                    isprime = False
                    break
            
            if isprime:
                if key <=count:
                    primNumbers.append(count)
            count += 1
        return primNumbers

    def generatePairNumbers(self, key):
        countKey = 0
        pairNumbers = []
        maxNumber = len(self.SYMBOLS_USED)
        multip = key
        num = key
        while num <= maxNumber:
            multip = key * multip
            num = multip
            if num > maxNumber:
                break
            pairNumbers.append(multip)
                
        return pairNumbers

    def getKeys(self, pairKeys, primKeys, text):
        longText = len(text)
        maxCounter = 0
        if len(pairKeys) > len(primKeys):
            maxCounter = len(pairKeys)
        else:
            maxCounter = len(primKeys)
        
        keys = []
        count = 0
        while len(keys) <= longText:
            if len(keys) == longText:
                break
            if count >= maxCounter:
                count = 0
            if len(pairKeys) > 0:
                if count < len(pairKeys):
                    keys.append(pairKeys[count])
            if len(primKeys) > 0:
                if count < len(primKeys):
                    keys.append(primKeys[count])
            count += 1

        return keys

    def getRandomChar(self):
        char = '.'
        num = self.getRandomKey()
        count = 0
        for character in self.SYMBOLS_USED:
            if num == count:
                char = character
            count += 1
        return char
    
    def encrypt(self, text, key):
        self._text = text
        self._encrypted_text = ''
        longText = len(text)

        # Generate auto key based on the key. Each key is multiply 
        keysPair = []
        keysPrime = []

        keysPrime = self.generatePrimNumbers(key)
        keysPair = self.generatePairNumbers(key)
        #print(keysPair)
        #print(keysPrime)
        #print("--")
        count = 0
        keys = []
        keys = self.getKeys(keysPair, keysPrime, text)
        #print(keys)
        caesar = CipherCaesar(2)
        for row in range(longText):
            self._encrypted_text += caesar.encrypt(self._text[row], keys[count])
            count += 1
        
        reverse = CipherReverse(2)
        textReverse = reverse.reverseAll(self._encrypted_text)
        self._encrypted_text = textReverse
        return self._encrypted_text

    def decrypt(self, text, key):
        reverse = CipherReverse(2)
        textReverse = reverse.reverseAll(text)

        self._text = ''
        self._encrypted_text = textReverse
        longText = len(text)

        

        # Generate auto key based on the key. Each key is multiply 
        keysPair = []
        keysPrime = []

        keysPrime = self.generatePrimNumbers(key)
        keysPair = self.generatePairNumbers(key)
        #print(keysPair)
        #print(keysPrime)
        #print("--")
        count = 0
        keys = []
        keys = self.getKeys(keysPair, keysPrime, text)
        #print(keys)
        caesar = CipherCaesar(2)
        for row in range(longText):
            self._text += caesar.decrypt(self._encrypted_text[row], keys[count])
            count += 1
            
        #print(self._text)
        #print("--")
        return self._text
