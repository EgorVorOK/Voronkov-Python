#Дано целое число N (1 < N < 26). Вывести N последних строчных (то есть маленьких)
#букв латинского алфавита в обратном порядке (начиная с буквы «z»).

try:
    sp = "abcdefghijklmnopqrstuvwxyz"
    n = int(input("Введите число, выполняющее условие: 1 < N < 26 "))
    if n < 1 or n > 26:
        raise ValueError
    new_sp = sp[::-1]
    print((new_sp[:n]))
except ValueError:
    print("ОШИБКА!")



