#Build a Python calculator called calculator.py that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. The calculator must handle user input safely using type casting and display results clearly using f-strings.



#inputs
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

#Calculations
if num2==0:
    print("Second number cannot be Zero(0) try a different number")
else:
    addition=num1+num2
    subtraction=num1-num2
    multiplication=num1*num2
    division=num1/num2
    floor_division=num1//num2
    modulus=num1%num2

    #Outputs
    print(f"Addition: {round(addition,2)}")
    print(f"Subtraction: {round(subtraction,2)}")
    print(f"Multiplication: {round(multiplication,2)}")
    print(f"Division: {round(division,2)}")
    print(f"Floor Division: {round(floor_division,2)}")
    print(f"Modulus: {round(modulus,2)}")





    