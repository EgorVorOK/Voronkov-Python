"""
В двумерном списке элементы второго столбца возвести в квадрат.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

for row in matrix:
    row[1] = row[1] ** 2
    
print("\nМатрица после преобразования:")
for row in matrix:
    print(row)