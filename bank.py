
class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("insufficient balance")

    def display_balance(self):
        print("Account Balance:", self.balance)

    def account_details(self):
        print("\nAccount details")
        print("holder:", self.name)
        print("number:", self.account_number)
        print("balance:", self.balance)



account = BankAccount("Shalah", 123456, 0)
account.account_details()
account.deposit(500)
account.display_balance()
account.withdraw(200)
account.display_balance()
account.account_details()
