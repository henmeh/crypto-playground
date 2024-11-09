from helperfunctions.ec_point import ECPoint, FieldElement
from helperfunctions.helper import mod_inverse, sha256
import random
import matplotlib.pyplot as plt

class ECC:
    def __init__(self):
        self.p_only_for_plotting = 17
        self.a_only_for_plotting = FieldElement(0, self.p_only_for_plotting)
        self.b_only_for_plotting = FieldElement(7, self.p_only_for_plotting)

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

    
    def get_keys(self)-> dict:
        private_key = random.randint(2, self.p - 2)
        public_key = private_key * self.G

        return {"private_key": private_key, "public_key": public_key}
    

    def get_session_key(self, private_key: int, public_key: ECPoint) -> ECPoint:
        return private_key * public_key


    def sign(self, message: str, private_key: int) -> tuple:
        message_bytes = message.encode('utf-8')
        message_hash_bytes = sha256(message_bytes)
        message_int = int.from_bytes(message_hash_bytes, 'big')
        
        private_key_ephemeral = random.randint(2, self.p - 2)
        R = private_key_ephemeral * self.G
        r = R.x_coordinate.num
        s = ((FieldElement(message_int, self.n) + FieldElement(private_key, self.n) * FieldElement(r, self.n)) / FieldElement(private_key_ephemeral, self.n)).num

        return (r, s)
    

    def verify(self, message: str, public_key: ECPoint, signature: tuple) -> bool:
        message_bytes = message.encode('utf-8')
        message_hash_bytes = sha256(message_bytes)
        message_int = int.from_bytes(message_hash_bytes, 'big')
        
        r = signature[0]
        s = signature[1]
    
        w = (mod_inverse(s, self.n)) % self.n
        u1 = (w * message_int) % self.n
        u2 = (w * r) % self.n
        P = u1 * self.G + u2 * public_key

        return P.x_coordinate.num  == r


    def plot_ecc_curve(self):
        x_vals = []
        y_vals = []
        for x in range(self.p_only_for_plotting):
            rhs = (FieldElement(x, self.p_only_for_plotting)**3 + self.a_only_for_plotting * FieldElement(x, self.p_only_for_plotting) + self.b_only_for_plotting)
            # Check if rhs is a quadratic residue mod p
            for y in range(self.p_only_for_plotting):
                if (FieldElement(y, self.p_only_for_plotting) * FieldElement(y, self.p_only_for_plotting)) == rhs:
                    x_vals.append(x)
                    y_vals.append(y)
        
        plt.figure(figsize=(10, 10))
        plt.scatter(x_vals, y_vals, s=5, color='blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Elliptic Curve: y^2 = x^3 + {self.a_only_for_plotting.num}x + {self.b_only_for_plotting.num} over Finite Field F_{self.p_only_for_plotting}')
        plt.grid(True)
        plt.show()