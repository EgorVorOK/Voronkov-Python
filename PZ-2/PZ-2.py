

v1 = int(input("Введите скорость первого автомобиля: "))
v2 = int(input("Введите скорость второго автомобиля: "))
s = int(input("Введите расстояние между ними: "))
t = int(input("Введите время движения: "))
print(abs(s - (v1 * t) - (v2 * t)))
