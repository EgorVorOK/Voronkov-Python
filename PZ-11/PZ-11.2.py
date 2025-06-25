"""
Из предложенного текстового файла (text18-5.txt) вывести на экран его содержимое,
количество символов в тексте. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно заменив символы нижнего регистра на верхний.
"""

with open('text18-5.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print("Содержимое файла:")
print(content)
print("\nКоличество символов в тексте:", len(content))

upper_content = content.upper()

with open('poem_upper.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(upper_content)

print("\nТекст в верхнем регистре сохранен в файл 'poem_upper.txt'")