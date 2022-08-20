import sys

sys.path.append('../../Set1/Challenge7')
sys.path.append('../../Set1/Challenge2')
sys.path.append('../../Common')

from S1CH7 import AesEcb
from S1CH2 import xorBytes
from FileReader import FileReader



class AesCbc():
    def encrypt(self, text: bytearray, key: bytearray, iv: bytearray):
        aes = AesEcb()
        encrypted = bytearray()
        blockSize = 16
        previous = iv
        for i in range(0, len(text), blockSize):
            block = text[i: i + blockSize]
            encryptedBlock = aes.encryptECB(xorBytes(block, previous), key)
            encrypted.extend(encryptedBlock)
            previous = encryptedBlock
        return encrypted
    
    def decrypt(self, encrypted: bytearray, key: bytearray, iv: bytearray):
        aes = AesEcb()
        decrypted = bytearray()
        blockSize = 16
        previous = iv
        for i in range(0, len(encrypted), blockSize):
            block = encrypted[i: i + blockSize]
            decrypted.extend(xorBytes(aes.decryptECB(block, key), previous))
            previous = block
        return decrypted
    

if __name__ == "__main__":
    f = FileReader()
    a = AesCbc()
    data = f.readBase64('input.txt')
    key = b'YELLOW SUBMARINE'
    iv = bytearray(0x0 for i in range(16))
    print(a.decrypt(data, key, iv))



