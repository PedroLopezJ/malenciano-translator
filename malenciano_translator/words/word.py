class Word:

    def __init__(self, word: str):
        self.word = word.replace('ñ', 'ny')

    def getWord(self):
        return self.word

    def isLong(self):
        return True if len(self.word) > 3 else False    

    def isMention(self):
        return True if self.word[0] == "@" else False        