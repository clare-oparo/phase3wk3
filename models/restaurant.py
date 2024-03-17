import sqlite3

class Restaurant:
    def __init__(self, id):
        self.id = id
        self.conn = sqlite3.connect('db/restaurant_reviews.db')
    
    def reviews(self):
        query = """
        SELECT * FROM Reviews
        WHERE restaurant_id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        reviews = cursor.fetchall()
        cursor.close()
        # Assuming review has columns: id, restaurant_id, customer_id, star_rating
        return [{"id": review[0], "restaurant_id": review[1], "customer_id": review[2], "star_rating": review[3]} for review in reviews]

    def customers(self):
        query = """
        SELECT DISTINCT Customers.* FROM Reviews
        JOIN Customers ON Reviews.customer_id = Customers.id
        WHERE Reviews.restaurant_id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        customers = cursor.fetchall()
        cursor.close()
        # Assuming customer has columns: id, first_name, last_name
        return [{"id": customer[0], "first_name": customer[1], "last_name": customer[2]} for customer in customers]
