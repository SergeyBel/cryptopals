import string
import math


class EnglishFrequency:
    def __init__(self, text: str) -> None:
        self.data = {}
        self.__generate(text)

    
    def __generate(self, text: str)-> None:
        counts = {}
        length = 0
       
        for c in text: 
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1

            length += 1
        
        for c in counts:
            self.data[c] = counts[c] / length
    
    def getFrequency(self, c: int)-> float:
        return self.data[c]
    
    def getChars(self)-> list:
        return self.data.keys()


class EnglishTextMetric:
    ENGLISH_FREQUENCY = {
     'a': 0.0651738,
     'b': 0.0124248,
     'c': 0.0217339,
     'd': 0.0349835,
     'e': 0.1041442,
     'f': 0.0197881,
     'g': 0.0158610,
     'h': 0.0492888,
     'i': 0.0558094,
     'j': 0.0009033,
     'k': 0.0050529,
     'l': 0.0050529,
     'm': 0.0202124,
     'n': 0.0564513,
     'o': 0.0596302,
     'p': 0.0137645,
     'q': 0.0008606,
     'r': 0.0497563,
     's': 0.0515760,
     't': 0.0729357,
     'u': 0.0225134,
     'v': 0.0082903,
     'w': 0.0171272,
     'x': 0.0013692,
     'y': 0.0145984,
     'z': 0.0007836,
     ' ': 0.1918182
    }

    def calculate(self, frequency: EnglishFrequency):
        metric = 0

        for c in frequency.getChars():
            delta = abs(self.ENGLISH_FREQUENCY[c] - frequency.getFrequency(c))
            metric += delta ** 2

        return metric
    
    def getAlphabet(self):
        return self.ENGLISH_FREQUENCY.keys()

def filterNonAlphabetCharacters(text: str, alphabet: list)->str:
    filteredText = ''
    for c in text:
        up = chr(c).lower()
        if up in alphabet:
            filteredText += up
    return filteredText


def decrypt(bytes: bytearray, key: int):
    decrypted = bytearray()
    for c in bytes:
        decrypted.append(c ^ key)
    return decrypted

m = EnglishTextMetric()
bytes = bytearray.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
min = 1000
k = None
for key in range(0, 256):
    decrypted = decrypt(bytes, key)
   
    filteredDecrypted = filterNonAlphabetCharacters(decrypted, m.getAlphabet())
    if filteredDecrypted == '':
        continue

    f = EnglishFrequency(filteredDecrypted)
    metric = m.calculate(f)
    if metric < min:
        min = metric
        k = key
        d = decrypted
print (k, min, d)



