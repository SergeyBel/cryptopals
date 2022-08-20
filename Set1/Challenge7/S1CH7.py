import sys

sys.path.append('../../Common')

from FileReader import FileReader
from Crypto.Cipher import AES



class AesEcb():
    def encryptECB(self, text: bytearray, key: bytearray):
        aes = AES.new(key, AES.MODE_ECB)
        return aes.encrypt(text)
    
    def decryptECB(self, decrypted: bytearray, key: bytearray):
        aes = AES.new(key, AES.MODE_ECB)
        return aes.decrypt(decrypted)
        


if __name__ == "__main__":
    f = FileReader()
    data = f.readBase64('input.txt')
    key = b'YELLOW SUBMARINE'
    aes = AesEcb()
    print (aes.decryptECB(data, key).decode('ascii'))