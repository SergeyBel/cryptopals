
class Pkcs7():
    def pad(self, data: bytearray, bytesLength: int):
        bytesToAdd = bytesLength - (len(data) % bytesLength)
        for i in range(bytesToAdd):
            data.append(bytesToAdd)
        
        return data

if __name__ == "__main__":
    pad = Pkcs7()
    bytes = bytearray('YELLOW SUBMARINE', 'ascii')
    print (pad.pad(bytes, 20))
