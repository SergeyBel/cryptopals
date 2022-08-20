import sys


sys.path.append('../Challenge3')
sys.path.append('../Challenge5')
sys.path.append('../../Common')

from S1CH3 import OneByteXorDecryptor
from S1CH5 import xorEncrypt
from FileReader import FileReader


def bytebyteBitsDiff(x: int, y: int)->int:
    c = x ^ y
    bits = 0
    while c > 0:
        bits += c % 2
        c = c // 2
    return bits

def hammingDistance(x: bytearray, y: bytearray)->int:
    if len(x) != len(y):
        raise Exception('Hamming distance strings not equals length')
    dist = 0
    for i in range(len(x)):
            dist += bytebyteBitsDiff(x[i], y[i])
    return dist



def detectKeyLength(text: bytearray)->int:
    min = 1000
    length = None
    for keyLength in range (2, 41):
        part1 = text[:keyLength]
        part2 = text[keyLength:2 * keyLength]
        part3 = text[2 * keyLength:3 * keyLength]
        part4 = text[3 * keyLength:4 * keyLength]
        h = (hammingDistance(part1, part2) + hammingDistance(part1, part3) + hammingDistance(part1, part4) + hammingDistance(part2, part3)+ hammingDistance(part2, part4) + + hammingDistance(part3, part4)) / 6 / keyLength 
        if (h < min):
            min = h
            length = keyLength
    return length

def transpose(text: bytearray, length: int):
    lines = [bytearray() for i in range(length)]
    counter = 0
    for t in text:
        lines[counter].append(t)
        counter  = (counter + 1) % length
    return lines

def findKey(transposed: list):
    d = OneByteXorDecryptor()
    key = bytearray()
    for i in range(keyLength):
        k, metric, text = d.decrypt(transposed[i].hex())
        key.append(k)
    return key


if __name__ == "__main__":
    f = FileReader()
    data = f.readBase64('input.txt')
    keyLength = detectKeyLength(data)
    print ('KEYLENGTH=', keyLength)

    transposed = transpose(data, keyLength)
    key = findKey(transposed)

    print('Key', key)
    print ("Decrypted:")
    decrypted = xorEncrypt(data, key)
    print (decrypted.decode("ascii"))


    #manual part

    key = bytearray('Terminator X: Bring the noise', 'ascii')
    print ("Decrypted:")
    decrypted = xorEncrypt(data, key)
    print (decrypted.decode("ascii"))





