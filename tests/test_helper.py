import unittest
import math
import random
from helperfunctions.helper import ggT


class Test(unittest.TestCase):

    def test_ggT_for_correct_result(self):
        self.assertEqual(ggT(356, 238), 2, "Should be 2")
        self.assertEqual(ggT(973, 301), 7, "Should be 7")

        for _ in range(100):
            a = random.randint(0, 10000000)
            b = random.randint(0, 10000000)
            if a > b:
                self.assertEqual(ggT(a, b), math.gcd(a, b))
            else:
                self.assertEqual(ggT(b, a), math.gcd(b, a))
        

    def test_ggT_for_type_error(self):
        with self.assertRaises(TypeError):
            ggT(4.5, 3)
        

    def test_ggT_for_value_error(self):
        with self.assertRaises(ValueError):
            ggT(301, 973)


if __name__ == '__main__':
    unittest.main()