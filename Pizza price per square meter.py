import math

def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2) / 10000  # Convert to square meters
    return price / area

def main():
    diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
    price1 = float(input("Enter the price of the first pizza (€): "))
    diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
    price2 = float(input("Enter the price of the second pizza (€): "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    print(f"First pizza unit price: €{unit_price1:.2f} per m²")
    print(f"Second pizza unit price: €{unit_price2:.2f} per m²")

    if unit_price1 < unit_price2:
        print("The first pizza offers better value for money.")
    else:
        print("The second pizza offers better value for money.")

if __name__ == "__main__":
    main()
