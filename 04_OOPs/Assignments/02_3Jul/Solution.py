class Customer:
    "Bank Name" = "ABC Bank"
    "Interest Rate" = 7.5
    accounts=[]
    transaction_counter = 1024

    def __init__(self,account_no,customer_name,balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance
        Customer.accounts.append(account_no)

    def deposit(self,amount):
        self.deposit = float(input("Enter Amount to Deposit: "))
        self.balance+=self.deposit

    def withdraw(self,amount):
        self.withdraw = float(input("Enter Amount to Withdraw: "))
        self.balance-=self.withdraw
    
    def transfer_money(self,receiver, amount):
        self.reciever = float(input("Enter Reciever No.  : "))
        self.transffered = float(input("Enter Amount to Transfer : "))
        self.balance-=self.transffered

    def display_balance(self):
        return self.balance
    
    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.new_interest_rate = new_rate 

    @classmethod
    def change_bank_name(cls,new_name):
        cls.new_bank_name = new_name

    @classmethod
    def display_bank_info(cls):
        return cls.new_bank_name,cls.new_interest_rate

    @staticmethod
    def validate_account_number(self,account_no):
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
    


    
    


