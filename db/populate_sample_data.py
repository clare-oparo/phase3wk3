import sqlite3

def insert_sample_data():
    conn = sqlite3.connect('db/restaurant_reviews.db')
    cursor = conn.cursor()

    # Sample Restaurants
    restaurants = [
        ('The Greenhouse', 'Medium'),
        ('Cafe del Sol', 'Low'),
        ('Spice of Life', 'High'),
    ]
    cursor.executemany('INSERT INTO Restaurants (name, price) VALUES (?, ?)', restaurants)

    # Sample Customers
    customers = [
        ('John', 'Doe'),
        ('Jane', 'Doe'),
        ('Alice', 'Johnson'),
    ]
    cursor.executemany('INSERT INTO Customers (first_name, last_name) VALUES (?, ?)', customers)

    # Committing here to ensure we have IDs to use for reviews
    conn.commit()

    # Sample Reviews
    # Assuming the IDs of Restaurants and Customers start at 1 and auto-increment
    reviews = [
        (1, 1, 5),  # Customer 1 reviews Restaurant 1 with 5 stars
        (2, 2, 4),  # Customer 2 reviews Restaurant 2 with 4 stars
        (3, 3, 3),  # Customer 3 reviews Restaurant 3 with 3 stars
    ]
    cursor.executemany('INSERT INTO Reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', reviews)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_sample_data()
    print("Sample data has been inserted into the database.")
