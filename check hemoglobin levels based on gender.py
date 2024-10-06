gender = input("Enter your biological gender (male/female): ").lower()
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin is low.")
    elif 117 <= hemoglobin <= 155:
        print("Hemoglobin is normal.")
    else:
        print("Hemoglobin is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin is low.")
    elif 134 <= hemoglobin <= 167:
        print("Hemoglobin is normal.")
    else:
        print("Hemoglobin is high.")
else:
    print("Invalid gender.")
