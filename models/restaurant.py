import sqlite3
from models.review import Review

class Restaurant:
    def __init__(self, id):
        self.id = id
        self.conn = sqlite3.connect('db/restaurant_reviews.db')
        self.name = self._get_name()

    def _get_name(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM Restaurants WHERE id = ?", (self.id,))
        name = cursor.fetchone()[0]
        cursor.close()
        return name

    @classmethod
    def fanciest(cls):
        conn = sqlite3.connect('db/restaurant_reviews.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM Restaurants ORDER BY price DESC LIMIT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return cls(result[0])
        return None

    def all_reviews(self):
        cursor = self.conn.cursor()
        query = """
        SELECT Customers.first_name, Customers.last_name, Reviews.star_rating
        FROM Reviews
        JOIN Customers ON Reviews.customer_id = Customers.id
        WHERE Reviews.restaurant_id = ?
        """
        cursor.execute(query, (self.id,))
        results = cursor.fetchall()
        cursor.close()
        formatted_reviews = [
            f"Review for {self.name} by {first_name} {last_name}: {star_rating} stars."
            for first_name, last_name, star_rating in results
        ]
        return formatted_reviews

    def __del__(self):
        self.conn.close()
