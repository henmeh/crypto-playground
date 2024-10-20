from helperfunctions.ec_point import ECPoint, FieldElement
from helperfunctions.helper import mod_inverse

import random


class ECC:
    def __init__(self):
        self.p = 2 ** 256 - 2 ** 32 - 977
        self.n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        self.a = FieldElement(0, self.p)
        self.b = FieldElement(7, self.p)
        self.G = ECPoint(
            FieldElement(
                0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, self.p
            ),
            FieldElement(
                0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8, self.p
            ),
            self.a,
            self.b,
        )

    
    def get_keys(self):
        private_key = random.randint(2, self.p - 2)
        public_key = private_key * self.G

        return {"private_key": private_key, "public_key": public_key}
    

    def get_session_key(self, private_key, public_key):
        return private_key * public_key


    def sign(self, message: str, private_key:int):
        message_bytes = message.encode('utf-8')
        message_int = int.from_bytes(message_bytes, 'big')
        
        private_key_ephemeral = random.randint(2, self.p - 2)
        R = private_key_ephemeral * self.G
        r = R.x_coordinate.num
        s = ((FieldElement(message_int, self.n) + FieldElement(private_key, self.n) * FieldElement(r, self.n)) / FieldElement(private_key_ephemeral, self.n)).num

        return (r, s)
    

    def verify(self, message: str, public_key: "ECPoint", signature: tuple):
        message_bytes = message.encode('utf-8')
        message_int = int.from_bytes(message_bytes, 'big')
        
        r = signature[0]
        s = signature[1]
    
        w = (mod_inverse(s, self.n)) % self.n
        u1 = (w * message_int) % self.n
        u2 = (w * r) % self.n
        P = u1 * self.G + u2 * public_key

        return P.x_coordinate.num  == r
