"""
The account class provides account-specific actions for an individual account owned by a user
"""


class AbortTransaction(Exception):
    """Raise this exception to abort the transaction"""


class Account:
    """Account class representing an individual bank account owned by a user"""
    def __init__(self, name: str, balance: int, password: str) -> None:
        self.name = name
        self.balance = self.validate_amount(balance)
        self.password = password

    @staticmethod
    def validate_amount(amount: int) -> int:
        """Validate the amount specified. Raise an AbortTransaction exception if validation fails"""
        try:
            amount = int(amount)
        except ValueError as error:
            raise AbortTransaction("amount must be an integer") from error
        if amount <= 0:
            raise AbortTransaction("amount must be > 0")
        return amount

    def check_password_match(self, password: str) -> None:
        """
        Check user specified password with the password on the account.
        Raise an AbortTransaction exception if the passwords do not match
        """
        if password != self.password:
            raise AbortTransaction("incorrect password")

    def deposit(self, amount: int, password: str) -> int:
        """Deposit the specified amount into the account if the user enters the correct password."""
        amount = self.validate_amount(amount)
        self.check_password_match(password)
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int, password: str) -> int:
        """Withdraw the specified amount if the user enters the correct password"""
        self.check_password_match(password)
        amount = self.validate_amount(amount)
        if amount > self.balance:
            raise AbortTransaction("cannot draw more than account balance")
        self.balance -= amount
        return self.balance

    def withdraw_all(self, password: str) -> int:
        """Withdraw the entire account balance if the user enters the correct password"""
        self.check_password_match(password)
        self.balance -= self.balance
        return self.balance

    def get_balance(self, password: str) -> int:
        """Return the balance on the account"""
        self.check_password_match(password)
        return self.balance

    def show(self) -> None:
        """Show the account information"""
        print('    Name:', self.name)
        print('    Balance:', self.balance)
        print('    Password:', self.password)
        print()
