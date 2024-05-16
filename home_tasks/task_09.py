map = {
    'Верхняя одежда': "Куртки",
    'Обувь': {
        'Кроссовки': "Nike",
        'Кеды': {
            'NB': {
                'Размер': 43,
                'Цвет': 'Красные'
            },
            'Nike': {
                'Размер': 43,
                'Цвет': 'Красные'
            },
            'Puma': {
                'Размер': 43,
                'Цвет': 'Красные'
            },
            ' Adidas': {
                'Размер': 43,
                'Цвет': 'Красные'
            },
        }
    }
}

print("1 Напишіть рекурсивну функцію, яка обходить вкладений словник та виводить всі його ключі.")
def print_keys(map):
    if isinstance(map, dict):
        for key in map.keys():
            print(key)
            print_keys(map[key])

print_keys(map)

print("2 Розширте попередню задачу, щоб рекурсивна функція підраховувала кількість значень у всіх вкладених словниках.")
def print_keys_and_count_values(map):
    count = 0
    if isinstance(map, dict):
        for value in map.values():
            count += print_keys_and_count_values(value)
    else:
        count += 1
    return count

print("Number of values:", print_keys_and_count_values(map))


print("3 Створіть рекурсивну функцію, яка обходить вкладений словник та виводить всі значення певного ключа.")
def print_values_of_key(map, target_key):
    if isinstance(map, dict):
        for key, value in map.items():
            if key == target_key:
                print(value)
            print_values_of_key(value, target_key)

print_values_of_key(map, 'Кеды')

print("4 Розширте попередню задачу, щоб рекурсивна функція підраховувала кількість входжень певного значення у всіх вкладених словниках.")
def count_and_print_values(map, target_value):
    count = 0
    if isinstance(map, dict):
        for value in map.values():
            count += count_and_print_values(value, target_value)
    elif map == target_value:
        count += 1
    return count


count = count_and_print_values(map, "Nike")
print(f"Total count: {count}")
