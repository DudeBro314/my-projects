from random import randint, shuffle


CreateTermList = lambda sequence: [bool(value) for value in sequence]


CloneChars = lambda chars, terms: "".join([chars[i] for i in range(len(terms)) if terms[i]])


def MixSequence(sequence, repeat=1):
    for reps in range(repeat):
        shuffle(sequence)
    return "".join(sequence)


def GeneratePwd(pwd_len, pwd_chars):
    result = []
    match len(pwd_chars) == 0:
        case True:
            return "Error"
        case False:
            result = []
            for char in range(pwd_len):
                result.append(pwd_chars[randint(0, len(pwd_chars) - 1)])
            #MixSequence(result, 3)
            return "".join(result)
