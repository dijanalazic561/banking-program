def show_balance():
    print(f"The balance is:{balance:.2f}")
    def deposit():
        amount = float(input("Enter amount you want to deposit: "))
        if amount <0:
            print("Not enough money")
            return 0
        else:
            return amount

    def withdraw():
        amount=float(input("ENter amount you want to withdraw: "))
        if amount >= balance:
            print("Not enought money")
            return 0
        elif  amount < 0:
            print("not negative input allowed")
            return 0
is_running=True

while is_running:
    print("Banking program")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdrawal")
    print("4.Exit")
