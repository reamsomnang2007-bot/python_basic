# Python Banking 

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposit: "))
    if amount < 0:
        print("That is not valid amount!")
        return 0
    else:
        return amount 

def withdraw(balance):
    amount = float(input("Enter amount to be withdraw: "))
    if amount > balance:
        print("That amount is greater than balance!")
        return 0
    elif amount == 0:
        print("That amount will be greater than 0!")
        return 0
    else:
        return amount

def show_option():
    print("----------> Banking System <----------")
    print("[1]. Show Balance")
    print("[2]. Deposit Money")
    print("[3]. Withdraw Money")
    print("[4]. Exit Program")
    print("--------------------------------------")


def main():
    balance = 0
    is_running = True
    while is_running:
        show_option()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("Thanks for your visiting...")
            is_running = False
        else:
            print("That is not valid choice...!")

if __name__ == "__main__":
    main()

        

