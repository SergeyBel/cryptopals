import sys

sys.path.insert(1, '../Challenge3')
sys.path.insert(1, '../../Common')

from S1CH3 import OneByteXorDecryptor
from FileReader import FileReader

if __name__ == "__main__":
    d = OneByteXorDecryptor()
    f = FileReader()
    lines = f.readLines('input.txt')
    min = 1000
    decrypted = None
    key = None
    for hexLine in lines:
        k, m, text = d.decrypt(hexLine)
        if (m < min):
            min = m
            decrypted = text
            key = k
    print(hexLine, decrypted, key)