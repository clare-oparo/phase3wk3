import sqlite3

create_restaurants_table = """
CREATE TABLE IF NOT EXISTS Restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price TEXT NOT NULL
);
"""

create_customers_table = """
CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
"""

create_reviews_table = """
CREATE TABLE IF NOT EXISTS Reviews (
    id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    customer_id INTEGER,
    star_rating INTEGER NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id),
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);
"""

def create_tables():
    # Connect to the SQLite database or create it if it doesn't exist
    conn = sqlite3.connect('db/restaurant_reviews.db')
    cursor = conn.cursor()

    # Execute table creation statements
    cursor.execute(create_restaurants_table)
    cursor.execute(create_customers_table)
    cursor.execute(create_reviews_table)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database successfully set up.")
