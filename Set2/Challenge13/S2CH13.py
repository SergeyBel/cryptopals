from sre_constants import BRANCH
import urllib.parse
import sys


sys.path.append('../../Set1/Challenge7')
sys.path.append('../Challenge9')
sys.path.append('../../Common/Random')

from S1CH7 import AesEcb
from S2CH9 import Pkcs7
from Random import Random


class UserEncoder:
    def encode(self, email: str):
        return 'email=' + email + '&uid=10&role=user' 
    def decode(self, decoded):
        return dict(urllib.parse.parse_qsl(decoded))

class UserOracle():
    def __init__(self) -> None:
        self.aes = AesEcb()
        self.padding = Pkcs7()
        self.encoder = UserEncoder()
        self.key = Random().getBytes(16)

    
    def encrypt(self, email: str):
        email = email.replace('&', '').replace('=', '')
        enc = self.padding.pad(bytearray(self.encoder.encode(email), 'ascii'), 16)
        return self.aes.encrypt(enc, self.key)
    
    def decrypt(self, encrypted: bytearray):
        dec = self.padding.unpad(self.aes.decrypt(encrypted, self.key))
        return self.encoder.decode(dec.decode('ascii'))


if __name__ == "__main__":
    oracle = UserOracle()
    pkcs = Pkcs7()
    email = 'A' * 10 + bytearray.decode(pkcs.pad(bytearray("admin", 'ascii'), 16), 'ascii')
    enc = oracle.encrypt(email)
    adminBlock = enc[16:32]
    hackEmail = 'A' * 13
    enc2 = oracle.encrypt(hackEmail)
    hack = enc2[:32] + adminBlock
    print(oracle.decrypt(hack))



