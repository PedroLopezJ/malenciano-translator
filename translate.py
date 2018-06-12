from translators import *

def getPhraseTranslated(phraseToTranslate):
    if (phraseToTranslate != ""):
        return Translator(phraseToTranslate).translate()
    else:
        return False