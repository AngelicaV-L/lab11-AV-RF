#https://github.com/AngelicaV-L/lab11-AV-RF
#Partner 1: Angelica Velazquez-Lassalle
#Parter 2: Robert F
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(1000,2),1002)



    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,2),1)
        self.assertEqual(subtract(0,0),0)
        self.assertEqual(subtract(100,1),99)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0,2),0)
        self.assertEqual(mul(-1, 5), -5)
        self.assertAlmostEqual(mul(1.2, 3.5), 4.2)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,6 ),3)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
        self.assertAlmostEqual(div(3.2,4.5), 1.40625)
        self.assertEqual(div(3,-9),-3)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,16),4)
        self.assertEqual(logarithm(10,10),1)
        self.assertEqual(logarithm(3,27),3)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,0)
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
          logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-5, -12), 13)
        self.assertEqual(hypotenuse(0, 0), 0)
    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
