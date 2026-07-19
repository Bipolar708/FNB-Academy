#inputs
weight=int(input("Enter your weight: "))
metric=input("(K)g or (L)bs: ")

#Calculations
if metric.upper()=="L":#Revised form (metric=="L" or metric=="l")
    print("Weight in Kgs :"+ str((weight*0.45)) )

else:#Revised form (elif metric=="K" or metric=="k")
    print("Weight in Lbs :"+ str(weight/0.45))