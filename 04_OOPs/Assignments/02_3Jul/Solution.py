class Customer:
    Bank_Name = "ABC Bank"
    Interest_Rate = 7.5
    accounts=[]
    transaction_counter = 1024

    def __init__(self,account_no,customer_name,balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance
        Customer.accounts.append(account_no)
        

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount
    
    def transfer_money(self, receiver, amount):
        self.balance -= amount
        receiver.balance += amount

    def display_balance(self):
        return self.balance
    
    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.Interest_Rate = new_rate 

    @classmethod
    def change_bank_name(cls,new_name):
        cls.Bank_Name = new_name

    @classmethod
    def display_bank_info(cls):
        return cls.Bank_Name, cls.Interest_Rate

    @staticmethod
    def validate_account_number(account_no):
        if account_no in Customer.accounts:
            return True
        else:
            return False

    @staticmethod
    def calculate_interest(amount, rate):
        return ( amount * rate ) / 100
    
    @staticmethod
    def generate_transaction_id():
        Customer.transaction_counter+=1
        return f"TXN{Customer.transaction_counter}"
    
for i in range(2):
    print(f"Customer{i+1}")
    ac_no = int(input("Account No : "))
    name = input("Customer Name : ")
    balance = float(input("Account Balance : "))
    globals()[f"c{i+1}"] = Customer(ac_no,name,balance)     #I used this globals to make it dynamic

amount =  float(input("Enter Deposit Amount: "))
c1.deposit(amount)

amount = float(input("Enter Transfer Amount: "))
c1.transfer_money(c2, amount)

print(f"Customer : {c1.customer_name}")
print(f"Balance  : {c1.display_balance()}\n")

print(f"Customer : {c2.customer_name}")
print(f"Balance  : {c2.display_balance()}\n")

print(f"Bank Name      : {Customer.Bank_Name}")
print(f"Interest Rate  : {Customer.Interest_Rate}%")
print(f"Transaction ID : {Customer.generate_transaction_id()}")