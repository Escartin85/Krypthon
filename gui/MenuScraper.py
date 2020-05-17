from gui.Menu import Menu
from gui.Terminal import Terminal
from core.scraping.ScraperFreeRecycle import ScraperFreeRecycle
import time
import os.path

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

class MenuScraper(Menu):

    def __init__(self):
        self._columns = self.COLUMNS
        self._rows = self.ROWS
        self._managerData = None
        self._running = True
        self._optionMenu = 0
        self._optionSubMenu = 0
        self._symbol_to_use = 2
        self.MenuTitle()

    # Print the head of table
    def MenuTitle(self):
        Terminal.clean()
        Terminal.print()
        Terminal.print()
        Terminal.print("\t  Menu ", "yellow")
        Terminal.print("\t\t  _____                                 ", "yellow")
        Terminal.print("\t\t /  ___|                                ", "yellow")
        Terminal.print("\t\t \ `--.  ___ __ _ _ __  _ __   ___ _ __ ", "yellow")
        Terminal.print("\t\t `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|", "yellow")
        Terminal.print("\t\t /\__/ / (_| (_| | |_) | |_) |  __/ |   ", "yellow")
        Terminal.print("\t\t \____/ \___\__,_| .__/| .__/ \___|_|   ", "yellow")
        Terminal.print("\t\t                 | |   | |              ", "yellow")
        Terminal.print("\t\t                 |_|   |_|              ", "yellow")
        Terminal.print()
        Terminal.print()
        self._rows = self._rows - 6
        Terminal.print("\t\t\t --> (1) Scrapping all url from FreeCycle.org", "yellow")
        Terminal.print("\t\t\t --> (2) Scrapping ads from FreeCycle.org", "yellow")
        Terminal.print("\t\t\t --> (3) Scrapping groups or cities from FreeCycle.org", "yellow")
        Terminal.print("\t\t\t --> (0) Close", "yellow")
        self._rows = self._rows - 4
        Terminal.print()
        self.inputNumberOptionMenu('menu', 'Scrapper', 0, 3)

    '''
    def title_sub_menu(self):
        option = self.getOptionMenu('menu') - 1
        Terminal.print()
        Terminal.print("\t\t\t         CIPHER %s  " % (self.CIPHERS_NAME[option]), "yellow")
        Terminal.print("\t\t\t\t ---> (1) Encryption - ", "yellow")
        Terminal.print("\t\t\t\t ---> (2) Decryption - ", "yellow")
        Terminal.print("\t\t\t\t ---> (0) Back Cryothography Menu - ", "yellow")
        Terminal.print()
        self.inputNumberOptionMenu('submenu', self.CIPHERS_NAME[option], 0, 2)
    '''    
    def run(self):

        while self._running != False:

            option = self.getOptionMenu('menu')
            # If the option of input is for go back to Menu Main
            if option == 0:
                self._running = False
                continue
            '''
            optionSubMenu = 1
            while optionSubMenu != 0:
                #self.title_sub_menu()
                #optionSubMenu = self.getOptionMenu('submenu')
                #if optionSubMenu == 0:
                #    continue
                self.option_menu()
            '''
            self.option_menu()
            optionMenu = input("\t\t\t\t PESS ANY KEY TO CONTINUE  ")
            self.MenuTitle()
            

        return True
    '''
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
        else:
            self._symbol_to_use = 2
        
    
    def input_original_text(self):
        text_isRight = False
        text_final = []
        text = ''
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
                symbolsNotAllowed = []
                text = ''
                text_final = []
                Terminal.print()
            else:
                text_isRight = True
        
        return ''.join(text_final)

    def input_number_key(self):
        keyIsNumber = False
        numKey = 0
        while keyIsNumber == False:
            try:
                tempKey = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
                keyIsNumber = True
            except:
                Terminal.print("ERROR! Key input is NOT a NUMBER", "red")
                keyIsNumber = False
        
        numKey = tempKey
        return numKey
    
    def input_letters_key(self):
        keyIsNumber = False
        numKey = 0
        while keyIsNumber == False:
            try:
                tempKey = int(input("\t\t\t\t Inside Number Key | 0 [Autogenerate Key]:  "))
                keyIsNumber = True
            except:
                Terminal.print("ERROR! Key input is NOT a NUMBER", "red")
                keyIsNumber = False
        
        numKey = tempKey
        return numKey
    
    '''
    def option_menu(self):
        option = self.getOptionMenu('menu')
        
        # create object's ScrapperFreeRecycle
        scrap = ScraperFreeRecycle('https://www.freecycle.org')
        #scrap = ScrapperFreeRecycle('http://groups.freecycle.org/RahwayNJ/files/13429')

        # If the option of input is (1) - for Scrapping all url from FreeCycle.org
        if option == 1:
            finish_loop = False
            cont = 1
            # loop until (visited urls == url all)
            while finish_loop != True:
                url = scrap.getFirst_url_all()
                if url != None:
                    # extract initialization list urls
                    scrap.extract_valid_urls(url)
                    #if scrap.is_url_data() == True:
                    #    scrap.extract_data()
                
                cont = cont + 1
                finish_loop = scrap.is_empty_url_all()
            
            print("------ URLS ------")
            scrap.printData("url_all")
            print("------ SUB DOMAINS ------")
            scrap.printData("subDomain_all")
            print("------ VISITED URLS ------")
            scrap.printData("url_visited")
            print("------ OTHER URLS ------")
            scrap.printData("other_url")
            print("------ FILES ULR ------")
            scrap.printData("files_url")
            print("------ EMAILS ------")
            scrap.printData("emails")
        # If the option of input is (2) - for Scrapping ads from FreeCycle.org
        elif option == 2:
            # extract data from each single advirstement page
            scrap.extractAdInPage('https://groups.freecycle.org/group/HackneyUK/posts/77172142/Aquen%20cordless%20kettle%201.7L')
        # If the option of input is (3) - for Scrapping groups or cities from FreeCycle.org
        elif option == 3:
            scrap.extractCountriesInPage('https://www.freecycle.org/browse?noautodetect=1')
        
        
        '''
        finish_loop = False
        cont = 1
        # loop until (visited urls == url all)
        while finish_loop != True:
            url = scrap.getFirst_url_all()
            if url != None:
                # extract initialization list urls
                scrap.extract_valid_urls(url)
                #if scrap.is_url_data() == True:
                #    scrap.extract_data()
            
            cont = cont + 1
            finish_loop = scrap.is_empty_url_all()
            #finish_loop = True
        

            # get url and extract new urls
            # pass the url read to visit urls
        
        print("------ URLS ------")
        scrap.printData("url_all")
        print("------ SUB DOMAINS ------")
        scrap.printData("subDomain_all")
        print("------ VISITED URLS ------")
        scrap.printData("url_visited")
        print("------ OTHER URLS ------")
        scrap.printData("other_url")
        print("------ FILES ULR ------")
        scrap.printData("files_url")
        print("------ EMAILS ------")
        scrap.printData("emails")
        '''
        # print("---- text test -----")
        # extract data from each single advirstement page
        #extractAdInPage('https://groups.freecycle.org/group/CityOfLondon/posts/76066700/Samsung%20laser%20printer%20with%20WiFi')
        #self.show_processed_text_original(text_original)
        #if neededKey == True:
        #    self.show_processed_text_key(keyUsed, autoKey)
        #self.show_processed_text_translated(text_translated)


    def show_processed_text_original(self, originalText):
        print()
        Terminal.print("\t\t\t\t\t Orginal Text: ", "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (originalText), "blod")
    
    def show_processed_text_key(self, key, auto=False):
        optionMenu = self.getOptionMenu('submenu') - 1
        textInLine = ''
        if self.getOptionMenu('submenu') == 1:
            textInLine = 'encrypt'
        else:textInLine = 'decrypt'
        if auto == True:
            Terminal.print("\t\t\t\t\t Key AutoGenerated to %sting with %s:" %(textInLine, self.CIPHERS_NAME[self.getOptionMenu('menu') - 1]), "reset")
        else:
            Terminal.print("\t\t\t\t\t Key used to %sting with %s:" %(textInLine, self.CIPHERS_NAME[self.getOptionMenu('menu') - 1]), "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (key), "blod")

    def show_processed_text_translated(self, translatedText):
        optionMenu = self.getOptionMenu('submenu') - 1
        textInLine = ''
        if self.getOptionMenu('submenu') == 1:
            textInLine = 'encrypt'
        else:textInLine = 'decrypt'
        Terminal.print("\t\t\t\t\t Text %sed: " % (textInLine), "reset")
        Terminal.print("\t\t\t\t\t\t %s" % (translatedText), "green")
        Terminal.print()
        Terminal.print("\t\t\t\t\t\t PRESS ANY KEY To CONTINUE", "yellow")
        input()

    def cipher_KYPTHON(self):
        print()