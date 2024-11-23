# 1. Product Management
# 2. Stock Management 
# 3. Search and Sort
from product import Products
from dbconn import Database

class Store:
    low_stock = 10
    def __init__(self):
        self.db = Database()

def add_product(self, Products):
    query = "INSERT INTO Store_Inventory (product_name, product_category, product_price, product_stock_quantity) VALUES(%S, %S, %S, %S)"
    self.db.execute_q(query, (Products.name, Products.category, Products.price, Products.stock_quantity))
    print(f"Product '{Products.name} added successfully")

def view_products(self):
    query = "SELECT * FROM Inventory_Store"
    products = self.db.fetch_q(query)
    if products:
        for p in products:
            print(p)
    else:
        print("No products in Inventory")
def update_productname(self, Product_n, Product_name):
    query = "UPDATE Inventory_Store SET Product_name = %s WHERE Product_name = %s"
    self.db.execute_q(query, (Product_name, Product_n))
    print("Update Successfully")

def restock_product(self, Product_id,  stock_quantity):
    query = "UPDATE Inventory_Store SET stock_quantity = %s WHERE Product_id = %s"
    self.db.execute_q(query, (Product_id, stock_quantity))
    print(f"Product ID {Product_id} restocked with {stock_quantity}")

def update_category(self, Product_n, category):
    query = "UPDATE Inventory_Store SET category = %s WHERE Product_n = %s"
    self.db.execute_q(query, (Product_n, category))
    print(f"Product {Product_n} updated to {category} category")

def update_price(self, Product_id, price):
    query = "UPDATE Inventory_Store SET price = %s WHERE Product_id = %s"
    self.db.execute_q(query, (Product_id, price))
    print(f"Product {Product_id} updated to {price} Price")

def remove_product(self, Product_id):
    query = "DELETE FROM Inventory_Store WHERE Product_id = %s "
    self.db.execute_q(query, Product_id)
    print(f"{Product_id} Removed")

def low_stock_alert(self, Product_id, stock_quantity):
    query = "SELECT * FROM Inventory_Store WHERE Product_id = %s AND stock_quantity < %s "
    products = self.db.fetch_q(query, (Product_id, stock_quantity))
    if products:
        return f"Product {Product_id} stock is low"
    else:
        return "Stock level sufficient for this product"
    
    #     alert_message = []
    #     for product in products:
    #         alert_message.append(f"Product {product['Product_id']} stock is low (Quantity: {product['stock_quantity']})")
    #     return "\n".join(alert_message)
    # else:
    #     return "Stock levels are sufficient for this product."
def search_product(self, Product_name, category):
    query = "SELECT * FROM Inventory_Store WHERE Product_name = %s AND category = %s"
    products = self.db.fetch_q(query, (Product_name, category))
    if products:
        return products
    else:
        return f"No product found for '{Product_name}' in category '{category}'."

def sort_product(self, price=None, stock_quantity=None, sort_by='price', order='ASC'):
    try:
        query = "SELECT * FROM Inventory_Store"
        conditions = []
        params = []
        if price is not None:
            conditions.append("price = %s")
            params.append(price)
        if stock_quantity is not None:
            conditions.append("stock_quantity = %s")
            params.append(stock_quantity)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += f" ORDER BY {sort_by} {order}" 
        Products = self.db.fetch_q(query, tuple(params))
        if Products:
            return Products
        else:
            return "No matching products found."
    except Exception as e:
        return f"An error occured: {str(e)}"
    