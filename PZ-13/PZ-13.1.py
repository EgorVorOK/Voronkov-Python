import random
"""
В двумерном списке элементы второго столбца возвести в квадрат.
"""

rows = 3
columns = 3
matrix = [[random.randint(1, 10) for c in range(columns)] for r in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

for row in matrix:
    row[1] = row[1] ** 2
    
print("\nМатрица после преобразования:")
for row in matrix:
    print(row)