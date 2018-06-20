
import unidecode
from words.word import Word
from words.short_word import ShortWord
from words.long_word import LongWord
    
def removeAccents(phrase: str):
    return unidecode.unidecode(phrase)    

class Translator:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def processWord(self, word: str):
        word = Word(word)

        if(word.isMention() == False):
            if word.isLong():
                word = LongWord(word.getWord())
                word.processLastCharacter()
                word.replaceLastDforT()
                return word.getWord()
            else:
                word = ShortWord(word.getWord())
                word.process3letterWords()
                word.replaceSpecialWords()
                word.replaceYforI()
                return word.getWord()
        else:
            return word.getWord()     

    def splitPhrase(self):   
        return self.phrase.split()

    def translate(self):
        self.phrase = ' '.join(list(map(self.processWord, self.splitPhrase())))
        return self.phrase    
        