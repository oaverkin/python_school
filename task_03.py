clothing_type = input("Який одяг ви хочете купити?\n1 - повсякденний\n2 - діловий\n"
                      "Виберете потрібну цифру: ")

if clothing_type == "повсякденний":
    item = input("Що ви хочете придбати? (футболку або штани): ")
    if item == "футболку":
        color = input("Якого кольору ви хочете футболку? (червоний, синій, зелений, жовтий, помаранчевий): ")
        if color in ["червоний", "синій", "зелений", "жовтий", "помаранчевий"]:
            print("Ви замовили {} {} повсякденного типу.".format(color, item))
        else:
            print("Такого кольору не існує.")
    elif item == "штани":
        color = input("Якого кольору ви хочете штани? (чорний, сірий, коричневий): ")
        if color in ["чорний", "сірий", "коричневий"]:
            print("Ви замовили {} {} повсякденного типу.".format(color, item))
        else:
            print("Такого кольору не існує.")
    else:
        print("Такого товару не існує.")
elif clothing_type == "діловий":
    item = input("Що ви хочете придбати? (сорочку або взуття): ")
    if item == "сорочку":
        color = input("Якого кольору ви хочете сорочку? (біла, голуба, блакитна): ")
        if color in ["біла", "голуба", "блакитна"]:
            print("Ви замовили {} {} ділового типу.".format(color, item))
        else:
            print("Такого кольору не існує.")
    elif item == "взуття":
        color = input("Якого кольору ви хочете взуття? (чорне, коричневе): ")
        if color in ["чорне", "коричневе"]:
            print("Ви замовили {} {} ділового типу.".format(color, item))
        else:
            print("Такого кольору не існує.")
    else:
        print("Такого товару не існує.")
else:
    print("Такого типу одягу не існує.")