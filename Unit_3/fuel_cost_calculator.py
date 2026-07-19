#With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:
#1. Ask the user how many kilometers they want to drive.
#2. Ask them for the current petrol price per liter (this can be aZdecimal, like R22.45).
#3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
#(Formula: liters_needed = kilometers / 10).
#4. Calculate the total cost (liters_needed * petrol_price).
#5. Use type casting to ensure your numbers work, and use round() to format the
#final cost to 2 decimal places.


#Inputs
distance=float(input("Enter your travel distance in kilometers: "))
current_price=float(input("Enter the current price per litre: "))

#Calculations
litres_needed=float(distance)/10
total_cost=litres_needed*current_price

#Output
print(f"For a {distance}km journey, It'll consume {round(litres_needed,2)} litres of fuel amounting to a total of R{round(total_cost,2)}")