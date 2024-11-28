import uuid

from CSVHandler import CSVHandler
from Customer import Customer
from Product import Product
from config import CUSTOMERS_FILE, PRODUCTS_FILE, ORDERS_FILE

# Order Class
class Order:
    @staticmethod
    def place_order(customer_id):
        products = sorted(CSVHandler.read_csv(PRODUCTS_FILE), key=lambda x: x['name'])
        orders = CSVHandler.read_csv(ORDERS_FILE)
        
        print("\nAvailable products:")
        for p in products:
            print(f"{p['product_id']}: {p['name']} - ${p['price']} (Stock: {p['stock']})")
        
        name = input("\nEnter the product name to order: ")
        quantity = int(input("Enter quantity: "))
        
        index = Product.search_product(products, name)
        if index == -1:
             print("Product not found!")
             return
         
        if int(products[index]['stock']) >= quantity:
            products[index]['stock'] = str(int(products[index]['stock']) - quantity)
            orders.append({
                    'order_id': str(uuid.uuid4()),
                    'customer_id': customer_id,
                    'product_id': products[index]['product_id'],
                    'quantity': quantity,
                    'status': 'Processing'
            })
            CSVHandler.write_csv(PRODUCTS_FILE, products, ['product_id', 'name', 'price', 'stock'])
            CSVHandler.write_csv(ORDERS_FILE, orders, ['order_id', 'customer_id', 'product_id', 'quantity', 'status'])
            print("Order placed successfully!")
            return
        else:
            print("Insufficient stock!")
            return       
     

    @staticmethod
    def track_order():
        print("\nYour order list:")
        
        customers = sorted(CSVHandler.read_csv(CUSTOMERS_FILE), key=lambda x: x['email'])
        orders = CSVHandler.read_csv(ORDERS_FILE)
        
        email = None
        while True:
            email = input("Enter your email: ")
            if Customer.is_valid_email(email):
                break
            
        customer_index = Customer.search_customer(customers, email)
        customer_id = customers[customer_index]['customer_id']
        
        for order in orders:
            if order['customer_id'] == customer_id:
                print(f"Order ID: {order['order_id']} Order Status: {order['status']}")
    
        