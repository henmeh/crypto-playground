import unittest
from rsa import RSA

class Test(unittest.TestCase):

    def test_rsa_encryption(self):
        messages = [
            "Hallo Henning",
            "Hallo Nadine",
            "Have fun staying poor",
            "32409234882142354387543982347134780"
        ]

        for message in messages:
            a = RSA()
            encrypted_message = a.encrypt(message)
            decrypted_message = a.decrypt(encrypted_message)
            self.assertEqual(decrypted_message, message, f"Should be {message}")


    def test_rsa_signature(self):
        test_cases = [("Hallo Henning", "Hallo Henning", True),
                      ("Hallo Henning", "allo Henning", False),
                     ]

        for test_case in test_cases:
            a = RSA()
            signature = a.sign(test_case[0])
            self.assertEqual(a.verify(test_case[1], signature), test_case[2])


if __name__ == '__main__':
    unittest.main()