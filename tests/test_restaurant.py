import unittest
from models.restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def test_fanciest(self):
        self.assertIsNone(Restaurant.fanciest())  # Assuming no restaurants are added yet

if __name__ == '__main__':
    unittest.main()
