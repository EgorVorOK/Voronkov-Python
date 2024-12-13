#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг
#конфет.
try:
    price = int(input("Введите цену за 1 кг конфет: "))
    weight = 1.0
    while weight <= 2:
        print("Цена за ", weight, "равна ",  price * weight)
        weight += 0.2
except ValueError:
    print("ОШИБКА!")
