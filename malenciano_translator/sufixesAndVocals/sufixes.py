sufixes4letters = {}
sufixes4letters['amos'] = "em"
sufixes4letters['imos'] = "im"
sufixes4letters['emos'] = "em"
sufixes4letters['ocos'] = "ocs"

sufixes2letters = {}
sufixes2letters["as"] = "es"
sufixes2letters["es"] = "s"
sufixes2letters["is"] = "es"
sufixes2letters["os"] = "s"
sufixes2letters["us"] = "us"
sufixes2letters["ar"] = ""

sufixes2lettersKeys = list(sufixes2letters.keys())
sufixes4lettersKeys = list(sufixes4letters.keys())

def replaceSufixes(word):
    sufix4letters = word[-4:]
    sufix2letters = word[-2:]

    if(sufix4letters in sufixes4lettersKeys):
        word = word[:-4]+sufixes4letters[sufix4letters]
    elif(sufix2letters in sufixes2lettersKeys):
        word = word[:-2]+sufixes2letters[sufix2letters]

    return word