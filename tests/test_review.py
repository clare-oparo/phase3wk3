import unittest
from models.review import Review
from models.customer import Customer
from models.restaurant import Restaurant

class TestReview(unittest.TestCase):

    def test_full_review(self):
        restaurant = Restaurant(1, "The Test Eatery", 3)
        customer = Customer(1, "Alice", "Wonderland")
        review = Review(1, restaurant.id, customer.id, 5)
        expected_review_text = "Review for The Test Eatery by Alice Wonderland: 5 stars."
        self.assertEqual(review.full_review(), expected_review_text)

if __name__ == '__main__':
    unittest.main()
