numbers = []

while True:
    user_input = input("Enter a number (or press Enter to finish): ")

    if user_input == "":
        break

    numbers.append(int(user_input))

numbers.sort(reverse=True)

print("The top 5 greatest numbers are:")
for number in numbers[:5]:
    print(number)
