"""Дано целое число N(>2). Сформировать и вывести целочисленный список
размера 10, содержащий 10 первых элементов последовательности чисел
Фибоначчи Fk: F1 = 1, F2 = 1, Fk = Fk-2 + Fk-1, K = 3,4...."""

fibonacci = [1, 1]

for i in range(2, 10):
    next = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next)

print(fibonacci)
