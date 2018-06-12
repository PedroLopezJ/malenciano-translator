import sys
sys.path.append('..')

from words.word import *
from sufixesAndVocals.vocals import vocals, accentMarkedVocals
from sufixesAndVocals.sufixes import *

class LongWord(Word):
    
    def processLastCharacter(self):
        lastLetter = self.word[-1:]
        if(lastLetter in vocals or lastLetter in accentMarkedVocals):   
            self.word = self.word[:-1]    
        else:
            wordWithSufixTranslated = replaceSufixes(self.word)
            if(wordWithSufixTranslated == self.word):
                self.word = self.word[:-1]
            else:
                self.word = wordWithSufixTranslated       

    def replaceLastDforT(self):
        lastCharacter = self.word[-1:]
        penultimateCharacter = self.word[-2:][0]

        if(lastCharacter.lower() == "d" and (penultimateCharacter.lower() in vocals)):
            if(lastCharacter == "d"): self.word = self.word[:-1]+"t"
            elif(lastCharacter == "D"): self.word = self.word[:-1]+"T"
