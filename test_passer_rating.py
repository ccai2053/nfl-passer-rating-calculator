import unittest
from passer_rating import passer_rating

class TestPasserRating(unittest.TestCase):

    def test_zero_attempts(self):
        # 0 attempts should return 'N/A'
        result = passer_rating(0, 0, 0, 0, 0)
        self.assertEqual(result, 'N/A')
    
    def test_perfect_case(self):
        result = passer_rating(31, 40, 500, 5, 0)
        self.assertEqual(result, '158.3')

    def test_zero_rating(self):
        result = passer_rating(3, 10, 30, 0, 1)
        self.assertEqual(result, '0.0')

    def test_invalid_touchdown(self):
        result = passer_rating(2, 2, 20, 4, 0)
        self.assertEqual(result, 'Error: Touchdowns must be between 0 and attempts'
    
if __name__ == '__main__':
    unittest.main()
