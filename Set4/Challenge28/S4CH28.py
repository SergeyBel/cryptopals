import hashlib
 

 

class Sha1Mac():
    def mac(self, message, key):
        return hashlib.sha1(key + message).digest()


if __name__ == "__main__":
    mac  = Sha1Mac()
    key = b"YELLOW SBMARINE"

    print(mac.mac(key, b"SOME MESSAGE"))
    print(mac.mac(key, b"ANOTHER MESSAGE"))