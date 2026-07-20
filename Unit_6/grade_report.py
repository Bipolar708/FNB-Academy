#Build a student grade classifier called grade_classifier.py that takes a learner’s name and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card. The program must correctly use conditionals for all grade and status logic.

#Extend the Unit 4 grade classifier into a full grade report generator called grade_report.py. The program must process a list of student dictionaries (each with name and marks for three subjects), generate a grade and status for each student, and produce a full class summary report.



#inputs
students=[
    {"name":"max","maths":"50","english":"90","science":"47"},
    {"name":"mia","maths":"87","english":"23","science":"36"},
    {"name":"may","maths":"25","english":"46","science":"97"},
    {"name":"moe","maths":"89","english":"87","science":"46"},
    {"name":"jay","maths":"87","english":"56","science":"80"}
]
results=[]
avg_total=0
averages=[]

def search_student():
    search=input("Enter name of student: ").lower()

    for student in results:
        if student["name"]==search:

            print(f"Student Name: {student["name"]}")
            print("---------------------------------")
            print(f"Average: {student["average"]}")
            print(f"Letter Grade: {student["grade"]}")
            print(f"Status: {student["status"]}")
            print("---------------------------------")
            break
            

    else:
        print("No such Student in this Class!")
        print("---------------------------------")
              
#Iterations
for student in students:
    #Calculations
    avg=(int(student["maths"])+int(student["english"])+int(student["science"]))/3

    status=""
    grade=""

    if avg>=80:
        status="Pass"
        grade="A"

        print(f"Student Name: {student["name"]}")
        
        print("---------------------------------")
        print(f"Average: {round(float(avg)),2}")
        print(f"Letter Grade: {grade}")
        print(f"Status: {status}")
        print("---------------------------------")

    elif avg>=70 and avg<=79:
        status="Pass"
        grade="B"
        
        print(f"Student Name: {student["name"]}")

        print("---------------------------------")
        print(f"Average: {round(float(avg),2)}")
        print(f"Letter Grade: {grade}")
        print(f"Status: {status}")
        print("---------------------------------")

    elif avg>=60 and avg<=69:
        status="Pass"
        grade="C"

        print(f"Student Name: {student["name"]}")

        print("---------------------------------")
        print(f"Average: {round(float(avg),2)}")
        print(f"Letter Grade: {grade}")
        print(f"Status: {status}")
        print("---------------------------------")
    
    elif avg>=50 and avg<=59:
        status="Pass"
        grade="D"

        print(f"Student Name: {student["name"]}")

        print("---------------------------------")
        print(f"Average: {round(float(avg),2)}")
        print(f"Letter Grade: {grade}")
        print(f"Status: {status}")
        print("---------------------------------")

    elif avg<40:
        status="Status: Fail (Needs Intervention)"
        grade="F"

        print(f"Student Name: {student["name"]}")

        print("---------------------------------")
        print(f"Average: {round(float(avg),2)}")
        print(f"Letter Grade: {grade}")
        print(f"Status: {status}")
        print("---------------------------------")

    else:
        status="Fail"
        grade="F"

        print(f"Student Name: {student["name"]}")

        print("---------------------------------")
        print(f"Average: {round(float(avg),2)}")
        print(f"Letter Grade: {grade}")
        print(f"Status: {status}")
        print("---------------------------------")

    results.append({"name":student["name"],"average":round(float(avg)),"grade":grade,"status":status})

    averages.append(avg)
    avg_total+=float(avg)

class_avg=avg_total/len(students)

print(f"Class Average: {round(float(class_avg),2)}")
print(f"Highest Mark: {round(max(averages),2)}")
print(f"Lowest Mark: {round(min(averages),2)}")
print("---------------------------------")


while True:
    userInput=int(input("1=Search         Any=Exit\n"))

    if userInput==1:
        search_student()

    else:
        break