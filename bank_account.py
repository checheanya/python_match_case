class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into Account {self.account_number}")
        else:
            print("Error: Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}")
        else:
            print("Error: Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: {self.balance}")

def create_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            print("Error: Account number already exists.")
            return
    accounts.append(BankAccount(account_number))
    print(f"Account {account_number} created successfully.")

def close_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            accounts.remove(account)
            print(f"Account {account_number} closed successfully.")
            return
    print("Error: Account number not found.")

def process_account_operation(accounts, account_number, operation, amount=None):
    for account in accounts:
        if account.account_number == account_number:
            match operation:
                case "deposit":
                    if amount is not None:
                        account.deposit(amount)
                    else:
                        print("Error: Invalid deposit amount.")
                case "withdraw":
                    if amount is not None:
                        account.withdraw(amount)
                    else:
                        print("Error: Invalid withdrawal amount.")
                case "balance":
                    account.display_balance()
                case _:
                    print("Error: Invalid operation.")
            return
    print("Error: Account number not found.")

# Main program loop
accounts = []

while True:
    print("Bank Account Management Menu:")
    print("1. Create Account")
    print("2. Close Account")
    print("3. Perform Account Operation")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '0':
        print("Goodbye!")
        break

    if choice == '1':
        account_number = input("Enter the account number: ")
        create_account(accounts, account_number)
    elif choice == '2':
        account_number = input("Enter the account number to close: ")
        close_account(accounts, account_number)
    elif choice == '3':
        account_number = input("Enter the account number: ")
        operation = input("Enter the operation (deposit/withdraw/balance): ")
        if operation in ["deposit", "withdraw"]:
            amount = float(input("Enter the amount: "))
            process_account_operation(accounts, account_number, operation, amount)
        elif operation == "balance":
            process_account_operation(accounts, account_number, operation)
        else:
            print("Error: Invalid operation.")
    else:
        print("Error: Invalid choice.")
