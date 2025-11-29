while True:
    balance = 5000
    pin = 1234
    attempts = 0  

    while attempts < 3:
        user_pin = int(input("Enter your PIN: "))

        if user_pin == pin:
            print("Your balance is:", balance)

            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance = balance - amount
                print("Congrats! Amount received.")
                print("New balance is:", balance)
            else:
                print("Insufficient balance!")

            break 

        else:
            attempts += 1
            print("Incorrect PIN!")

            if attempts == 3:
                print(" Your account is locked due to 3 wrong attempts.")
                break
    break
