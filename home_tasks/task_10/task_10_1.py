class Automobile:
    def __init__(self, brand, model, manufacture_year, max_speed):
        self.brand = brand
        self.model = model
        self.manufacture_year = manufacture_year
        self.max_speed = max_speed

    def car_info(self):
        print(f"Car brand - {self.brand}\n"
              f"Model - {self.model}\n"
              f"Manufacture year - {self.manufacture_year}\n"
              f"Max speed - {self.max_speed} Km/h\n")


car1 = Automobile("BMW", "X5", "2016", "220")
car1.car_info()

# Car brand - BMW
# Model - X5
# Manufacture year - 2016
# Max speed - 220 Km/h
