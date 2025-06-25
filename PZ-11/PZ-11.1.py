"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Сумма элементов:
Элементы, умноженные на минимальный элемент:
"""

with open('numbers.txt', 'w', encoding='utf-8') as file:
    file.write("5 -3 10 -8 2 0 7 -1")

with open('numbers.txt', 'r', encoding='utf-8') as file:
    numbers = list(map(int, file.read().split()))

count = len(numbers)
sum_numbers = sum(numbers)
min_num = min(numbers)
multiplied = [num * min_num for num in numbers]

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write("Исходные данные: " + str(numbers) + '\n')
    file.write("Количество элементов: " + str(count) + '\n')
    file.write("Сумма элементов: " + str(sum_numbers) + '\n')
    file.write("Элементы, умноженные на минимальный элемент: " + str(multiplied))
