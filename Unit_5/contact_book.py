#Build a command-line contact book called contact_book.py that stores contacts as a list of dictionaries and allows the user to add, search, view, and delete contacts. This is a foundational data structure pattern used in virtually every real app.

#Inputs
contact_list=[]

#functions
def add_contact():
    new_name=input("Enter your name: ").lower()
    new_phone=int(input("Enter your phone number: "))
    new_email=input("Enter your email: ").lower()

    new_contact={"name":new_name,"phone":new_phone,"email":new_email}
    contact_list.append(new_contact)
    print("---------------------------------------------")
    print(f"{new_name} added to contact list")
    print("---------------------------------------------")

def search_contact():
    lookup_contact=input("Enter the name you want to lookup: ").lower()

    for contact in contact_list:
        if contact["name"]==lookup_contact:
            print("---------------------------------------------")
            print("Contact found!!")
            print("---------------------------------------------")
            print(contact)
            
        else:
            print("---------------------------------------------")
            print("None!!!")
            print("---------------------------------------------")

def delete_contact():
    ex_contact=input("Enter the name of the contact you want to delete: ").lower()

    for contact in contact_list:
        if contact["name"]==ex_contact:
            contact_list.remove(contact)
            print("---------------------------------------------")
            print(f"{ex_contact} deleted successfully")
            print("---------------------------------------------")
        else:
            print("---------------------------------------------")
            print(f"No record of {ex_contact} in the list")
            print("---------------------------------------------")

def view_all():
    cnt=1
    print("-----------------Contact List----------------")
    if len(contact_list)>0:
         for contact in contact_list:
            print(f"({cnt}). {contact["name"]}")
            cnt+=1
    else:
        print("--------------------------------")
        print("No Contacts!!")
        print("--------------------------------")

#Main Loop            
while True:
    print("------------------Main Menu------------------")
    choice=int(input("1=Add  2=Search  3=Delete  4=View All  5=Exit \n"))

    if choice==1:
        add_contact()
    elif choice==2:
        search_contact()
    elif choice==3:
        delete_contact()
    elif choice==4:
        view_all()
    elif choice==5:
        break
    else:
        print("--------------------------------")
        print("Invalid Selection! Try Again")
        print("--------------------------------")

