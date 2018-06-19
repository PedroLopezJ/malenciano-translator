import sys
from translators import Translator
sys.path.append('.')

def getPhraseTranslated(phraseToTranslate):
    if (phraseToTranslate != ""):
        return Translator(phraseToTranslate).translate()
    else:
        return False