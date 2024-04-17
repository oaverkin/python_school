class Animal:
    def __init__(self, animal_kind):
        self.animal_kind = animal_kind


class Dog(Animal):
    def bark(self):
        print("Гав!")


class Cat(Animal):
    def meow(self):
        print("Мяу!")


dog = Dog("Собака")
cat = Cat("Кот")


print(dog.animal_kind)
dog.bark()

print(cat.animal_kind)
cat.meow()
