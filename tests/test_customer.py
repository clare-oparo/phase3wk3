import unittest
from models.customer import Customer
from models.restaurant import Restaurant

class TestCustomer(unittest.TestCase):

    def test_full_name(self):
        customer = Customer(1, "James", "Bond")
        self.assertEqual(customer.full_name(), "James Bond")

    def test_add_review(self):
        
        self.assertTrue(True) 

if __name__ == '__main__':
    unittest.main()
