#Build a student grade classifier called grade_classifier.py that takes a learner’s name and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card. The program must correctly use conditionals for all grade and status logic.

#inputs
name=input("Enter your name: ")
sub1=float(input("Enter the marks for subject 1: "))
sub2=float(input("Enter the marks for subject 2: "))
sub3=float(input("Enter the marks for subject 3: "))

#Calculations
avg=(sub1+sub2+sub3)/3

if avg>=80:
    print(f"Student Name: {name}")
    print(f"Subject 1: {round(sub1,2)}")
    print(f"Subject 2: {round(sub2,2)}")
    print(f"Subject 3: {round(sub3,2)}")

    print(f"Average: {round(avg),2}")
    print(f"Letter Grade: A")
    print("Status: Pass")

elif avg>=70 and avg<=79:
    print(f"Student Name: {name}")
    print(f"Subject 1: {round(sub1,2)}")
    print(f"Subject 2: {round(sub2,2)}")
    print(f"Subject 3: {round(sub3,2)}")

    print(f"Average: {round(avg),2}")
    print(f"Letter Grade: B")
    print("Status: Pass")

elif avg>=60 and avg<=69:
    print(f"Student Name: {name}")
    print(f"Subject 1: {round(sub1,2)}")
    print(f"Subject 2: {round(sub2,2)}")
    print(f"Subject 3: {round(sub3,2)}")

    print(f"Average: {round(avg),2}")
    print(f"Letter Grade: C")
    print("Status: Pass")
    
elif avg>=50 and avg<=59:
    print(f"Student Name: {name}")
    print(f"Subject 1: {round(sub1,2)}")
    print(f"Subject 2: {round(sub2,2)}")
    print(f"Subject 3: {round(sub3,2)}")

    print(f"Average: {round(avg),2}")
    print(f"Letter Grade: D")
    print("Status: Pass")

elif avg<40:
    print(f"Student Name: {name}")
    print(f"Subject 1: {round(sub1,2)}")
    print(f"Subject 2: {round(sub2,2)}")
    print(f"Subject 3: {round(sub3,2)}")

    print(f"Average: {round(avg),2}")
    print(f"Letter Grade: F")
    print("Status: Fail (Needs Intervention)")


else:
    print(f"Student Name: {name}")
    print(f"Subject 1: {round(sub1,2)}")
    print(f"Subject 2: {round(sub2,2)}")
    print(f"Subject 3: {round(sub3,2)}")

    print(f"Average: {round(avg),2}")
    print(f"Letter Grade: F")
    print("Status: Fail")