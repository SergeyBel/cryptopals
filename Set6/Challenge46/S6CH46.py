import base64
import sys
import math
from decimal import *

sys.path.append('../../Set5/Challenge39')
sys.path.append('../../Common')

from S5CH39 import Rsa
from IntConverter import IntConverter

class RsaParityOracle:
    def __init__(self) -> None:
        self.rsa = Rsa(512)
    
    def isEven(self, number):
        decrypted = self.rsa.decrypt(number)
        return decrypted % 2 == 0



if __name__ == "__main__":
    text = base64.b64decode('VGhhdCdzIHdoeSBJIGZvdW5kIHlvdSBkb24ndCBwbGF5IGFyb3VuZCB3aXRoIHRoZSBGdW5reSBDb2xkIE1lZGluYQ==')
    converter = IntConverter()
    number = converter.bytesToInt(text)
    oracle = RsaParityOracle()

    encrypted = oracle.rsa.encrypt(number)

    e, n = oracle.rsa.getPublicKey()
    start = Decimal(0)
    finish =Decimal(n)

    c = encrypted
    getcontext().prec = 1024

    while(finish - start > 1):
        c = c * pow(2, e, n)
        
        if oracle.isEven(c):
            finish = (start + finish) / 2
        else:
            start = (start + finish) / 2
    
    findedNumber = int(finish)
    print('Find number', findedNumber)
    print('As text', converter.intToBytes(findedNumber))
    print('Initial text: ', text)
