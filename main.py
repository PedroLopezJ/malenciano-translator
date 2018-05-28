from translators import *

if __name__ == "__main__":
    phraseToTranslate = input()
else:
    phraseToTranslate = "frase base"    

phraseTranslated = Translator(phraseToTranslate).translate()

#.split()
print(phraseTranslated)