import zipfile
from itertools import product

class ProgrammData():
    def __init__(self):
        self.chars = "".join([string.strip() for string in open("chars.txt", encdosing="utf-8")])

def Pick(target, pick):
    try:
        target.extractall(pwd=pick)
    except:
        print(f"Combination {pick} unseccessful")
    else:
        print(f"Combination {pick} succeeded!")
        exit(0)

data = ProgrammData()
archive = zipfile.ZipFile("archive.zip")
#passwords = open('имя_файла_с_паролями.txt', 'rb')

def Brute(target, blind_mode=True):
    if blind_mode:
        for length in range(1, 21):
            for password in product(data.chars, repeat=length):
                Pick(target, "".join(password))
    else:
        pwd_set = [i.strip() for i in open("password_list.txt", encoding="utf-8")]
        for password in pwd_set:
            Pick(target, password)