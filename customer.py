import Model
import re

db = Model

class customer():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.address = ""
        self.phone = ""
    def adhaar_number_validation(self,number):
        regex = ("^[2-9]{1}[0-9]{3}\\" +
             "s[0-9]{4}\\s[0-9]{4}$")
        p = re.compile(regex)
        if(re.search(p, number)):
            return True
        else:
            return False
    def customer_creation(self):
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.email = input("email: ")
        self.address = input("enter your address: ")
        adhaar_number = input("Enter your adhaar number: ")
        self.phone = input("Enter your mobile number: ")
        check = self.adhaar_number_validation(adhaar_number)
        if check == False:
            print("="*20)
            print("sorry cannot create the account as adhaar number is not valid")
        else:
            phone_check = Model.Database.get_customer_values(self.phone)
            email_check = Model.Database.get_customer_values(self.email)
            if phone_check:
                print("Customer already present in the records")
            elif email_check:
                print("Customer already present in the records")
            else:
                name = f"{self.first_name} {self.last_name}"
                Model.Database.insert_customer_values(name,self.phone,self.email,self.address)
    def loan_account(self):
        pass
    def deposit_account(self):
        pass
    
        
customer = customer()
customer.customer_creation()

