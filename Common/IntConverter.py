class IntConverter:
    def bytesToInt(self, bytes: bytearray):
        return int.from_bytes(bytes, 'big')
    
    def intToBytes(self, value: int):
        return value.to_bytes(1024, 'big')