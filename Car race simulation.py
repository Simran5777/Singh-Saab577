import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(registration, max_speed))

race_over = False
while not race_over:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_over = True
            break

print(f"{'Reg Number':<10} {'Max Speed':<10} {'Current Speed':<15} {'Distance Travelled':<20}")
for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<15} {car.travelled_distance:<20}")
