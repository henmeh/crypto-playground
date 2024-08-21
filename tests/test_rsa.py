import unittest
from rsa import RSA

class Test(unittest.TestCase):

    def test_rsa(self):
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




if __name__ == '__main__':
    unittest.main()