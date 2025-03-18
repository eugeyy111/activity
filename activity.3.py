class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts money if balance is sufficient."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Displays the account balance."""
        print(f"Account balance: ${self.balance}")


# Create a BankAccount instance
account = BankAccount(account_number="347824739", owner="Jasper")

# Perform transactions
account.deposit(50000)
account.withdraw(5000)
account.display_balance()
account.withdraw(3000)
account.display_balance()