#Write a Python script called string_formatter.py that takes a user’s first name, last name, and a short bio message as input, then applies multiple string transformations to produce a formatted user profile output. This simulates how a real app backend processes user-submitted text.


#Inputs
first=input("Enter your first name: ").strip()
last=input("Enter your last name: ").strip()
bio=input("ENter a short bio about yourself: ").strip().replace("I am","I'm")

#String transformation/manipulation
username=f"{first[0].lower()}{last.lower()}".title()

lbio=len(bio)


#Output

#print(f"First Name: {first}     Last Name: {last}")
print(f"Username: {username}")
print(f"Tell us about yourself: {bio}")
print(f" Character Count: {lbio}")


