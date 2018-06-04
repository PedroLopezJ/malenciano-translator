import sys
sys.path.append('../')

from malencianoTranslator.words.word import *
from malencianoTranslator.words.special_words import *
from malencianoTranslator.sufixesAndVocals.vocals import vocals, accentMarkedVocals

class ShortWord(Word):
    def replaceYforI(self):
      
        if len(self.word) == 2 and (self.word[1] == ',' or self.word[1] == '.'):
            wordWithoutSpecialCharacters = self.word[:1]
        else:
            wordWithoutSpecialCharacters = self.word

        self.word = self.word.replace('y', 'i') if len(wordWithoutSpecialCharacters) == 1 else self.word

    def process3letterWords(self):
        if(len(self.word) == 3):
            lastCharacter = self.word[-1:]
            penultimateCharacter = self.word[-2:][0]

            if(lastCharacter.isalpha() and penultimateCharacter.isalpha()):
                if((lastCharacter in vocals or lastCharacter in accentMarkedVocals) and penultimateCharacter not in vocals):
                    self.word = self.word[:-1]

    def replaceSpecialWords(self):
        if(self.word in specialWordsKeys):
            self.word = specialWords[self.word]