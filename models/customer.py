import sqlite3

class Customer:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def add_review(self, restaurant, rating):
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()

        c.execute('INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)',
                  (restaurant.id, self.id, rating))

        conn.commit()
        conn.close()
