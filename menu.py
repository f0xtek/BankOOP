"""
The menu class acts as the primary user interface for the banking system.
The menu loop prompts the user for various actions related to managing accounts.
"""
from bank import Bank, AbortTransaction


class Menu:
    """Menu class to provide a user interface to the banking system"""
    def __init__(self):
        self.bank = Bank()

    @staticmethod
    def print_menu() -> None:
        """Print the menu's user interface"""
        print()
        print("Press b to get the balance")
        print("Press d to make a deposit")
        print("Press o to open a new account")
        print("Press w to make a withdrawal")
        print("Press s to show all accounts")
        print("Press c to close an account")
        print("Press i for bank contact information")
        print("Press q to quit")
        print()

    @staticmethod
    def prompt_for_action() -> str:
        """Prompt user for an action from the menu"""
        action = input("What do you want to do? ")
        action = action.casefold()
        action = action[0]
        return action

    def run(self):
        """Run the menu loop"""
        while True:
            self.print_menu()

            action = self.prompt_for_action()

            try:
                if action == 'b':
                    self.bank.balance()
                elif action == 'd':
                    self.bank.deposit()
                elif action == 'o':
                    self.bank.open_account()
                elif action == 'w':
                    self.bank.withdraw()
                elif action == 's':
                    self.bank.show()
                elif action == 'c':
                    self.bank.close_account()
                elif action == 'i':
                    self.bank.contact_info()
                elif action == 'q':
                    break
            except AbortTransaction as error:
                print(error)
