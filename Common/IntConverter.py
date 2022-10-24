class IntConverter:
    def bytesToInt(self, bytes: bytearray)->int:
        return int.from_bytes(bytes, 'big')
    
    def intToBytes(self, value: int, bytes: int = 1024)->bytearray:
        return value.to_bytes(bytes, 'big')