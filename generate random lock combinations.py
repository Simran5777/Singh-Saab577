import random

code_3_digits = [random.randint(0, 9) for _ in range(3)]
code_4_digits = [random.randint(1, 6) for _ in range(4)]

print(f"3-digit combination: {code_3_digits}")
print(f"4-digit combination: {code_4_digits}")
