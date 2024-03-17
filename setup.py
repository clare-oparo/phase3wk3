import sqlite3

def create_tables():
    # Connect to database or create it if it doesn't exist
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    # Create restaurants table
    c.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL
        );
    ''')

    # Create customers table
    c.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL
        );
    ''')

    # Create reviews table
    c.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            star_rating INTEGER NOT NULL,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Database and tables created successfully.")
