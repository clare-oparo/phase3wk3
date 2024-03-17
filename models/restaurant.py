import sqlite3

class Restaurant:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @staticmethod
    def all():
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()

        c.execute('SELECT * FROM restaurants')
        all_restaurants = c.fetchall()

        conn.close()
        return [Restaurant(*restaurant) for restaurant in all_restaurants]

    @staticmethod
    def fanciest():
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()

        c.execute('SELECT * FROM restaurants ORDER BY price DESC LIMIT 1')
        restaurant = c.fetchone()

        conn.close()
        if restaurant:
            return Restaurant(*restaurant)
        return None
