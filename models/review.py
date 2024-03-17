import sqlite3

class Review:
    def __init__(self, id, restaurant_id, customer_id, star_rating):
        self.id = id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating

    @staticmethod
    def find_by_customer(customer_id):
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()

        c.execute('SELECT * FROM reviews WHERE customer_id = ?', (customer_id,))
        reviews = c.fetchall()

        conn.close()
        return [Review(*review) for review in reviews]

    @staticmethod
    def find_by_restaurant(restaurant_id):
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()

        c.execute('SELECT * FROM reviews WHERE restaurant_id = ?', (restaurant_id,))
        reviews = c.fetchall()

        conn.close()
        return [Review(*review) for review in reviews]

    def get_restaurant_name(self):
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()

        c.execute('SELECT name FROM restaurants WHERE id = ?', (self.restaurant_id,))
        name = c.fetchone()[0]

        conn.close()
        return name

    def get_customer_full_name(self):
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()

        c.execute('SELECT firstname, lastname FROM customers WHERE id = ?', (self.customer_id,))
        firstname, lastname = c.fetchone()

        conn.close()
        return f"{firstname} {lastname}"

    def full_review(self):
        # Fetch the restaurant name and customer full name using the IDs
        restaurant_name = self.get_restaurant_name()
        customer_full_name = self.get_customer_full_name()

        return f"Review for {restaurant_name} by {customer_full_name}: {self.star_rating} stars."
