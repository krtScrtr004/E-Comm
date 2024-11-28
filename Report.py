from CSVHandler import CSVHandler
from config import PRODUCTS_FILE, ORDERS_FILE

# Report Class
class Report:
    @staticmethod
    def generate_sales_report():
        print("\nReport Sales")
        
        orders = CSVHandler.read_csv(ORDERS_FILE)
        total_revenue = 0
        product_sales = {}
        for order in orders:
            product_id = order['product_id']
            quantity = int(order['quantity'])
            
            products = CSVHandler.read_csv(PRODUCTS_FILE)
            price = next((float(p['price']) for p in products if p['product_id'] == product_id), 0)
            total_revenue += quantity * price
            product_sales[product_id] = product_sales.get(product_id, 0) + quantity
            
        print("Top Selling Products:")
        for product_id, sales in sorted(product_sales.items(), key=lambda x: x[1], reverse=True):
            print(f"Product ID: {product_id}, Quantity Sold: {sales}")
        print(f"\nTotal Revenue: ${total_revenue}")