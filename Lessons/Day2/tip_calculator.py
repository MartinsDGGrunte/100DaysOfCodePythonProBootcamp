print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_as_decimal = int(tip_percentage) / 100
tip_value = float(total_bill) * tip_as_decimal
total_bill_plus_tip = float(total_bill) + tip_value
num_of_people_dining = input("How many people to split the bill? ")
per_person_bill = round(total_bill_plus_tip / int(num_of_people_dining), 2)
print(f'Each person should pay: ${per_person_bill}')