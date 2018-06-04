class Word:

    def __init__(self, word: str):
        self.word = word

    def getWord(self):
        return self.word

    def isValidToProcess(self):
        return True if len(self.word) > 3 else False    