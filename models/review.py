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
