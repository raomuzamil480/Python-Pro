def show_balance(balance):
    print(f"Your balance is {balance}")


def deposit():
    amount = float(input("Please enter deposit amount: "))

    if amount < 0:
        print("Invalid amount")
        return 0
    return amount


def withdraw(balance):
    amount = float(input("Enter withdraw amount: "))

    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Invalid amount")
        return 0
    return amount

def main():
    balance = 0
    is_run = True

    while is_run:
        print("\nEnter Choice:")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_run = False
            print("Thanks for choosing")

        else:
            print("Invalid choice")
if __name__=='__main__':
    main()