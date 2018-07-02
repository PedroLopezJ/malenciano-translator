from .translators import Translator

def getPhraseTranslated(phraseToTranslate):
    if (phraseToTranslate != ""):
        return Translator(phraseToTranslate).translate()
    else:
        return False
