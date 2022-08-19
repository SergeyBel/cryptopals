

with open('input.txt') as f:
    lines = f.read().splitlines()


def countBlocks(text: str):
    length = 32
    statistics = {}

    for i in range(0, len(text), length):
        part = text[:length]
        if part in statistics.keys():
            statistics[part] += 1
        else:
            statistics[part] = 1

        text = text[length:]
    return statistics



for hexLine in lines:
    stat = countBlocks(hexLine)
    for c in stat.keys():
        if stat[c] >= 2:
            print ('AES ECB ciphertext:', hexLine)
    
    
