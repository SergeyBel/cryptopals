import sys


sys.path.insert(1, '../Challenge3')

from S1CH3 import OneByteXorDecryptor


d = OneByteXorDecryptor()
with open('input.txt') as f:
    lines = f.read().splitlines()
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