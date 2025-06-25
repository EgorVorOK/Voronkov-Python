"""
Из последовательности на п целых чисел создать новую последовательность, в
которой каждый последующий элемент равен квадрату суммы двух соседних элементов.
"""

n = int(input("Введите количество элементов: "))
sequence = []
for i in range(n):
    num = int(input(f"Введите {i+1}-е число: "))
    sequence.append(num)

new_sequence = []
for i in range(len(sequence) - 1):
    sum_neighbors = sequence[i] + sequence[i+1]
    new_element = sum_neighbors ** 2
    new_sequence.append(new_element)

print("\nИсходная последовательность:", sequence)
print("Новая последовательность:", new_sequence)