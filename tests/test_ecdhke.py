import unittest
from ecdhke import ECDHKE


class Test(unittest.TestCase):

    def test_equal_session_key(self):
        for _ in range(0, 50):
            a = ECDHKE()
            b = ECDHKE()
            a_keys = a.get_keys()
            b_keys = b.get_keys()

            self.assertEqual(a.get_session_key(a_keys["private_key"], b_keys["public_key"]), b.get_session_key(b_keys["private_key"], a_keys["public_key"]))


if __name__ == '__main__':
    unittest.main()