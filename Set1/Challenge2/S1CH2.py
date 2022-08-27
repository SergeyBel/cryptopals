def xorBytes(x: bytearray, y: bytearray)->bytearray:
    c = bytearray()
    if (len(x) != len(y)):
        raise Exception('Different length: ' + str(len(x)) + ' ' + str(len(y)))
    length = len(x)
    for i in range(length):
        c.append(x[i] ^ y[i])
    return c
    

if __name__ == "__main__":
    x = bytearray.fromhex(input())
    y = bytearray.fromhex(input())
    c = xorBytes(x, y)
    print(c.hex())