from random import randint, shuffle


CreateTermList = lambda sequence: [bool(value) for value in sequence]


CloneChars = lambda chars, terms: "".join([chars[i] for i in range(len(terms)) if terms[i]])


def ProcessPwd(pwd, string):
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i + 1]:
            char = string[randint(0, len(string) - 1)]
            while pwd.count(char) != 0:
                char = string[randint(0, len(string) - 1)]
            pwd = pwd[:i + 1] + char + pwd[i + 2:]
    return pwd


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
