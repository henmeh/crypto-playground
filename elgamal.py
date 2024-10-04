import random
from dhke import DHKE
from helperfunctions.helper import mod_inverse

class ELGAMAL:
    def __init__(self):
        dh = DHKE()
        self.p = dh.p
        self.generator = dh.generator
        keys = dh.get_keys()
        self.private_key = keys["private_key"]
        self.public_key = keys["public_key"]

    def get_key_private_ephemeral(self):
        return random.randint(2, self.p - 2)


    def get_key_public_ephemeral(self, base, private_key_ephemeral):
        return pow(base, private_key_ephemeral, self.p)
    

    def encrypt(self, message: str, key_public: int):
        message_bytes = message.encode('utf-8')
        message_int = int.from_bytes(message_bytes, 'big')

        chiffre = (message_int * key_public) % self.p

        return chiffre.to_bytes(128, "big")
    

    def decrypt(self, chiffre: bytes, key_public_encryption: int):
        chiffre_int = int.from_bytes(chiffre, "big")
        key_public_ephemeral = pow(key_public_encryption, self.private_key, self.p)
        
        inverse = mod_inverse(key_public_ephemeral, self.p)

        decrypted_int = (chiffre_int * inverse) % self.p

        decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big')

        return decrypted_bytes.decode('utf-8')





