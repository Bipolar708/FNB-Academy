#Calculating the tip

#inputs
bill=float(input("Enter the bill amount: R"))
tip=0.15 #Written in decimal

#Calculations
val_tip=bill*tip
total_cost=bill+val_tip

#Output
print(f"Here is the tip: {val_tip}")
print(f"Here is the rounded tip: {round(val_tip,2)}")

print(f"Here is the total cost: {total_cost}")
print(f"Here is the rounded total cost: {round(total_cost,2)}")