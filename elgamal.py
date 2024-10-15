import random
from dhke import DHKE
from helperfunctions.helper import mod_inverse, ggT

class ELGAMAL:
    def __init__(self, bytesize):
        dh = DHKE(bytesize=bytesize)
        self.p =dh.p
        self.generator = dh.generator
        keys = dh.get_keys()
        self.private_key = keys["private_key"]
        self.public_key = keys["public_key"]

    def get_key_private_ephemeral(self):
        return random.randint(2, self.p - 2)
    

    def get_key_private_ephemeral_signing(self):
        inverse_exist = 0
        while inverse_exist != 1:
            key_private_ephemeral_signing = random.randint(2, self.p - 2)
            inverse_exist = ggT(key_private_ephemeral_signing, self.p - 1) 
        
        return key_private_ephemeral_signing


    def get_key_public_ephemeral(self, base, private_key_ephemeral):
        return pow(base, private_key_ephemeral, self.p)
    

    def encrypt(self, message: str, key_public: int):
        message_bytes = message.encode('utf-8')
        message_int = int.from_bytes(message_bytes, 'big')

        chiffre = (message_int * key_public) % self.p

        return chiffre.to_bytes(128, "big")
    

    def decrypt(self, chiffre: bytes, key_public_encryption: int):
        chiffre_int = int.from_bytes(chiffre, "big")
        
        """
        Bei Aussnutzung des kleine Fermat kann auf EEA zur Bestimmung der Inversen von key_public_ephemeral
        verzichtet werden
        """
        #key_public_ephemeral = pow(key_public_encryption, self.private_key, self.p)
        #inverse = mod_inverse(key_public_ephemeral, self.p)

        inverse = pow(key_public_encryption, self.p-1-self.private_key, self.p)

        decrypted_int = (chiffre_int * inverse) % self.p

        decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big')

        return decrypted_bytes.decode('utf-8')
    
    def sign(self, message: str):
        message_bytes = message.encode('utf-8')

        message_int = int.from_bytes(message_bytes, 'big')
        private_key_ephemeral = self.get_key_private_ephemeral_signing()

        r = pow(self.generator, private_key_ephemeral, self.p) 
        s = ((message_int - self.private_key * r) * mod_inverse(private_key_ephemeral, self.p - 1)) % (self.p - 1)

        return (r, s)
    

    def verify(self, message: str, signature: tuple):
        message_bytes = message.encode('utf-8')

        message_int = int.from_bytes(message_bytes, 'big')
        t = (pow(self.public_key, signature[0]) * (pow(signature[0], signature[1]))) % self.p

        return t == pow(self.generator, message_int, self.p)