import sys
import random


sys.path.append('../../Set3/Challenge21')
sys.path.append('../../Common/Random')
from S3CH21 import MersenneTwister
from Random import Random


class MersenneCtr:
    def __init__(self) -> None:
        self.blockSize = 32
        self.rng = MersenneTwister()

    def encrypt(self, data: bytearray, key: int) -> bytearray:
        self.rng.seed(key)
        encrypted = bytearray()
        for i in range(0, len(data), self.blockSize):
            gamma = bytearray()
            for j in range(self.blockSize // 8):
                gamma += self.rng.getRandomNumber().to_bytes(8, 'little')
            encrypted += self.__xor(data[i: i + self.blockSize], gamma)
        return encrypted

    def decrypt(self, data: bytearray, key: int) -> bytearray:
        return self.encrypt(data, key)

    def __xor(self, x: bytearray, y: bytearray) -> bytearray:
        c = bytearray()
        length = min(len(x), len(y))
        for i in range(length):
            c.append(x[i] ^ y[i])
        
        
        return c

def test():
    key = 0xabcd
    data = bytearray('message', 'ascii')
    ctr = MersenneCtr()
    print('Data', data)
    encrypted = ctr.encrypt(data, key)
    print('Encrypted', encrypted)
    decrypted = ctr.decrypt(encrypted, key)
    print('Decrypted', decrypted)

if __name__ == "__main__":
    test()

    key = random.randint(0, 0xffff)
    ctr = MersenneCtr()
    part = bytearray('A' * 14, 'ascii')
    data = Random().getBytes(Random().getInt(1, 40)) + part

    encrypted = ctr.encrypt(data, key)

    for k in range(0xffff):
        decrypted = ctr.decrypt(encrypted, k)
        if decrypted.find(part) != -1:
            print(key, decrypted)



