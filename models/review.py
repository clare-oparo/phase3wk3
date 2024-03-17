import sqlite3

class Review:
    def __init__(self, id):
        self.id = id
        self.conn = sqlite3.connect('db/restaurant_reviews.db')
    
    def customer(self):
        query = """
        SELECT Customers.* FROM Reviews
        JOIN Customers ON Reviews.customer_id = Customers.id
        WHERE Reviews.id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        customer = cursor.fetchone()
        cursor.close()
        # Assuming customer has columns: id, first_name, last_name
        if customer:
            return {"id": customer[0], "first_name": customer[1], "last_name": customer[2]}
        return None

    def restaurant(self):
        query = """
        SELECT Restaurants.* FROM Reviews
        JOIN Restaurants ON Reviews.restaurant_id = Restaurants.id
        WHERE Reviews.id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        restaurant = cursor.fetchone()
        cursor.close()
        # Assuming restaurant has columns: id, name, price
        if restaurant:
            return {"id": restaurant[0], "name": restaurant[1], "price": restaurant[2]}
        return None
