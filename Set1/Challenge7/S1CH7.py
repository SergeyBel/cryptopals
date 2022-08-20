import sys

sys.path.append('../../Common')

from FileReader import FileReader
from Crypto.Cipher import AES



class AesEcb():
    def encrypt(self, data: bytearray, key: bytearray):
        aes = AES.new(key, AES.MODE_ECB)
        return aes.encrypt(data)
    
    def decrypt(self, encrypted: bytearray, key: bytearray):
        aes = AES.new(key, AES.MODE_ECB)
        return aes.decrypt(encrypted)
        


if __name__ == "__main__":
    f = FileReader()
    data = f.readBase64('input.txt')
    key = b'YELLOW SUBMARINE'
    aes = AesEcb()
    print (aes.decrypt(data, key).decode('ascii'))