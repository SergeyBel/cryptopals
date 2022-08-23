import sys


sys.path.append('../Challenge9')
from S2CH9 import Pkcs7


if __name__ == "__main__":
    p  = Pkcs7()
    p.unpad(b"ICE ICE BABY\x01\x02\x03\x04")
    