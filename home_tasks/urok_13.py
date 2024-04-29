# Вариант без elif и без равного веса
x=int(input("Вага Богдана: "))
y=int(input("Вага Наталки: "))
if x>y:
    max = x
    max_name = "Богдан"
else:
    max = y
    max_name = "Наталка"
print("Більше важить", max_name, "(", max, "кг.)")

#Вариант с elif с одинкаовым весом
x=int(input("Вага Богдана: "))
y=int(input("Вага Наталки: "))
if x > y:
    print("Більше важить Богдан","(", x,"кг.)")
elif x < y:
    print("Більше важить Наталка", "(", y, "кг.)")
else:
    print("Вага одинакова")
