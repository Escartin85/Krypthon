
class DetectingLanguage():

    # Detect English

    UPPERLETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_AND_SPACE = self.UPPERLETTER + self.UPPERLETTER.lower() + ' \t\n'
    ENGLISH_WORDS = ''

    def __init__(self):
        self.ENGLISH_WORDS = self.loadDictionary()

    def loadDictionary():
        dictionaryFile = open('dictionaryEnglish.txt')
        englishWords = {}
        for word in dictionaryFile.read().split('\n'):
            englishWords[word] = None
        dictionaryFile.close()
        return englishWords

    def getEnglishCount(self, text):
        text = text.upper()
        text = self.removeNonLetters(text)
        possibleWords = text.split()

        if possibleWords == []:
            # No words at all, so return 0.0.
            return 0.0 

        matches = 0
        for word in possibleWords:
            if word in self.ENGLISH_WORDS:
                matches += 1
        return float(matches) / len(possibleWords)


    def removeNonLetters(self, text):
        lettersOnly = []
        for symbol in text:
            if symbol in self.LETTERS_AND_SPACE:
                lettersOnly.append(symbol)
        return ''.join(lettersOnly)


    def isEnglish(self, text, wordPercentage=20, letterPercentage=85):
        # By default, 20% of the words must exist in the dictionary file, and
        # 85% of all the characters in the message must be letters or spaces
        # (not punctuation or numbers).
        wordsMatch = self.getEnglishCount(text) * 100 >= wordPercentage
        numLetters = len(self.removeNonLetters(text))
        textLettersPercentage = float(numLetters) / len(text) * 100
        lettersMatch = textLettersPercentage >= letterPercentage
        return wordsMatch and lettersMatch