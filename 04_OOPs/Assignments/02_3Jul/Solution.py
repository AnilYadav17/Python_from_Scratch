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
        self.deposit = amount
        self.balance+=self.deposit

    def withdraw(self,amount):
        self.withdraw = amount
        self.balance-=self.withdraw
    
    def transfer_money(self,reciever, amount):
        self.reciever = reciever
        self.transffered = amount
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
    


c1 = Customer(1001,"Anil",50000)
c2 = Customer(1002,"Anu",30000)

amount =  float(input("Enter Deposit Amount: "))
c1.deposit(amount)

amount = float(input("Enter Transfer Amount: "))
receiver = c2.account_no
c1.transfer_money(receiver,amount)


print(c1.display_balance())
c2.balance + c2.calculate_interest(c2.balance,c2.Interest_Rate)

print(c2.display_balance())