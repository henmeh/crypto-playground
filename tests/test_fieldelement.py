import unittest
from helperfunctions.fieldelement import FieldElement

class Test(unittest.TestCase):

    def test_init_for_value_error(self):
        with self.assertRaises(ValueError, msg="Num 10 not in field range 0 to 2"):
            FieldElement(10,3)


    def test_init_correct(self):
        x = FieldElement(3,10)

        self.assertEqual(x.num, 3)
        self.assertEqual(x.prime, 10)


    def test_repr(self):
        x = FieldElement(3,10)

        self.assertEqual(repr(x), "FieldElement_3(10)")


    def test_eq(self):
        test_cases = [(FieldElement(3,10) != FieldElement(4,10), True),
                      (FieldElement(3,10) == FieldElement(4,10), False),
                      (FieldElement(3,10) == FieldElement(3,10), True),
                      (FieldElement(3,10) != FieldElement(3,10), False)]
        
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])
    

    def test_add(self):
        test_cases = [(FieldElement(2,31) + FieldElement(15,31), FieldElement(17,31)),
                      (FieldElement(17,31) + FieldElement(21,31), FieldElement(7,31))]
        
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])

        with self.assertRaises(TypeError, msg="Numbers must be in the same modulo field"):
            FieldElement(17,30) + FieldElement(21,31)


    def test_sub(self):
        test_cases = [(FieldElement(29,31) - FieldElement(4,31), FieldElement(25,31)),
                      (FieldElement(15,31) - FieldElement(30,31), FieldElement(16,31))]
        
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])

        with self.assertRaises(TypeError, msg="Numbers must be in the same modulo field"):
            FieldElement(17,30) - FieldElement(21,31)
    

    def test_mul(self):
        test_cases = [(FieldElement(24,31) * FieldElement(19,31), FieldElement(22,31))]
        
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])

        with self.assertRaises(TypeError, msg="Numbers must be in the same modulo field"):
            FieldElement(17,30) * FieldElement(21,31)
    

    def test_pow(self):
        test_cases = [(FieldElement(17,31)**3, FieldElement(15,31)),
                      (FieldElement(5,31)**5 * FieldElement(18,31), FieldElement(16,31))]
        
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])
    

    def test_div(self):
        test_cases = [(FieldElement(3,31) / FieldElement(24,31), FieldElement(4,31)),
                      (FieldElement(17,31)**-3, FieldElement(29,31)),
                      (FieldElement(4,31)**-4 * FieldElement(11,31), FieldElement(13,31))]
        
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])

        with self.assertRaises(TypeError, msg="Numbers must be in the same modulo field"):
            FieldElement(17,30) / FieldElement(21,31)
    

    def test_rmul(self):
        test_cases = [(27 * (FieldElement(3,31)), FieldElement(19,31))]
                      
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])
 


if __name__ == '__main__':
    unittest.main()