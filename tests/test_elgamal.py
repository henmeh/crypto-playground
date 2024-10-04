import unittest
from elgamal import ELGAMAL

class Test(unittest.TestCase):

    def test_elgamal(self):
        # Bob setzt eigenes DLP auf
        bob_dlp = ELGAMAL()

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



if __name__ == '__main__':
    unittest.main()