# Import your model classes here
from models.restaurant import Restaurant
from models.customer import Customer
from models.review import Review

def test_restaurant_methods():
    # Create an instance of Restaurant and test its methods
    restaurant = Restaurant(1)  # Assuming the ID of an existing restaurant
    print("Restaurant Reviews:", restaurant.reviews())
    print("Restaurant Customers:", restaurant.customers())

def test_customer_methods():
    # Create an instance of Customer and test its methods
    customer = Customer(1)  # Assuming the ID of an existing customer
    print("Customer Reviews:", customer.reviews())
    print("Customer Restaurants:", customer.restaurants())

def test_review_methods():
    # Create an instance of Review and test its methods
    review = Review(1)  # Assuming the ID of an existing review
    print("Review Customer:", review.customer())
    print("Review Restaurant:", review.restaurant())

if __name__ == "__main__":
    test_restaurant_methods()
    test_customer_methods()
    test_review_methods()
