import unittest
from ecc import ECC


class Test(unittest.TestCase):

    def test_ecc_key_exchange(self):
        for _ in range(0, 50):
            a = ECC()
            b = ECC()
            a_keys = a.get_keys()
            b_keys = b.get_keys()

            self.assertEqual(a.get_session_key(a_keys["private_key"], b_keys["public_key"]), b.get_session_key(b_keys["private_key"], a_keys["public_key"]))
    

    def test_signature(self):
        a = ECC()
        keys = a.get_keys()
        private_key = keys["private_key"]
        public_key = keys["public_key"]
    
        test_cases = [("Hallo Henning", "Hallo Henning", private_key, public_key, True),
                      ("Hallo Henning", "allo Henning", private_key, public_key, False),
                      ("Hallo Henning", "Hallo Henning", private_key+1, public_key, False),
                      ("Hallo Henning", "Hallo Henning", private_key, 2*public_key, False),
                     ]

        for test_case in test_cases:            
            signature = a.sign(test_case[0], test_case[2])
            self.assertEqual(a.verify(test_case[1], test_case[3], signature), test_case[4])


if __name__ == '__main__':
    unittest.main()