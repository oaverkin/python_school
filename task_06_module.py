import random

rnd_number = random.randint(1, 20)

names = ['Олег', 'Даша', 'Славик', 'Оля', 'Вадим', 'Марк']


def random_number(number):
    print("Твое случайное число:", number)


def random_name(name):
    print("Случайное имя:", random.choice(name))


