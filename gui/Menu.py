
class Menu(object):
    ROWS = 40
    COLUMNS = 101
    def __init__(self):
        self._option = "0"

    def textGetOption(self):
        #for x in range(1, self.COLUMNS):
        #    print("-"),
        #print()
        self._option = input("\t\t\t\t Inside Option Menu:  ")

    def getOption(self):
        return self._option

    def setOption(self, option):
        self._option = option

    def columns(self):
        return self.COLUMNS

    def rows(self):
        return self.ROWS
