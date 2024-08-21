from helperfunctions.helper import ggT, mod_inverse, miller_rabin_test
import random

class RSA:
    def __init__(self):
        while True:
            self.p = int.from_bytes(random.randbytes(128), "big")
            if miller_rabin_test(self.p):
                break

        while True:
            self.q = int.from_bytes(random.randbytes(128), "big")
            if miller_rabin_test(self.q):
                break

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        while True:
            self.e = random.randint(1, self.phi - 1)
            if ggT(self.e, self.phi) == 1:
                break

        self.d = mod_inverse(self.e, self.phi)

    def get_keys(self):
        return {"private_key": (self.d, self.n), "public_key": (self.e, self.n)}

    def encrypt(self, message: str):
        message_bytes = message.encode('utf-8')
        
        message_int = int.from_bytes(message_bytes, 'big')
        chiffre = pow(message_int, self.e, self.n)
        
        byte_length = (self.n.bit_length() + 7) // 8
        return chiffre.to_bytes(byte_length, 'big')

    def decrypt(self, chiffre: bytes):
        message_int = int.from_bytes(chiffre, 'big')
        decrypted_int = pow(message_int, self.d, self.n)
        
        byte_length = (decrypted_int.bit_length() + 7) // 8
        decrypted_bytes = decrypted_int.to_bytes(byte_length, 'big')
        
        return decrypted_bytes.decode('utf-8')