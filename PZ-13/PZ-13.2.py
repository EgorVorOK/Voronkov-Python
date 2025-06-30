import random
"""
Сгенерировать двумерный список, в которой нечетные элементы заменяются на 0.
"""

rows = 3
columns = 3
matrix = [[random.randint(1, 10) for c in range(columns)] for r in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] % 2 != 0:
            matrix[i][j] = 0

print("\nМатрица после замены нечетных элементов на 0:")
for row in matrix:
    print(row)