class Word:

    def __init__(self, word: str):
        self.word = word

    def getWord(self):
        return self.word

    def isLong(self):
        return True if len(self.word) > 3 else False    