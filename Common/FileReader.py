import base64

class FileReader():
    def readLines(self, filename: str)-> list:
        with open(filename) as f:
            lines = f.read().splitlines()
        return lines
    
    def readBase64Lines(self, filename: str)-> list:
        with open(filename) as f:
            lines = f.read().splitlines()
        
        decodedLines = []
        for line in lines:
            decodedLines.append(bytearray(base64.b64decode(line)))
        return decodedLines
    
    def readBase64Line(self, filename: str)-> bytearray:
        with open(filename, 'r') as file:
            data = file.read()

        return bytearray(base64.b64decode(data))

