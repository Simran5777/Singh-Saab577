size_limit = 42
zander_length = float(input("Enter the length of the zander in centimeters: "))

if zander_length >= size_limit:
    print("The zander meets the size limit.")
else:
    print(f"Release the zander back into the lake. It is {size_limit - zander_length:.2f} cm below the size limit.")
