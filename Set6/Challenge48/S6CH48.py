import sys


sys.path.append('../../Set5/Challenge39')
sys.path.append('../../Common')

from S5CH39 import Rsa
from IntConverter import IntConverter


class PkcsRsaOracle:
    def __init__(self, k):
        self.k = k
        bits = (k // 2) * 8
        self.rsa = Rsa(bits)
        self.converter = IntConverter()
    
    def isCorrect(self, number):
        decrypt = self.rsa.decrypt(number)
        bytes = self.converter.intToBytes(decrypt, self.k)
        return bytes[0] == 0x00 and bytes[1] == 0x02
    
def pkcsPad(data, k):
    d = len(data)
    pad = b'\xff' * (k - d - 3)
    return b'\x00\x02' + pad + b'\x00' + data


class Segment:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    

    def length(self):
        return self.b - self.a
    
    def isPoint(self):
        return self.length() == 0
    
    def __str__(self) -> str:
        return '[' + str(self.a) + ',' + str(self.b) + ']'
    
    def __eq__(self, __o: object) -> bool:
        return self.a == __o.a and self.b == __o.b
    
    def __hash__(self) -> int:
        return hash(str(self.a) + str(self.b))


def ceil(x, y):
    return x // y + int(x % y != 0)


def findS(start, oracle, c, e, n):
    s = start
    while True:
        cn = c * pow(s, e, n)
        if oracle.isCorrect(cn):
            break

        s += 1
    
    return s

def unionOneSegment(segment, s, n, B):
    a = segment.a
    b = segment.b

    r1 = (a * s - 3 * B + 1) // n
    r2 = (b * s - 2 * B) // n

    print('r', r1, r2, r2 - r1)

    newSegments = set()

    for r in range(r1, r2 + 1):
        start = max(a, ceil((2 * B + r * n), s))
        finish = min(b, (3 * B - 1 + r * n) // s)
        print(start, finish)
        if (start <= finish):
            sgm = Segment(start, finish)
            if sgm not in newSegments:
                print(sgm)
                newSegments.add(sgm)
    
    return newSegments

def union(M, s, n, B):
    print('union')
    newM = set()
    for segment in M:
        newM = newM.union(unionOneSegment(segment, s, n, B))
    
    return newM


def printM(M):
    for segment in M:
        print(segment, segment.length(),)
    print()


def findSForOneSegment(a, b, sPrev, B, c, e, n):
    r = 2 * (b * sPrev - B) // n

    while True:
        for s in range((2 * B + r * n) // b, (3 * B + r * n) // a + 1):
            cn = c * pow(s, e, n)
            if oracle.isCorrect(cn):
                return s
        r += 1




if __name__ == "__main__":
    k = 6
    B = 2 ** (8 * (k - 2))
    oracle = PkcsRsaOracle(k)
    converter = IntConverter()
    e, n = oracle.rsa.getPublicKey()
    

    data = b"H"
    padData = pkcsPad(data, k)
    number = converter.bytesToInt(padData)
    
    c = oracle.rsa.encrypt(number)

    M = set([Segment(2 * B, 3 * B)])

    print('Start find s1')
    s = findS(n // (3 * B), oracle, c, e, n)
    print('s1 = ', s)
    M = union(M, s, n, B)
    printM(M)
 


    while True:
        if len(M) == 0:
            print('LEN = 0')
            break
        if (len(M) >= 2):
            print('two')
            s = findS(s + 1, oracle, c, e, n)
            print('s = ', s)
            M = union(M, s, n, B)
            printM(M)
            continue
        elif (len(M) == 1):
            print('one')
            segment = M.pop()
            M.add(segment)
            if segment.isPoint():
                print ('finded')
                break
            s = findSForOneSegment(segment.a, segment.b, s, B, c, e, n)
            M = union(M, s, n, B)
            print('After one')
            printM(M)
            continue
    
    print('Number=', number)
    printM(M)
    
    













