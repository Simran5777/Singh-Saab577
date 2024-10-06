talents = float(input("Enter the mass in talents (leiviskä): "))
pounds = float(input("Enter the mass in pounds (naula): "))
lots = float(input("Enter the mass in lots (luoti): "))

talent_to_kg = 8.512
pound_to_kg = 0.4256
lot_to_kg = 0.0133

total_kg = talents * talent_to_kg + pounds * pound_to_kg + lots * lot_to_kg
kg_part = int(total_kg)
grams_part = (total_kg - kg_part) * 1000

print(f"The total mass is {kg_part} kilograms and {grams_part:.0f} grams.")
