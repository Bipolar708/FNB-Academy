#Write a Python script called student_info.py that collects personal information from the user and displays it in a formatted profile card. The program must demonstrate correct use of all four data types, string manipulation, arithmetic, and the f-string output format.

#Inputs
name=input("Enter your name: ")
surname=input("Enter your surname: ")
age=int(input("How old are you?: "))
fav_num=float(input("Whats your favourite number?: "))

#Output Text
print(f"Welcome, {name} {surname}")
print(f"Uppercase: {name.upper()}")
print(f"Title: {name.title()}")

#Output Numbers
print(f"Age in Months: ",age*12)
print("Rounded Favourite number: ",round(fav_num,2))

#Output value types
print(type(name))
print(type(surname))
print(type(age))
print(type(fav_num))