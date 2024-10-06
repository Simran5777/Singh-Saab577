def withdraw_money():
    try:
        balance = float(input("Enter account balance: "))
        withdrawal = float(input("Enter withdrawal amount: "))

        if withdrawal > balance:
            raise Exception("Withdrawal amount exceeds balance.")
        elif withdrawal < 0:
            raise Exception("Withdrawal amount cannot be negative.")
        else:
            print(f"Withdrawal successful. New balance: {balance - withdrawal}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(e)


withdraw_money()
