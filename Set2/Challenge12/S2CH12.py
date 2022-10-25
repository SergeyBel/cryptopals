
import sys
import base64
import string


sys.path.append('../../Set1/Challenge7')
sys.path.append('../Challenge9')
sys.path.append('../../Common/Random')

from S1CH7 import AesEcb
from S2CH9 import Pkcs7
from Random import Random


class EcbOracle():
    def __init__(self, key) -> None:
        self.key = key
        self.ecb = AesEcb()
        self.padding = Pkcs7()
        self.secret = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    def encrypt(self, data: bytearray):
        toEncrypt = self.padding.pad(data + self.secret, 16)
        return self.ecb.encrypt(toEncrypt, self.key)
    
if __name__ == "__main__":
    key = Random().getBytes(16)
    oracle = EcbOracle(key)
    size = 144
    alphabet = string.printable
    answer = bytearray()
    for i in range(size):
        prefix = bytearray('A' * (size - i - 1), 'ascii')
        correct = oracle.encrypt(prefix)
        for c in alphabet:
            tryPrefix = prefix.copy() + answer
            tryPrefix.append(ord(c))
            enc = oracle.encrypt(tryPrefix)          
            if correct[:size] == enc[:size]:
                answer.append(ord(c))
                break
    
    print('Decrypted:')
    print(answer.decode('ascii'))

    









