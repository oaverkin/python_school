speed = int(2)
height = int(20)

time = 1
x = 0
y = height
while y > 0:
    print(f"time={round(time, 1)}, x={round(x, 1)}, y={round(y, 1)}")
    time += 0.1
    x = speed * time
    y = height - (9.8 * time**2) / 2
