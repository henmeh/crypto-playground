import unittest
import math
import random
from helperfunctions.helper import ggT


class Test(unittest.TestCase):

    def test_ggT_for_correct_result(self):
        self.assertEqual(ggT(356, 238), 2, "Should be 2")

        for _ in range(100):
            a = random.randint(0, 10000)
            b = random.randint(0, 10000)
            self.assertEqual(ggT(a, b), math.gcd(a, b))

        
    def test_ggT_for_type_error(self):
        with self.assertRaises(TypeError):
            ggT(4.5, 3)



if __name__ == '__main__':
    unittest.main()