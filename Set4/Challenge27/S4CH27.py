import sys

sys.path.append('../../Set1/Challenge2')
sys.path.append('../../Set2/Challenge9')
sys.path.append('../../Set2/Challenge10')


from S2CH10 import AesCbc
from S2CH9 import Pkcs7
from S1CH2 import xorBytes


class CbcAsciiOracle:
    def __init__(self) -> None:
        self.key = b"YELLOW SUBMARINE"
        self.iv = self.key
        self.aes = AesCbc()
        self.padding = Pkcs7()
    
    def encrypt(self, url: str):
        data = bytearray(url, 'ascii')
        return self.aes.encrypt(self.padding.pad(data, 16), self.key, self.iv)
    
    def decrypt(self, data):
        dec  = self.padding.unpad(self.aes.decrypt(data, self.key, self.iv))
        if not all(c < 128 for c in dec):
            raise Exception(dec)
        return dec


if __name__ == "__main__":
    oracle = CbcAsciiOracle()
    zero = b'\x00' * 16
    a = 'A' * 16

    encryptedA = oracle.encrypt(a)
    c = encryptedA[:16]
    pad = encryptedA[16:]
    enc = c + zero + c + pad
    try:
        dec = oracle.decrypt(enc)
    except Exception as e:
        dec = e.args[0]
        print('Key', xorBytes(dec[:16], dec[32:48]))

