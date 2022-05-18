"""
The Bank class manages multiple Account objects, providing an interface
for working with any given account.

This is an Object Manager Object pattern, using object composition.
"""
from account import Account, AbortTransaction


class Bank:
    """Bank class representing a banking system. Manages one or more accounts."""
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 0
        self.address = "123 ABC Street, DEF City, GHI County. AB1 2CD"
        self.tel = "01234 567 890"
        self.open_hours = "08:00 - 17:00"

    def contact_info(self) -> None:
        """Display the bank's contact info"""
        print("*** Contact ***")
        print(f"    {self.address}")
        print(f"    {self.tel}")
        print(f"    {self.open_hours}")
        print()

    def ask_for_valid_account_number(self) -> int:
        """Prompt user for an account number and validate the input"""
        acc_num = input("What is your account number? ")
        try:
            acc_num = int(acc_num)
        except ValueError as error:
            raise AbortTransaction("account number must be an integer") from error
        if acc_num not in self.accounts:
            raise AbortTransaction(f"account {acc_num} does not exist")
        return acc_num

    @staticmethod
    def ask_for_valid_password(acc: Account) -> str:
        """Prompt the user for their password and validate against the password on the account"""
        password = input("What is your password? ")
        if password != acc.password:
            raise AbortTransaction("invalid password")
        return password

    @staticmethod
    def ask_for_valid_starting_balance() -> int:
        """
        Prompt the user for the starting balance when opening an account,
        and validate the input
        """
        starting_balance = input("Please enter the starting balance: ")
        try:
            starting_balance = int(starting_balance)
        except ValueError as error:
            raise AbortTransaction("starting balance must be an integer") from error
        return starting_balance

    @staticmethod
    def ask_for_valid_deposit_amount() -> int:
        """Prompt the user for the deposit amount and validate the input"""
        deposit_amount = input("Please enter the deposit amount: ")
        try:
            deposit_amount = int(deposit_amount)
        except ValueError as error:
            raise AbortTransaction("deposit amount must be an integer") from error
        return deposit_amount

    @staticmethod
    def ask_for_valid_withdraw_amount() -> int:
        """Prompt the user for a withdrawal amount and validate the input"""
        amount = input("Please enter the withdrawal amount: ")
        try:
            amount = int(amount)
        except ValueError as error:
            raise AbortTransaction("deposit amount must be an integer") from error
        return amount

    def get_users_account(self, account_number) -> Account:
        """Get the user's bank account object"""
        acc = self.accounts[account_number]
        return acc

    def create_account(self, name: str, start_balance: int, password: str) -> int:
        """Create a new bank account object fo the user"""
        acc = Account(name, start_balance, password)
        new_account_number = self.next_account_number
        self.accounts[new_account_number] = acc
        self.next_account_number += 1
        return new_account_number

    def open_account(self) -> None:
        """Prompt the user for new bank account details and call the method to create the account"""
        print("*** Open Account ***")
        name = input("What is the account name? ")
        starting_balance = self.ask_for_valid_starting_balance()
        password = input("What is your password? ")
        account_num = self.create_account(name, starting_balance, password)
        print(f"Your new account number is: {account_num}")

    def close_account(self) -> None:
        """Close an open bank account, printing any remaining balance if greater than 0"""
        print("*** Close Account ***")
        account_num = self.ask_for_valid_account_number()
        acc = self.get_users_account(account_num)
        password = self.ask_for_valid_password(acc)
        balance = acc.get_balance(password)
        if balance > 0:
            print(f"You had {balance} in your account, which will be returned to you.")
        del self.accounts[account_num]
        print("Account is now closed.")

    def balance(self) -> int:
        """Prompt the user for an account number, retrieve and display the account's balance"""
        print("*** Get Balance ***")
        account_number = self.ask_for_valid_account_number()
        acc = self.get_users_account(account_number)
        self.ask_for_valid_password(acc)
        balance = acc.get_balance(acc.password)
        print(f"Your balance is: {balance}")
        return balance

    def deposit(self) -> None:
        """Deposit the specified amount in the account specified by the user"""
        print("*** Deposit ***")
        account_num = self.ask_for_valid_account_number()
        acc = self.get_users_account(account_num)
        self.ask_for_valid_password(acc)
        deposit_amount = self.ask_for_valid_deposit_amount()
        balance = acc.deposit(deposit_amount, acc.password)
        print(f"Deposited: {deposit_amount}")
        print(f"Your new balance is: {balance}")

    def show(self) -> None:
        """Show all accounts managed by the bank"""
        print("*** Show ***")
        if len(self.accounts.keys()) == 0:
            print("    No accounts created")
        else:
            for account_num, account in self.accounts.items():
                print(f"    Account: {account_num}")
                account.show()

    def withdraw(self) -> None:
        """Withdraw the specified amount from the account specified by the user"""
        print("*** Withdraw ***")
        account_num = self.ask_for_valid_account_number()
        acc = self.get_users_account(account_num)
        self.ask_for_valid_password(acc)
        amount = self.ask_for_valid_withdraw_amount()
        balance = acc.withdraw(amount, acc.password)
        print(f"Withdrew: {amount}")
        print(f"Balance: {balance}")
