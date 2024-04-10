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
            }
        }
    }
}

print("1 Напишіть рекурсивну функцію, яка обходить вкладений словник та виводить всі його ключі.")
def print_keys(map):
    for key in map:
        print(key)
        if isinstance(map[key], dict):
            print_keys(map[key])

print_keys(map)

print("2 Розширте попередню задачу, щоб рекурсивна функція підраховувала кількість значень у всіх вкладених словниках.")
def print_keys_and_count_values(map, count=0):
    for key, value in map.items():
        if isinstance(value, dict):
            print(key)
            count = print_keys_and_count_values(value, count)
        else:
            print(key)
            count += 1
    return count

count = print_keys_and_count_values(map)
print("Total values", count)

print("3 Створіть рекурсивну функцію, яка обходить вкладений словник та виводить всі значення певного ключа.")
def print_values(map, key):
    if isinstance(map, dict):
        for k, v in map.items():
            if k == key:
                print(v)
            elif isinstance(v, dict):
                print_values(v, key)

print_values(map, 'Кеды')

print("4 Розширте попередню задачу, щоб рекурсивна функція підраховувала кількість входжень певного значення у всіх вкладених словниках.")
def count_and_print_values(map, key, count=0):
    if isinstance(map, dict):
        for k, v in map.items():
            if k == key:
                print(v)
                count += 1
            elif isinstance(v, dict):
                count = count_and_print_values(v, key, count)
    return count

count = count_and_print_values(map, "Цвет")
print(f"Total count: {count}")
