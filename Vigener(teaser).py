def MatchRegister(source, char):
    if source.islower():
        return char.lower()
    return char


CheckIfAlpha = lambda char: char.isalpha() # Silly function, but it's more readable that way


alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def VigenerCore(line, key, direction=1):
    crypt, pos = "", 0
    for char in line:
        if CheckIfAlpha(char):
            if pos > len(key) - 1:
                pos = 0
            crypted_char = alph[(alph.find(char.upper()) + alph.find(key[pos].upper()) * direction) % 26]
            crypt += MatchRegister(char, crypted_char)
            pos += 1
        else:
            crypt += char
    return crypt

print(VigenerCore("Test string", "KEY"))
