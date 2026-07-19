#Users often forget their passwords. Create a script that helps them by showing a secure hint.

#Inputs
password=input("Enter your secret password: ").strip()

#Hint generation
print(f"Your password hint: It starts with {password[0].upper()} and ends with {password[-1].upper()}")