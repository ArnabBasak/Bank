import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect("customer.sqlite")

    def create_database(self):
        #CUSTOMER
        self.db.execute("""CREATE TABLE IF NOT EXISTS CUSTOMER
                        (customer_number INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT,
                        phone INTEGER,
                        email TEXT,
                        address TEXT)""")
        #ACCOUNT
        self.db.execute("""CREATE TABLE IF NOT EXISTS ACCOUNT 
                        (ACCOUNT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_number integer,
                        balance real,
                        recurring_deposit integer,
                        fixed_deposit integer,
                        loan integer,
                        CONSTRAINT fk_customer_no  
                        FOREIGN KEY (customer_number)  
                        REFERENCES CUSTOMER(customer_number))
                        """)
        #LOAN
        self.db.execute("""CREATE TABLE IF NOT EXISTS LOAN
                        (LOAN_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        CUSTOMER_NUMBER INTEGER,
                        LOAN_AMOUNT REAL,
                        LOAN_TYPE TEXT,
                        INTEREST_RATE REAL,
                        CONSTRAINT fk_customer_no
                        FOREIGN KEY (customer_number)
                        REFERENCES CUSTOMER(customer_number))""")
        #DEPOSIT
        self.db.execute("""CREATE TABLE IF NOT EXISTS DEPOSIT
                        (DEPOSIT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        CUSTOMER_NUMBER INTEGER,
                        DEPOSIT_AMOUNT REAL,
                        DEPOSIT_TYPE TEXT,
                        INTEREST_RATE REAL,
                        CONSTRAINT fk_customer_no
                        FOREIGN KEY (customer_number)
                        REFERENCES CUSTOMER(customer_number))""")
        #EMPLOYEE
        self.db.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE
                        (EMPLOYEE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        ADDRESS TEXT,
                        AGE INTEGER,
                        EMAIL TEXT,
                        PHONE TEXT)""")
        #SALARY
        self.db.execute("""CREATE TABLE IF NOT EXISTS SALARY
                        (SALARY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        SALARY REAL,
                        SALARY_DATE TEXT,
                        EMPLOYEE_ID INTEGER,
                        CONSTRAINT fk_employee_id
                        FOREIGN KEY (EMPLOYEE_ID)
                        REFERENCES EMPLOYEE(EMPLOYEE_ID))""")
        

    def insert_customer_values(self,name,phone,email,address):
        self.db.execute(f"""INSERT INTO CUSTOMER (name,phone,email,address) VALUES ('{name}',{phone},'{email},'{address}'')""")

    def get_customer_values(self,name=None,phone=None,email=None,address=None):
        cursor = self.db.cursor()
        if name:
            try:
                return cursor.execute(f"SELECT name FROM CUSTOMER WHERE name = {name}")
            except:
                print("Data not found")
        elif phone:
            try:
                return cursor.execute(f"SELECT phone FROM CUSTOMER WHERE phone = {phone}")
            except:
                print("Data not found")
        elif email:
            try:
                return cursor.execute(f"SELECT email FROM CUSTOMER WHERE email = {email}")
            except:
                print("Data not found")
        elif address:
            try:
                return cursor.execute(f"SELECT address FROM CUSTOMER WHERE address = {address}")
            except:
                print("Data not found")
        else:
            print("Record not found")

    def update_values(self,name=None,phone=None,email=None):
        pass

#db = Database()
#db.create_database()