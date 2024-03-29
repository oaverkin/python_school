import math
import random
import string
import datetime
import time

task = 0
while task != 11:
    task = int(input("\n"
          "1 - Як працює поділ із залишком (%)?\n"
          "2 - Як працює цілий поділ (//)?\n"
          "3 - Випадкова послідовність\n"
          "4 - Знаходження остачі від ділення на 2\n"
          "5 - Визначання поточного часу та дати\n"
          "6 - Скільки днів у користувача до дня народження\n"
          "7 - Випадкове ім'я та прізвище\n"
          "8 - Обчислння різниці між датами в секундах\n"
          "9 - Список аргументів командного рядка\n"
          "10 - Таймер у секундах\n"
          "11 - Выход\n"
          "Введите номер задания: "))

    if task == 1:
        print("Задание 1: Опишіть своїми словами як ви розумієте як працює поділ із залишком (%)?")
        print("Ответ: Деление с остатком выполняет деление одного числа на другое и возвращает остаток от этого деления")
    elif task == 2:
        print("Задание 2: Опишіть своїми словами як ви розумієте як працює цілий поділ (//)")
        print("Ответ: Целочисленное деление выполняет деление двух чисел, возвращается только целая часть, а дробная часть не учитывается.")
    elif task == 3:
        print("Задание 3: Напишіть програму, яка генерує випадкову послідовність символів (маленьких та великих букв та цифр) заданої довжини за допомогою модуля random.\n")


        def generate_random_string(length):
            chars = string.ascii_letters + string.digits
            random_string = ''.join(random.choice(chars) for _ in range(length))
            return random_string


        length = int(input("Введите длину случайной последовательности символов: "))
        random_seq = generate_random_string(length)
        print("Случайная последовательность символов:", random_seq)

    elif task == 4:
        print("Задание 4: Реалізуйте програму, яка перевіряє, чи є введене користувачем число парним, використовуючи функцію math.fmod() для знаходження остачі від ділення на 2.\n")

        def is_even():
            user_input = int(input("Введите число: "))
            remainder = math.fmod(user_input, 2)
            if remainder > 0:
                print(f"Число {user_input} не четное.")
            else:
                print(f"Число {user_input} четное.")

        is_even()
    elif task == 5:
        print("Задание 5: Реалізуйте програму, яка визначає поточний час та дату за допомогою модуля datetime.\n")

        current_datetime = datetime.datetime.now()
        formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("Текущая дата и время:", formatted_date)

    elif task == 6:
        print("Задание 6: Напишіть програму, яка приймає введені користувачем його ім'я та дату народження,\n"
              "а потім виводить інформацію про те, через скільки днів у користувача день народження. Використовуйте модуль datetime.\n")


        def days_until_birthday(birthdate):
            today = datetime.date.today()
            next_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
            if next_birthday < today:
                next_birthday = datetime.date(today.year + 1, birthdate.month, birthdate.day)
            days_until = (next_birthday - today).days
            return days_until


        def get_birthdate():
            birthdate_str = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
            birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
            return birthdate


        name = input("Введите ваше имя: ")
        birthdate = get_birthdate()
        days_until = days_until_birthday(birthdate)
        if days_until == 0:
            print(f"С днем рождения, {name}!")
        else:
            print(f"До вашего дня рождения осталось {days_until} дней.")

    elif task == 7:
        print("Задание 7: Напишіть програму, яка генерує випадковий ім'я та прізвище за допомогою модуля random та списку доступних імен і прізвищ.\n")

        firstname_list = ['Олег', 'Даша', 'Славик', 'Оля', 'Вадим', 'Марк']
        lastname_list = ['Николаенко', 'Васильев', 'Гершкович', 'Василиади', 'Дмитрук', 'Савченко', 'Анишин']


        def random_person(firstname_list, lastname_list):
            print(f"Случайное имя и фамилия: {random.choice(firstname_list)} {random.choice(lastname_list)}")


        random_person(firstname_list, lastname_list)

    elif task == 8:
        print("Задание 8: Напишіть програму, яка приймає дві дати в форматі YYYY-MM-DD та обчислює різницю між ними в секундах за допомогою модуля datetime.\n")

        def get_date():
            date_str = input("Введите дату в формате YYYY-MM-DD: ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").timestamp()
            return date

        print("Введите две даты для вычисления разницы в секундах.")
        date1 = get_date()
        date2 = get_date()

        diff = date2 - date1
        print("Разница между датами в секундах:", diff)
    elif task == 9:
        print("Задание 9: Створіть скрипт, який виводить на екран список аргументів командного рядка, переданих програмі, використовуючи модуль sys.\n")
        print("Задание 9 выполнено в файле task_08_multi_args\n")
    elif task == 10:
        print("Задание 10: Реалізуйте простий таймер, який приймає час у секундах від користувача та відлічує до його завершення, використовуючи модуль time.")


        def timer(seconds):
            print(f"Таймер запущен на {seconds} секунд.")
            for remaining_time in range(seconds, 0, -1):
                print(f"Осталось времени: {remaining_time} сек.")
                time.sleep(1)
            print("Время истекло!")

        seconds = int(input("Введите время в секундах: "))
        timer(seconds)

    elif task == 11:
        print("Вы вышли из программы!\n")
    else:
        print("Не верный выбор!\n")

