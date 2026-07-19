#creating a professional system email generator

#inputs
first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()
 
#Generate Username
username=f"{first[0]}{last}"

#Output
print(f"Your email is: {username.lower()}@university.co.za")
