#Simulate a bank transaction checking if a user has enough money.
#1. Set a fixed variable representing a bank balance, for example: balance = 500.
#2. Ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!).
#3. If the request is less than or equal to the balance, deduct the amount and print:
#“Withdrawal successful! Remaining balance: RX”.
#4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or equal to 0. If so, print: “Invalid amount”. You must withdraw more than “R0”.
#5. Otherwise (else), print: “Declined. Insufficient funds”

#Inputs
balance=500
withdrawal=float(input("How much do you want to withdraw?: R"))


if withdrawal<=0:
    print("Invalid amount! You must withdraw more than 'R0'")

elif withdrawal<=balance:
    new_balance=float(balance)-withdrawal
    print(f"Withdrawal successful! Remaining balance: R{new_balance}")

else:
    print("Declined. Insufficient funds")
