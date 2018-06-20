import sys
sys.path.append('..')
from malenciano_translator.translators import Translator

def getPhraseTranslated(phraseToTranslate):
    if (phraseToTranslate != ""):
        return Translator(phraseToTranslate).translate()
    else:
        return False