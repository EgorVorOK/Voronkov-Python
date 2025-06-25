"""
Сгенерировать двумерный список, в которой нечетные элементы заменяются на 0.
"""

m = 3
n = 3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(m):
    for j in range(n):
        if matrix[i][j] % 2 != 0:
            matrix[i][j] = 0

print("\nМатрица после замены нечетных элементов на 0:")
for row in matrix:
    print(row)