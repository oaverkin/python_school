import os


def new_file():
    filename = input("Введите название файла для записи текста: ")
    text = input("Введите текст для записи в файл: ")
    with open(filename, 'w') as file:
        file.write(text)
    return filename


def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        word_count = len(content.split())
    print(f"Содержимое файла {filename}: {content}")
    return word_count


def average_length(filename1, filename2):
    with open(filename1, 'r') as input_file:
        with open(filename2, 'w') as output_file:
            first_10_chars = input_file.read(10)
            output_file.write(first_10_chars)
    print(f"Первые 10 символов {first_10_chars} в файле {filename2}")

    with open(filename2, 'r') as file:
        content = file.read()
        words = content.split()
        average_word_length = sum(len(word) for word in words) / len(words)
    return average_word_length


def compare_files(filename1, filename2):
    words_in_file1 = count_words(filename1)
    words_in_file2 = count_words(filename2)

    if words_in_file1 > words_in_file2:
        print(f"В файле {filename1} больше слов. (Слов {words_in_file1})")
    elif words_in_file1 < words_in_file2:
        print(f"В файле {filename2} больше слов. (Слов {words_in_file2})")
    else:
        print("Количество слов в обоих файлах одинаково.")


def delete_files(*filenames):
    for filename in filenames:
        os.remove(filename)


# 1 Запросіть від користувача текст і запишіть його у файл з вказаною назвою.
filename1 = new_file()

# 2 Прочитайте вміст створеного в попередньому завданні файлу і виведіть кількість слів у тексті.
word_count = count_words(filename1)
print(f"Количество слов в файле {filename1}: {word_count}")

# 3 Створіть новий файл, в який запишіть тільки перші 10 символів з вмісту попереднього файлу. Потім знайдіть середню довжину слова у цьому новому файлі.
filename2 = "file_10_chars.txt"
average_word_length = average_length(filename1, filename2)
print(f"Средняя длина слова в новом файле {filename2}: {average_word_length}")

# 4 Створіть ще один файл з іншим текстом. Порівняйте кількість слів у цьому файлі з кількістю слів у першому файлі та виведіть повідомлення про те, який файл містить більше слів.
filename3 = new_file()
compare_files(filename1, filename3)

delete_files(filename1, filename2, filename3)