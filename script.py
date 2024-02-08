alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


CheckIfChar = lambda char: char.isalpha()


def MatchRegister(source, char):
    if source.islower():
        return char.lower()
    return char


def CeasarCore(line, key, direction=1):
    crypt = ""
    for char in line:
        if CheckIfChar(char):
            crypted_char = alph[(alph.find(char.upper()) + key * direction) % 26]
            crypt += MatchRegister(char, crypted_char)
        else:
            crypt += char
    return crypt

