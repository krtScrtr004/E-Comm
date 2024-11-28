from Customer import Customer
from Product import Product
from Order import Order
from Report import Report

# Main Menu
class ECommerce:
    @staticmethod
    def main():
        customer_id = None
        
        # Login and registration page
        while True:
            print("\nE-Commerce Store:")
            print("[1] Login     [2] Register     [3] Exit\n")
            
            choice = int(input("Enter your choice: "))
            if choice == 1:
                customer_id = Customer.login()
                break
            elif choice == 2:
                Customer.register()
            elif choice == 3:
                return
            else:
                print("Invalid choice!")
        
        while True and customer_id is not None:
            print("\nE-commerce Store")
            print("[1] Add Product               [2] Remove Product")
            print("[3] Place Order               [4] Track Order")
            print("[5] Generate Sales Report     [6] Exit\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Product.add_product()
            elif choice == 2:
                Product.remove_product()
            elif choice == 3:
                Order.place_order(customer_id)
            elif choice == 4:
                Order.track_order()
            elif choice == 5:
                Report.generate_sales_report()
            elif choice == 6:
                print("\nGoodbye!\n")
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    ECommerce.main()