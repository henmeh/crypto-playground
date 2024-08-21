from helperfunctions.helper import ggT, mod_inverse, miller_rabin_test
import random

class RSA():
    def __init__(self) -> dict:
        while True:
            self.p = int.from_bytes(random.randbytes(128), "big")
            if miller_rabin_test(self.p) == True:
                break
        
        while True:
            self.q = int.from_bytes(random.randbytes(128), "big")
            if miller_rabin_test(self.p) == True:
                break
            
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        
        while True:
            self.e = random.randint(1, self.phi-1)
            if ggT(self.e, self.phi) == 1:
                break

        self.d = mod_inverse(self.e, self.phi)


    def get_keys(self):
        return {"private_key": (self.d, self.n), "public_key": (self.e, self.n)}


    def encrypt(self, message):
        # Convert message to an integer and encrypt
        chiffre = pow(int.from_bytes(message, "big"), self.e, self.n)
        
        # Ensure the ciphertext is the same length as n
        byte_length = (self.n.bit_length() + 7) // 8
        return chiffre.to_bytes(byte_length, "big")

    def decrypt(self, chiffre):
        # Convert ciphertext to an integer and decrypt
        message = pow(int.from_bytes(chiffre, "big"), self.d, self.n)
        
        # Ensure the decrypted message is the same length as the original
        byte_length = (self.n.bit_length() + 7) // 8
        return message.to_bytes(byte_length, "big")

a = RSA()
#print(a.get_keys())
x = 4321432
#print(x.to_bytes(258, "big"))
#print(int.from_bytes(random.randbytes(258), "big"))
print(x)
y = a.encrypt(x.to_bytes(128, "big"))
print(y)
x = a.decrypt(y)
print(int.from_bytes(x, "big"))