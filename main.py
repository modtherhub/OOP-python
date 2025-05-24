from car import Car

car_1 = Car("Golf", "VW", 2024, "blue")
car_2 = Car("Mustang", "Ford", 2020, "black")

print(car_2.color)
print(car_2.make)
print(car_2.model)
print(car_2.year)

car_2.drive()
car_2.stop()