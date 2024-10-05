import unittest
from helperfunctions.fieldelement import FieldElement
from helperfunctions.ec_point import ECPoint

class Test(unittest.TestCase):
    def test_init_for_value_error(self):
        with self.assertRaises(ValueError, msg="-2, 4 is not on the curve"):
            ECPoint(-2, 4, 5, 7)


    def test_init_for_none(self):
        point = ECPoint(None, None, 0, 0) 
        self.assertEqual(point.x_coordinate, None)
        self.assertEqual(point.y_coordinate, None)
        self.assertEqual(point.a_param, 0)
        self.assertEqual(point.b_param, 0)
    

    def test_init_true_point(self):
        point = ECPoint(3, 7, 5, 7) 
        self.assertEqual(point.x_coordinate, 3)
        self.assertEqual(point.y_coordinate, 7)
        self.assertEqual(point.a_param, 5)
        self.assertEqual(point.b_param, 7)
    
    
    def test_eq(self):
        test_cases = [(ECPoint(3, -7, 5, 7) == ECPoint(3, -7, 5, 7), True),
                      (ECPoint(3, -7, 5, 7) == ECPoint(18, 77, 5, 7), False),
                      (ECPoint(3, -7, 5, 7) != ECPoint(18, 77, 5, 7), True),
                      (ECPoint(3, -7, 5, 7) != ECPoint(3, -7, 5, 7), False)]
        

        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])
    

    def test_repr(self):
        test_cases = [(repr(ECPoint(None, None, 5, 7)), "Point(infinity)_5_7"),
                      (repr(ECPoint(3, -7, 5, 7)), "Point(3,-7)_5_7"),
                      (repr(ECPoint(FieldElement(192, 223), FieldElement(105, 223), FieldElement(0, 223), FieldElement(7, 223))), "Point(192,105)_0_7_223")]


        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])


    def test_add(self):
        test_cases = [(ECPoint(None, None, 5, 7) + ECPoint(2, 5, 5, 7), ECPoint(2, 5, 5, 7)),
                      (ECPoint(2, 5, 5, 7) + ECPoint(None, None, 5, 7), ECPoint(2, 5, 5, 7)),
                      (ECPoint(2, 5, 5, 7) + ECPoint(2, -5, 5, 7), ECPoint(None, None, 5, 7)),
                      (ECPoint(3, 7, 5, 7) + ECPoint(-1, -1, 5, 7), ECPoint(2, -5, 5, 7)),
                      (ECPoint(0, 0, 0, 0) + ECPoint(0, 0, 0, 0), ECPoint(None, None, 0, 0)),
                      (ECPoint(-1, 1, 5, 7) + ECPoint(-1, 1, 5, 7), ECPoint(18, -77, 5, 7))]
        
        for test_case in test_cases:
            self.assertEqual(test_case[0], test_case[1])

        with self.assertRaises(TypeError, msg="Points Point(3,7)_5_7, Point(infinity)_4_5 are not on the same curve"):
            ECPoint(3, 7, 5, 7) + ECPoint(None, None, 4, 5)
    

    def test_add_for_adding_fieldelements(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        test_cases = [(192, 105, 17, 56, 170, 142), (47, 71, 117, 141, 60, 139), (143, 98, 76, 66, 47, 71)]

        for test_case in test_cases:
            x1 = FieldElement(test_case[0], prime)
            y1 = FieldElement(test_case[1], prime)
            p1 = ECPoint(x1, y1, a, b)
            
            x2 = FieldElement(test_case[2], prime)
            y2 = FieldElement(test_case[3], prime)
            p2 = ECPoint(x2, y2, a, b)
            
            x3 = FieldElement(test_case[4], prime)
            y3 = FieldElement(test_case[5], prime)
            p3 = ECPoint(x3, y3, a, b)
            
            self.assertEqual(p1 + p2, p3)
    

    def test_rmul(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        
        test_cases = [(2, 192, 105, 49, 71), (2, 143, 98, 64, 168), (2, 47, 71, 36, 111), (4, 47, 71, 194, 51), (8, 47, 71, 116, 55), (21, 47, 71, None, None)]

        for test_case in test_cases:

            x1 = FieldElement(test_case[1], prime)
            y1 = FieldElement(test_case[2], prime)
            p1 = ECPoint(x1, y1, a, b)
            
            if test_case[3] is None:
                p2 = ECPoint(None, None, a, b)
            else:
                x2 = FieldElement(test_case[3], prime)
                y2 = FieldElement(test_case[4], prime)
                p2 = ECPoint(x2, y2, a, b)

            assert test_case[0] * p1 == p2


if __name__ == '__main__':
    unittest.main()