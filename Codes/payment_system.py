"""It is testing version. I should connect it with DB"""




wallet = 1315
attempt = 0
my_card = 1001


def checking():
    """Checks PIN and blocks card after 3 failed attempts."""
    global attempt
    while True:
        if attempt == 3:
            print("Your card has been BLOCKED!!!")
            return -1
        w = int(input("Enter your PIN code: "))
        if w == my_card:
            print("Welcome!\nHow can I assist you?")
            return 1
        else:
            attempt += 1
            print(f"Incorrect PIN! Attempts left: {3 - attempt}")


def show_balance():
    """Displays the account balance."""
    print(f"Your balance: {wallet}$\n")
    print("1. Check balance", "2. Withdraw money", "3. Deposit money", "Enter '0' to exit\n", sep='\n')


def withdraw_money():
    """Allows the user to withdraw money if sufficient funds are available."""
    global wallet
    while True:
        wallet = int(wallet)
        amount = int(input("Enter the amount: "))
        if wallet < amount:
            print("Insufficient funds!")
        else:
            wallet -= amount
            wallet = str(wallet)
            print(f"{amount}$ withdrawn\nRemaining balance: {wallet}$\n")
            break
    print("1. Check balance", "2. Withdraw money", "3. Deposit money", "Enter '0' to exit\n", sep='\n')


def deposit_money():
    """Allows the user to deposit money into their account."""
    global wallet
    wallet = int(wallet)
    amount = int(input("Enter the amount: "))
    wallet += amount
    wallet = str(wallet)
    print(f"Your balance is now {wallet}$\nIncreased by {amount}$\n")
    print("1. Check balance", "2. Withdraw money", "3. Deposit money", "Enter '0' to exit\n", sep='\n')


def interface():
    """Main ATM interface."""
    global attempt
    if checking() == -1:
        return  # Exit if card is blocked
    print("1. Check balance", "2. Withdraw money", "3. Deposit money", "Enter '0' to exit\n", sep='\n')

    while True:
        choice = input("Enter a number: ")
        if choice == '1':
            show_balance()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == '0':
            break
        else:
            print("Please try again :/\n")

    attempt = 0  # Reset attempt count after a successful session


interface()



