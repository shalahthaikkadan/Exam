
class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.previous_amount = self.balance
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
            print("Insufficient balance")

    def display_balance(self):
        print("Current Balance:", self.balance)

    def account_details(self):
        print("Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Previous Amount:", self.previous_amount)
        print("Current Balance:", self.balance)



account = BankAccount("Shalah", 123456, 0)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Account Details")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        account.account_details()

    else:
        print("Invalid choice. Please try again.")
