from helperfunctions.helper import ggT, miller_rabin_test, prime_factors
import random

class DHKE:
    def __init__(self, prime=None, generator=None, bytesize=8):
        
        if prime is not None and generator is not None:
            self.p = prime
            self.generator = generator
        
        else:
            while True:
                self.p = int.from_bytes(random.randbytes(bytesize), "big")
                if miller_rabin_test(self.p):
                    break
            
            self.generator = self.find_generator()


    def is_generator(self, g, n, factors):
        phi_n = n - 1
        if pow(g, phi_n, n) != 1:
            return False
        
        for factor in factors:
            if pow(g, phi_n // factor, n) == 1:
                return False
        
        return True
                

    def find_generator(self):
        factors = prime_factors(self.p-1)
    
        for g in range(2, self.p):
            if ggT(g, self.p) == 1 and self.is_generator(g, self.p, factors):
                return g
        
        return None
    
    
    def get_keys(self):
        private_key = random.randint(2, self.p - 2)
        public_key = pow(self.generator, private_key, self.p)

        return {"private_key": private_key, "public_key": public_key}
    

    def get_session_key(self, private_key, public_key):
        return pow(public_key, private_key, self.p)