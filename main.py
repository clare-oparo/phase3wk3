from models.restaurant import Restaurant
from models.customer import Customer
from models.review import Review

def create_sample_data():
    global restaurant1, restaurant2, customer1, customer2
    
    # Creating instances of Restaurant
    restaurant1 = Restaurant(1, "Matoke Nation", 3)
    restaurant2 = Restaurant(2, "Ugali House", 2)
    
    # Creating instances of Customer
    customer1 = Customer(1, "James", "Bond")
    customer2 = Customer(2, "Hellen", "Mirren")
    
    # Assume these instances are saved to the database
    print("Sample data created.")

def add_reviews():
    # Simulating adding reviews
    
    print(f"Adding reviews...")
    review1 = Review(1, restaurant1.id, customer1.id, 5)
    review2 = Review(2, restaurant2.id, customer1.id, 4)
    review3 = Review(3, restaurant1.id, customer2.id, 3)
    
    # Assume these reviews are saved to the database here
    print("Reviews added.")

def main():
    print("Setting up sample data...")
    create_sample_data()
    
    print("Running sample operations...")
    add_reviews()
    
    print(f"{customer1.full_name()} added a review for {restaurant1.name}.")
    print(f"{customer2.full_name()} added a review for {restaurant1.name}.")

if __name__ == '__main__':
    main()
