"""Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
порядке элементы списка, расположенные между элементами AK и AL, включая эти
элементы."""


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(a)

try:
    k = int(input("Введите индекс k от 0 до 9 в соответствии с условием (1 < K < L): "))
    l = int(input("Введите индекс l от 0 до 9 в соответствии с условием (1 < K < L): "))
    if k > l or k < 0 or k > 9 or l > 9 or l < 1 or k == l:
        raise ValueError
    a[k:l+1] = a[k:l+1][::-1]
    print(a)
except ValueError:
    print("ОШИБКА!")
