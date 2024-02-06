alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# I misspeled the word in C++ LOL
Ceasar = lambda crypt, key, code=1: "".join([alph[(alph.find(char) + key * code) % 26] for char in crypt])

print(Ceasar("TEST", 3))