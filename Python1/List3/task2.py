class Bank_acconunt:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self,amount):
        self.balance +=amount
    def withdraw(self,amount):
        self.balance -=amount
    def check_balance(self):
        return self.balance

Account_1 = Bank_acconunt(123456789,1000,"01/01/2020","John")
print("Balance : " , Account_1.check_balance())
Account_1.deposit(500)
print("Balance after deposit : ",Account_1.check_balance())
Account_1.withdraw(200)
print("Balance after withdraw : ",Account_1.check_balance())