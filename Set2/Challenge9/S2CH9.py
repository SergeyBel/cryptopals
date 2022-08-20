
class Pkcs7():
    def pad(self, bytes: bytearray, bytesLength: int):
        bytesToAdd = bytesLength - (len(bytes) % bytesLength)
        for i in range(bytesToAdd):
            bytes.append(bytesToAdd)
        
        return bytes

if __name__ == "__main__":
    pad = Pkcs7()
    bytes = bytearray('YELLOW SUBMARINE', 'ascii')
    print (pad.pad(bytes, 20))