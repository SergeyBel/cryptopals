import base64

class FileReader():
    def readLines(self, filename: str)-> list:
        with open(filename) as f:
            lines = f.read().splitlines()
        return lines
    
    def readBase64(self, filename: str)-> bytearray:
        with open(filename, 'r') as file:
            data = file.read()

        return bytearray(base64.b64decode(data))