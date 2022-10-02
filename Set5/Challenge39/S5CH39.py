from Crypto.Util import number
import math


class Rsa:
    def __init__(self) -> None:
        self.e = 3
        self.n = None
        self.d = None
        self.generateKeys(64)
        
    
    def generateKeys(self, bits):
        
        while True:
            p = number.getPrime(bits)
            q = number.getPrime(bits)
            if q != p:
                phi = (p - 1) * (q - 1)
                if math.gcd(self.e, phi) == 1:
                    break
        
        self.n = p * q
        self.d = pow(self.e, -1, phi)
    
    def getPublicKey(self):
        return self.e, self.n
    
    def encrypt(self, number: int)->int:
        return pow(number, self.e, self.n)
    
    def decrypt(self, encrypted: int)->int:
        return pow(encrypted, self.d, self.n)





if __name__ == "__main__":
    rsa  = Rsa()
    num = 42
    encrypted = rsa.encrypt(num)
    decrypted = rsa.decrypt(encrypted)
    
    print('Decrypt correct:', decrypted == num)
