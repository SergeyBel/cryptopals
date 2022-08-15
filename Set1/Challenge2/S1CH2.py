def xorBytes(x: bytearray, y:bytearray)->bytearray:
    c = bytearray()
    if (len(x) != len(y)):
        raise Exception('Different length')
    length = len(x)
    for i in range(length):
        c.append(x[i] ^ y[i])
    return c
    


x = bytearray.fromhex(input())
y = bytearray.fromhex(input())
c = xorBytes(x, y)
print(c.hex())