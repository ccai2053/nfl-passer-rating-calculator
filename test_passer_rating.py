import unittest
from passer_rating import passer_rating

class TestPasserRating(unittest.TestCase):

    def test_zero_attempts(self):
        # 0 attempts should return 'N/A'
        result = passer_rating(0, 0, 0, 0, 0)
        self.assertEqual(result, 'N/A')
    
    def test_perfect_case(self):
        result = passer_rating(40, 31, 500, 5, 0)
        self.assertEqual(result, '158.3')
    
if __name__ == '__main__':
    unittest.main()