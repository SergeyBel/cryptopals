import base64
from Crypto.Cipher import AES


class AesCipher():
    def __init__(self, key) -> None:
        self.aes = AES.new(key, AES.MODE_ECB)
    def encryptECB(self, text: bytearray, key: bytearray):
        aes = AES.new(key, AES.MODE_ECB)
        return aes.encrypt(text)
    
    def decryptECB(self, decrypted: bytearray, key: bytearray):
        aes = AES.new(key, AES.MODE_ECB)
        return self.aes.decrypt(decrypted)
        

with open('input.txt', 'r') as file:
    data = file.read()

data = bytearray(base64.b64decode(data))
key = b'YELLOW SUBMARINE'
aes = AesCipher(key)
print (aes.decryptECB(data).decode('ascii'))