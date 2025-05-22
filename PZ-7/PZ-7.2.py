# Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать
# строку, выполнив циклическую замену каждой буквы на букву того же регистра,
# расположенную в алфавите на K-й позиции после шифруемой буквы (например, для
# K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.). Букву «ё»
# в алфавите не учитывать, знаки препинания и пробелы не изменять.

def encrypt_sentence(sentence, K):
    russian_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    russian_upper = russian_lower.upper()
    encrypted = []

    for char in sentence:
        if char in russian_lower:
            original_pos = russian_lower.index(char)
            new_pos = (original_pos + K) % 32
            encrypted.append(russian_lower[new_pos])
        elif char in russian_upper:
            original_pos = russian_upper.index(char)
            new_pos = (original_pos + K) % 32
            encrypted.append(russian_upper[new_pos])
        else:
            encrypted.append(char)

    return ''.join(encrypted)

try:
    sentence = input("Введите предложение на русском: ")
    K = int(input("Введите число K (0 < K < 10): "))

    if 0 < K < 10:
        encrypted_sentence = encrypt_sentence(sentence, K)
        print("Зашифрованное предложение:", encrypted_sentence)
    else:
        print("Число K должно быть в диапазоне 0 < K < 10")

except ValueError as e:
    print("ОШИБКА!!!", e)
