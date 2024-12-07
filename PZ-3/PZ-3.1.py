
try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    if a > 0:
        print("Неравенство A > 0 справедливо.")
    else:
        print("Неравенство A > 0 несправедливо.")

    if b < -2:
        print("Неравенство B < -2 справедливо.")
    else:
        print("Неравенство B < -2 несправедливо.")
except Exception as e:
    print(f"ОШИБКА: {e}")