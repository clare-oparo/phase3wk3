import sqlite3

class Customer:
    def __init__(self, id):
        self.id = id
        self.conn = sqlite3.connect('db/restaurant_reviews.db')
    
    def reviews(self):
        query = """
        SELECT * FROM Reviews
        WHERE customer_id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        reviews = cursor.fetchall()
        cursor.close()
        # Assuming review has columns: id, restaurant_id, customer_id, star_rating
        return [{"id": review[0], "restaurant_id": review[1], "customer_id": review[2], "star_rating": review[3]} for review in reviews]

    def restaurants(self):
        query = """
        SELECT DISTINCT Restaurants.* FROM Reviews
        JOIN Restaurants ON Reviews.restaurant_id = Restaurants.id
        WHERE Reviews.customer_id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        restaurants = cursor.fetchall()
        cursor.close()
        # Assuming restaurant has columns: id, name, price
        return [{"id": restaurant[0], "name": restaurant[1], "price": restaurant[2]} for restaurant in restaurants]
