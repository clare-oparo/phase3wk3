import sqlite3
from models.restaurant import Restaurant  

class Customer:
    def __init__(self, id):
        self.id = id
        self.conn = sqlite3.connect('db/restaurant_reviews.db')

    def full_name(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT first_name, last_name FROM Customers WHERE id = ?", (self.id,))
        first_name, last_name = cursor.fetchone()
        cursor.close()
        return f"{first_name} {last_name}"

    def favorite_restaurant(self):
        query = """
        SELECT restaurant_id, AVG(star_rating) as avg_rating FROM Reviews
        WHERE customer_id = ?
        GROUP BY restaurant_id
        ORDER BY avg_rating DESC
        LIMIT 1
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            restaurant_id = result[0]
            return Restaurant(restaurant_id)
        return None

    def add_review(self, restaurant, rating):
        query = "INSERT INTO Reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query, (restaurant.id, self.id, rating))
        self.conn.commit()
        cursor.close()

    def delete_reviews(self, restaurant):
        query = "DELETE FROM Reviews WHERE customer_id = ? AND restaurant_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id, restaurant.id))
        self.conn.commit()
        cursor.close()
    
    def __del__(self):
        self.conn.close()
