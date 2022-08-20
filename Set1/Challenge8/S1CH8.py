import sys

sys.path.append( '../../Common')
from FileReader import FileReader



def countDuplicateBlocks(data: bytes):
    length = 16
    statistics = {}

    for i in range(0, len(data), length):
        part = data[i: i + length]
        if part in statistics.keys():
            statistics[part] += 1
        else:
            statistics[part] = 1

    return statistics

def detectEcb(data: bytearray):
    stat = countDuplicateBlocks(bytes(data))
    for c in stat.keys():
        if stat[c] >= 2:
            return True

    return False

if __name__ == "__main__":
    f = FileReader()
    lines = f.readLines('input.txt')
    for hexLine in lines:
        if detectEcb(bytearray.fromhex(hexLine)):
            print ('AES ECB ciphertext:', hexLine)
    
    
