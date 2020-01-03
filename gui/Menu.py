from gui.Terminal import Terminal

class Menu(object):
    ROWS = 40
    COLUMNS = 101
    def __init__(self):
        self._optionMenu = 0
        self._optionSubMenu = 0

    def inputNumberOptionMenu(self, typeMenu, titleMenu, minOption, maxOption):
        #for x in range(1, self.COLUMNS):
        #    print("-"),
        #print()
        validOptionNumber = False
        while validOptionNumber == False:
            try:
                optionMenu = int(input("\t\t\t\t Inside Option for %s %s:  " % (titleMenu, typeMenu)))
                if (optionMenu >= minOption) and (optionMenu <= maxOption):
                    self.setOptionMenu(typeMenu, optionMenu)
                    validOptionNumber = True
                else:
                    Terminal.print()
                    Terminal.print("\t\t\t\t  WARNING! The input option is not between %s to %s" % (minOption, maxOption), "red")
                    Terminal.print()
            except:
                Terminal.print()
                Terminal.print("\t\t\t\t  ERROR! The input option is not a number. Please, inside between %s to %s" % (minOption, maxOption), "red")
                Terminal.print()

    def getOptionMenu(self, typeMenu):
        if typeMenu == 'menu':
            return self._optionMenu
        if typeMenu == 'submenu':
            return self._optionSubMenu

    def setOptionMenu(self, typeMenu, option):
        if typeMenu == 'menu':
            self._optionMenu = option
        if typeMenu == 'submenu':
            self._optionSubMenu = option
        #print('SET Option %s' % (self._optionMenu))
        #print('SET OptionSub %s' % (self._optionSubMenu))

    def columns(self):
        return self.COLUMNS

    def rows(self):
        return self.ROWS
