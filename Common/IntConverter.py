class IntConverter:
    def bytesToInt(self, bytes: bytearray):
        return int.from_bytes(bytes, 'big')
    
    def intToBytes(self, value: int, bytes = 1024):
        return value.to_bytes(bytes, 'big')