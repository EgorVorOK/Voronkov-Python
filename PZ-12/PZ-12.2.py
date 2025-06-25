"""
Составить генератор (yield), который переведет символы строки из нижнего
регистра в верхний.
"""

def upper_case_generator(input_string):
    for char in input_string:
        yield char.upper()

text = "тестовая строка"

gen = upper_case_generator(text)

print("Постепенная обработка:")
for upper_char in gen:
    print(upper_char, end='')
print("\n")