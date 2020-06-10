from inspect import getsourcefile
from os.path import abspath
import hashlib
import string
import random
from Crypto.Cipher import AES
from Crypto import Random


class Secur:

    def __init__(self) -> None:
        self.salt = b"SOMEbodyoncetoldme"
        self.IV456 = b"0123456789101112"

    def GenUSKey(self, key: bytes) -> bytes:
        uskey = hashlib.pbkdf2_hmac("sha256", key, self.salt, 100000)
        return uskey

    def Hashing(self, value: bytes) -> bytes:
        hashval = hashlib.sha256(self.salt + value).digest()
        return hashval

    def Encrypt(self, message: bytes, key: bytes) -> bytes:
        message = len(message).to_bytes(length=16, byteorder="big") + message
        rlet = string.ascii_letters[random.randint(0, len(message) % 52)]
        if 16 > len(message):
            txt = message.ljust(16, rlet.encode(encoding="UTF-8"))
        elif len(message) % 16 != 0:
            n = 16 - len(message) % 16 + len(message)
            txt = message.ljust(n, rlet.encode(encoding="UTF-8"))
        else:
            txt = message
        obj = AES.new(key, AES.MODE_CBC, self.IV456)
        ciphertext = obj.encrypt(txt)
        return ciphertext

    def Decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        cipher = AES.new(key, AES.MODE_CBC, self.IV456)
        text = cipher.decrypt(ciphertext)
        size = text[:16]
        sizel = int.from_bytes(size, byteorder="big")
        text = text[16:sizel + 16]
        return text

    def GenSKey(self) -> bytes:
        return Random.new().read(32)
