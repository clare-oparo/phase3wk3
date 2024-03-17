import sqlite3

class Review:
    def __init__(self, id):
        self.id = id
        self.conn = sqlite3.connect('db/restaurant_reviews.db')
        self.star_rating = self._get_star_rating()

    def _get_star_rating(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT star_rating FROM Reviews WHERE id = ?", (self.id,))
        result = cursor.fetchone()
        cursor.close()
    
        if result:
            return result[0]
        else:
            return None 


    def full_review(self):
        cursor = self.conn.cursor()
        query = """
        SELECT Restaurants.name, Customers.first_name, Customers.last_name
        FROM Reviews
        JOIN Restaurants ON Reviews.restaurant_id = Restaurants.id
        JOIN Customers ON Reviews.customer_id = Customers.id
        WHERE Reviews.id = ?
        """
        cursor.execute(query, (self.id,))
        result = cursor.fetchone()
        restaurant_name, first_name, last_name = result
        full_name = f"{first_name} {last_name}"
        cursor.close()
        return f"Review for {restaurant_name} by {full_name}: {self.star_rating} stars."

    def __del__(self):
        self.conn.close()
