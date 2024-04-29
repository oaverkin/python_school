class Transport:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, accelerate):
        self.speed += accelerate

    def brake(self, brake):
        self.speed -= brake


class Car(Transport):
    def __init__(self, speed=0):
        super().__init__(speed)

    def accelerate(self, accelerate):
        super().accelerate(accelerate)
        print("Автомобиль ускоряется")

    def brake(self, brake):
        super().brake(brake)
        print("Автомобиль тормозит")


class Bicycle(Transport):
    def __init__(self, speed=0):
        super().__init__(speed)

    def accelerate(self, accelerate):
        super().accelerate(accelerate)
        print("Велосипед ускоряется")

    def brake(self, brake):
        super().brake(brake)
        print("Велосипед тормозит")


car = Car()
bicycle = Bicycle()

car.accelerate(20)
print("Скорость автомобиля:", car.speed)

bicycle.accelerate(10)
print("Скорость велосипеда:", bicycle.speed)

car.brake(10)
print("Скорость автомобиля после торможения:", car.speed)

bicycle.brake(5)
print("Скорость велосипеда после торможения:", bicycle.speed)
