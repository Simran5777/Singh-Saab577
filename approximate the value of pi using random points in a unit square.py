import random

def approximate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside_circle += 1

    pi_approx = 4 * (inside_circle / num_points)
    return pi_approx

points = int(input("How many random points do you want to generate? "))
pi_value = approximate_pi(points)
print(f"Approximate value of pi: {pi_value}")
