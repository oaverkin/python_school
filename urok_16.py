import turtle

v0 = int(input("Введите начальную скорость: "))
h = int(input("Введите начальную высоту: "))
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(h)

t = 0.1
x = 0
y = h
while y > 0:
    print(f"t={round(t, 1)}, x={round(x, 1)}, y={round(y, 1)}")
    t += 0.1
    x = v0 * t
    y = h - (9.8 * t**2) / 2
    turtle.goto(x, y)

turtle.up()
turtle.goto(0, h)
turtle.write(h)
turtle.goto(x, 0)
turtle.write(x)



