def show_balance(balance):
    print("**********")
    print(f"The balance is: {balance:.2f} dollars")
    print("**********")
    return balance

def deposit():
    print("**********")
    try:
        amount = float(input("Enter amount you want to deposit: "))
    except ValueError:
        print("**********")
        print("Please enter a valid number")
        print("**********")
        return 0.0
    if amount <= 0:
        print("**********")
        print("Amount must be positive")
        print("**********")
        return 0.0
    return amount

def withdraw(balance):
    print("**********")
    try:
        amount = float(input("Enter amount you want to withdraw: "))
    except ValueError:
        print("**********")
        print("Enter a valid amount")
        print("**********")
        return 0.0
    if amount <= 0:
        print("**********")
        print("Amount must be positive")
        print("**********")
        return 0.0
    if amount > balance:
        print("**********")
        print("Not enough money")
        print("**********")
        return 0.0
    return amount

def main():
    balance = 0.0
    is_running = True

    while is_running:
        # Always show current balance first
        show_balance(balance)

        print("Banking program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")
        print("**********")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            amt = deposit()
            if amt > 0:
                balance += amt
            show_balance(balance)  # show updated or unchanged balance

        elif choice == "3":
            amt = withdraw(balance)
            if amt > 0:
                balance -= amt
            show_balance(balance)  # show updated or unchanged balance

        elif choice == "4":
            is_running = False

        else:
            print("**********")
            print("Invalid choice")
            print("**********")

    print("**********")
    print("Thank you for using banking program")
    print("**********")

if __name__ == "__main__":
    main()