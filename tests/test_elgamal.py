import unittest
from elgamal import ELGAMAL

class Test(unittest.TestCase):

    def test_elgamal_encryption(self):
        # Bob setzt eigenes DLP auf
        bob_dlp = ELGAMAL(bytesize=8)

        # Alice wählt eigenen ephemeral private key
        alice_private_key_ephemeral = bob_dlp.get_key_private_ephemeral()

        # Alice berechnet eigenen public ephemeral and verschlüsselungs key
        alice_public_key_ephemeral = bob_dlp.get_key_public_ephemeral(bob_dlp.generator ,alice_private_key_ephemeral)
        alice_public_key_encryption = bob_dlp.get_key_public_ephemeral(bob_dlp.public_key ,alice_private_key_ephemeral)

        # Alice verschlüsselt ihre message
        messages = [
            "Hallo",
            "Nadine",
            "Bitcoin",
            "8"
        ]

        for message in messages:
            encrypted_message = bob_dlp.encrypt(message, alice_public_key_encryption)
            decrypted_message = bob_dlp.decrypt(encrypted_message, alice_public_key_ephemeral)
            self.assertEqual(decrypted_message, message, f"Should be {message}")
    

    def test_elgamal_signature(self):
        test_cases = [("Hallo Henning", "Hallo Henning", True),
                      ("Hallo Henning", "allo Henning", False),
                     ]
        
        for test_case in test_cases:
            # Bob setzt eigenes DLP auf
            bob = ELGAMAL(bytesize=2)

            signature = bob.sign(test_case[0])

            self.assertEqual(bob.verify(test_case[1], signature), test_case[2])




if __name__ == '__main__':
    unittest.main()