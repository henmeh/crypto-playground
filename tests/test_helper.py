import unittest
import math
import random
from helperfunctions.helper import ggT, eea, mod_inverse


class Test(unittest.TestCase):

    def test_ggT_for_correct_result(self):
        self.assertEqual(ggT(356, 238), 2, "Should be 2")
        self.assertEqual(ggT(973, 301), 7, "Should be 7")

        for _ in range(100):
            a = random.randint(0, 10000000)
            b = random.randint(0, 10000000)
            self.assertEqual(ggT(a, b), math.gcd(a, b))
        

    def test_ggT_for_type_error(self):
        with self.assertRaises(TypeError):
            ggT(4.5, 3)
            ggT(4, 3.5)
            ggT(4.5, 3.5)
    

    def test_eea_for_correct_result(self):
        self.assertEqual(eea(4, 27), (1, 7, -1), "Should be (1, 7, -1)")
        self.assertEqual(eea(6, 29), (1, 5, -1), "Should be (1, 5, -1)")
        self.assertEqual(eea(8, 3), (1, -1, 3), "Should be (1, -1, 3)")
        self.assertEqual(eea(7, 5), (1, -2, 3), "Should be (1, -2, 3)")
        self.assertEqual(eea(3, 4), (1, -1, 1), "Should be (1, -1, 1)")
        self.assertEqual(eea(4, 2), (2, 0, 1), "Should be (2, 0, 1)")


    def test_eea_for_type_error(self):
        with self.assertRaises(TypeError):
            eea(4.5, 3)
            eea(4, 3.5)
            eea(4.5, 3.5)
    

    def test_mod_inverse_for_correct_result(self):
        self.assertEqual(mod_inverse(4, 27), 7, "Should be 7")
        self.assertEqual(mod_inverse(6, 29), 5, "Should be 5")
        self.assertEqual(mod_inverse(8, 3), 2, "Should be 2")
        self.assertEqual(mod_inverse(7, 5), 3, "Should be 1")
        self.assertEqual(mod_inverse(3, 4), 3, "Should be 1")
    

    def test_mod_inverse_for_value_error(self):
        with self.assertRaises(ValueError):
            mod_inverse(4, 2)
    

    def test_mod_inverse_for_type_error(self):
        with self.assertRaises(TypeError):
            mod_inverse(4.5, 3)
            mod_inverse(4, 3.5)
            mod_inverse(4.5, 3.5)
        

if __name__ == '__main__':
    unittest.main()