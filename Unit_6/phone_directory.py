#Create a mini data directory using a List and a Dictionary combined.
# 1. Create a dictionary called contacts where the Keys are friend names and the Values are their phone numbers (keep phone numbers as strings so the leading 0 doesn’t drop off, e.g., “0821112222”). Fill it with 3 people.
# 2. Ask the user to input the name of the friend they want to look up.
# 3. Use a conditional check to see if the name matches a key. If it exists, pull out and print their number: “Found! [Name]’s number is [Number]”.
# 4. Otherwise, print “Contact not found.”

phone_dir=[{"name":"max","number":"0234567896"},{"name":"mia","number":"0987865434"},{"name":"moe","number":"0986754324"}]

while True:
    search=input("Enter name you want to lookup: ")

    for contact in phone_dir:
        if contact["name"]==search:
            print(f"Found! {contact["name"]}'s number is {contact["number"]}")
            break

    else:
        print("Contact not found")