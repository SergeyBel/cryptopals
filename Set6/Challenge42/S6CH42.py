
import sys

sys.path.append('../../Set4/Challenge28')
sys.path.append('../../Set5/Challenge39')
sys.path.append('../../Common')

from S5CH39 import Rsa
from IntConverter import IntConverter
from S4CH28 import Sha1

class BleichenbacherOracle:
    def __init__(self, rsa: Rsa) -> None:
        self.converter = IntConverter()
        self.rsa = rsa
        self.hashLen = 20
        self.hash = Sha1()
        
    
    def verify(self, signature, message):
        packet = self.converter.intToBytes(self.rsa.encrypt(signature))

        index = packet.index(b'\x00\x01')
        index = packet.index(b'\x00', index + 1)
        hash = packet[index + 1: index + 1 + self.hashLen]
        if hash != self.hash.hash(message):
            raise Exception('hash check failed')
        
        return True
        


if __name__ == "__main__":
    sha = Sha1()
    bits = 128
    rsa = Rsa(bits)
    converter = IntConverter()

    message = b'hi mom'
    
    hash = sha.hash(message)
    print(hash)
    
    packetLen = bits // 8
    packet = b'\x00\x01' + b'\xff' * (packetLen - len(hash) - 3) + b'\x00' + hash
    
    signature = rsa.decrypt(converter.bytesToInt(packet))

    oracle = BleichenbacherOracle(rsa)
    print('Verify: ', oracle.verify(signature, message))

