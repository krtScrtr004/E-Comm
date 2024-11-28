import uuid
import hashlib

from CSVHandler import CSVHandler
from config import CUSTOMERS_FILE

# Customer Class
class Customer:
    
    @staticmethod
    def register():
        print("\nRegister Customer")
        
        name = email = password = None
        customers = sorted(CSVHandler.read_csv(CUSTOMERS_FILE), key=lambda x: x['email'])
        customer_id = str(uuid.uuid4())
        
        while True:
            name = input("Enter your name: ")
            if Customer.is_valid_name(name):
                break
            
        while True:
            email = input("Enter your email: ")
            if Customer.is_valid_email(email):
                break
        
        while True:
            password = input("Enter a password: ")
            if Customer.is_valid_password(password):
                password = hashlib.sha256(password.encode()).hexdigest()
                break
            
        if (Customer.search_customer(customers, email) == -1):
            customers.append({'customer_id': customer_id, 'name': name, 'email': email, 'password': password})
            CSVHandler.write_csv(CUSTOMERS_FILE, customers, ['customer_id', 'name', 'email', 'password'])
            print("Registration successful!")
        else:
            print("Registration failed")

    @staticmethod
    def login():
        print("\nLogin Customer")
        
        email = password = None
        customers = sorted(CSVHandler.read_csv(CUSTOMERS_FILE), key=lambda x: x['email'])
        
        while True:
            email = input("Enter your email: ")
            if Customer.is_valid_email(email):
                break
        
        while True:
            password = input("Enter a password: ")
            if Customer.is_valid_password(password):
                password = hashlib.sha256(password.encode()).hexdigest()
                break
            
        credential = Customer.search_customer(customers, email)
        if credential > -1 and password == customers[credential]['password']:
            print(f"\nWelcome, {customers[credential]['name']}!")
            return customers[credential]['customer_id']
            
        print("Invalid credentials!")
        return None
    
    @staticmethod
    def is_valid_name(name):
        """Validates the name for minimum length and valid characters."""
        if 3 < len(name) > 128:
            print("Name must be between 3 and 128 characters long.")
            return False
        if not name.replace(" ", "").isalpha():
            print("Name can only contain alphabetic characters and spaces.")
            return False
        
        return True

    @staticmethod
    def is_valid_email(email):
        """Validates the email format and checks for uniqueness."""
        if "@" not in email or "." not in email:
            print("Invalid email format.")
            return False
        
        return True

    @staticmethod
    def is_valid_password(password):
        """Validates the password for length and complexity."""
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            return False
        if not any(char.isdigit() for char in password):
            print("Password must contain at least one number.")
            return False
        if not any(char.isalpha() for char in password):
            print("Password must contain at least one letter.")
            return False
        if not any(char in "!@#$%^&*()-_+=<>?" for char in password):
            print("Password must contain at least one special character (!@#$%^&*()-_+=<>?).")
            return False
        
        return True
    
    @staticmethod
    def search_customer(customers, target_email):
        left, right = 0, len(customers) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_email = customers[mid]['email']
            
            if mid_email == target_email:
                return mid  
            elif mid_email < target_email:
                left = mid + 1  
            else:
                right = mid - 1 
                
        return -1