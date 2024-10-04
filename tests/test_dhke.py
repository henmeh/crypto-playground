import unittest
from dhke import DHKE


class Test(unittest.TestCase):

    def test_equal_session_key(self):
        for _ in range(0, 500):
            a = DHKE(bytesize = 8)
            b = DHKE(prime = a.p, generator = a.generator)
            a_keys = a.get_keys()
            b_keys = b.get_keys()

            self.assertEqual(a.get_session_key(a_keys["private_key"], b_keys["public_key"]), b.get_session_key(b_keys["private_key"], a_keys["public_key"]))
