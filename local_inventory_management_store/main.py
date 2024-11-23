
from product import Products
from store import Store
def display_menu():
    print("\nLocal Inventory Store.")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product Details")
    print("4. Update Stock Quantity")
    print("5. Generate Low-Stock Alert")
    print("6. Search Product")
    print("7. Sort Product")
    print("8. Exit")



def main():
    inventory = Store()
    while True:
        display_menu()
        option = input("Select Option 1-8: ")
        if option == "1":
            print("Add New Product")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = input("Enter Product Price: ")
            stock_quantity = int(input("Enter Stock Quantity: "))
            products = Products(name, category, price, stock_quantity)
            inventory.add_products(products)
            

        elif option == "2":
            inventory.view_products()
            
            
        elif option == "3":
            print("Choose the option you want to update: ")
            print("1. Product Name")
            print("2. Product Category")
            print("3. Price")
            print("4. stock_quantity")

            option = input("Enter the option you want to update: ")
            match option:

                case "1":
                    Product_n = input("Enter the product name to update: ")
                    Product_name = input("Enter New name: ")
                    inventory.update_product(Product_n, Product_name)
                case "2":
                    Product_n = input("Enter the Product name to update: ")
                    category = ("Enter the category: ")
                    inventory.update_category(Product_n, category)

                case "3":
                    Product_id = int(input("Enter Product id to update: "))
                    price = int(input("Enter the price in USD: "))
                    inventory.update_price(Product_id, price)

                case "4":
                    Product_id = int(input("Enter the Product Id to restock: "))
                    stock_quantity = int(input("Enter the new quantity: "))
                    inventory.restock_product(Product_id, stock_quantity)
                case _:
                    print("Invalid Option")
        elif option == "4":
            Product_id = int(input("Enter Product ID: "))
            stock_quantity = int(input("Enter stock quantity to add: "))
            inventory.restock_product(Product_id, stock_quantity)
        elif option == "5":
            Product_id = int(input("Enter Product ID: "))
            stock_quantity = int(input("Enter low stock threshold: "))
            inventory.low_stock_alert(Product_id, stock_quantity)
        elif option == "6":
            Product_name = (input("Enter Product name: "))
            category = input("Enter Product catgeory: ")
            inventory.search_product(Product_name, category)
        elif option == "7":
            price = float(input("Enter price: "))
            stock_quantity = float(input("Enter stock quantity: "))
            inventory.sort_product(price, stock_quantity)
        elif option == "8":
            inventory.close()
            break

        else:
            print("Invalid option, Choose from 1-8")
    
if __name__ == "__main__":
    main()










        


