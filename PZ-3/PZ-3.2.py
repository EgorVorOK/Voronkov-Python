

suits = {
    1: "пики",
    2: "трефы",
    3: "бубны",
    4: "червы"
}

dignities = {
    11: "Валет",
    12: "Дама",
    13: "Король",
    14: "Туз"
}
try:
    num = int(input("Введите трехзначное число: "))
    suit = num // 100
    dignity = num % 100
    print(dignities[dignity], suits[suit])
except Exception as e:
    print("ОШИБКА: такой карты нет!")
