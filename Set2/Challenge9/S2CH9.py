
class Pkcs7():
    def pad(self, data: bytearray, bytesLength: int):
        bytesToAdd = bytesLength - (len(data) % bytesLength)
        for i in range(bytesToAdd):
            data.append(bytesToAdd)
        
        return data
    
    def unpad(self, data: bytearray)->bytearray:
        lastByte = data[-1]
        length = int(lastByte)
        for i in range(length):
            if data[len(data) - i - 1] != lastByte:
                raise Exception('incorrect pkcs7 padding')
        
        unpadded = data[:-length]
        return unpadded




if __name__ == "__main__":
    pad = Pkcs7()
    bytes = bytearray('YELLOW SUBMARINE', 'ascii')
    padded = pad.pad(bytes, 20)
    print(padded)
    print(pad.unpad(padded))
