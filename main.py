from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

def test_customer_methods():
    print("Testing Customer Methods:")
    customer = Customer(1)  
    print(f"Full Name: {customer.full_name()}")
    
    favorite = customer.favorite_restaurant()
    if favorite:
        print(f"Favorite Restaurant: {favorite.name}")
    else:
        print("Favorite Restaurant: None")
    
    # Add a review 
    customer.add_review(Restaurant(1), 5)
    print("Added a new review.")
    
    # Delete reviews for a Restaurant 
    customer.delete_reviews(Restaurant(1))
    print("Deleted reviews for Restaurant 1.\n")

def test_restaurant_methods():
    print("Testing Restaurant Methods:")
    # Testing fanciest method
    fanciest_restaurant = Restaurant.fanciest()
    print(f"Fanciest Restaurant: {fanciest_restaurant.name}")
    
    # Testing all_reviews method for a specific restaurant
    restaurant = Restaurant(1)  
    reviews = restaurant.all_reviews()
    print(f"All Reviews for {restaurant.name}:")
    for review in reviews:
        print(review)
    print()

def test_review_methods():
    print("Testing Review Methods:")
    review = Review(2)  
    print(review.full_review())
    print()

if __name__ == "__main__":
    test_customer_methods()
    test_restaurant_methods()
    test_review_methods()
