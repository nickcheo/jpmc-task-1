import unittest
from client import getRatio
class TestMethods(unittest.TestCase):
    def test_getRatio_normal(self):
        price_a = 10
        price_b = 10
        result = getRatio(price_a, price_b)
        expectedResult = 1
        self.assertEqual(expectedResult, result)
    def test_getRatio_edge1(self):
        price_a = 0
        price_b = 100000
        result = getRatio(price_a, price_b)
        expectedResult = 0
        self.assertEqual(expectedResult, result)
    def test_getRatio_edge2(self):
        price_a = 120
        price_b = 1
        result = getRatio(price_a, price_b)
        expectedResult = 120
        self.assertEqual(expectedResult, result)
        
if __name__ == '__main__':
    unittest.main()