'''class StringData:
    service = []
    interface = []
    ads = []'''

def ScanFile(path):
    # path
    with open(path, encoding="utf-8") as scan:
         strings = scan.readlines()
    
    strings = [line.strip() for line in strings]

    return strings
