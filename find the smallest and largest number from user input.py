numbers = []
while True:
    user_input = input("Enter a number (or press Enter to stop): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")
