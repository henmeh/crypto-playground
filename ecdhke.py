from helperfunctions.helper import ggT, miller_rabin_test, prime_factors
from helperfunctions.ec_point import ECPoint, FieldElement

import random


class ECDHKE:
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