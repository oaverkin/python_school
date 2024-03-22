import random

# 1
heroes = "Spiderman, Ironman, Batman, Superman, Wonder Woman"
heroes_list = heroes.split(", ")

print("Heroes:")
for hero in heroes_list:
    print(hero)

# 2
secret_number = random.randint(1, 20)
print("Угадай число от 1 до 20!")
number = 0
while number != secret_number:
    number = int(input("Введіть вашу догадку: "))
    if number > secret_number:
        print("Число меньше.")
    if number < secret_number:
        print("Число больше.")
print("Вы угадали число! Поздравляю!")

# 3
text = "Programming is awesome!"
a = 0

for i in text:
    if i == 'a':
        a += 1

print("Колличество буквы 'а' в строке:", a)

# 4
true_password = input("Введите ваш пароль: ")
entered_password = ''

while entered_password != true_password:
    entered_password = input("Повторите ваш пароль: ")
    if entered_password != true_password:
        print("Вы ввели не верный пароль.")
print("Вы ввели верный пароль.")

# 5
string = input("Введите строку: ")
new_string = ""
i = 0

while i < len(string):
    char = string[i]

    if char.islower():
        new_string += char.upper()
    elif char.isupper():
        new_string += char.lower()
    else:
        new_string += char
    i += 1

print(new_string)
