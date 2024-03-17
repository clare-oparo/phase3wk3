import sqlite3

def insert_sample_data(db_path='db/restaurant_reviews.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear existing data
    cursor.executescript("""
    DELETE FROM Reviews;
    DELETE FROM Customers;
    DELETE FROM Restaurants;
    """)

    # Insert sample Restaurants
    restaurants = [
        ('The Greenhouse', 'High'),  # Price here is 'Low', 'Medium', 'High'
        ('Cafe del Sol', 'Medium'),
        ('Spice of Life', 'Low'),
    ]
    cursor.executemany('INSERT INTO Restaurants (name, price) VALUES (?, ?)', restaurants)

    # Insert sample Customers
    customers = [
        ('John', 'Doe'),
        ('Jane', 'Roe'),
        ('Alice', 'Johnson'),
    ]
    cursor.executemany('INSERT INTO Customers (first_name, last_name) VALUES (?, ?)', customers)

    # Commit to save IDs
    conn.commit()

    # Insert sample Reviews
    # Match the IDs correctly based on the insertion order above
    reviews = [
        (1, 1, 5),  # First restaurant reviewed by first customer
        (1, 2, 4),  # First restaurant reviewed by second customer
        (2, 3, 3),  # Second restaurant reviewed by third customer
    ]
    cursor.executemany('INSERT INTO Reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', reviews)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    insert_sample_data()
    print("Sample data has been successfully inserted.")
