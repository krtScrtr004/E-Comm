import uuid

from CSVHandler import CSVHandler
from config import PRODUCTS_FILE

# Product Class
class Product:
    @staticmethod
    def add_product():
        print("\nAdd Product")
        
        products = sorted(CSVHandler.read_csv(PRODUCTS_FILE), key=lambda x: x['name'])
        product_id = str(uuid.uuid4())
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        
        if Product.search_product(products, name) == -1:
            products.append({'product_id': product_id, 'name': name, 'price': price, 'stock': stock})
            CSVHandler.write_csv(PRODUCTS_FILE, products, ['product_id', 'name', 'price', 'stock'])
            print("Product added successfully!")
        else:
            print("Product already exists!")
        

    @staticmethod
    def remove_product():
        print("\nRemove Product")
        
        products = sorted(CSVHandler.read_csv(PRODUCTS_FILE), key=lambda x: x['name'])
        name = input("Enter product name to remove: ")
        
        index = Product.search_product(products, name)
        if index <= -1:
            print("Product not found!")
            return
       
        updated_products = [p for p in products if p['name'].lower() != name.lower()]
        CSVHandler.write_csv(PRODUCTS_FILE, updated_products, ['product_id', 'name', 'price', 'stock'])
        print("Product removed successfully!")
                
    @staticmethod
    def search_product(products, target_name):
        left, right = 0, len(products) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_name = products[mid]['name'].lower()
            
            if mid_name == target_name.lower():
                return mid 
            elif mid_name < target_name.lower():
                left = mid + 1  
            else:
                right = mid - 1 
                
        return -1 