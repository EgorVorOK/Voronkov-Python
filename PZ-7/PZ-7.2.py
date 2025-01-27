# Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать
# строку, выполнив циклическую замену каждой буквы на букву того же регистра,
# расположенную в алфавите на K-й позиции после шифруемой буквы (например, для
# K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.). Букву «ё»
# в алфавите не учитывать, знаки препинания и пробелы не изменять.

def encr_text(rus_text, k):
    low_alph = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    upp_alph = [chr(i) for i in range(ord('А'), ord('Я') + 1)]

    text = ""

    for char in rus_text:
        if char in low_alph:
            nindex = (low_alph.index(char) + k) % len(low_alph)
            text += low_alph[nindex]
        elif char in upp_alph:
            nindex = (upp_alph.index(char) + k) % len(upp_alph)
            text += upp_alph[nindex]
        else:
            text += char

    return text


try:
    rus_tex = input("Введите строку-предложение на русском языке: ")
    k = int(input("Введите число, выполняющее условие 0 < K < 10: "))

    if k <= 0 or k >= 10:
        raise ValueError("K должно быть в диапазоне от 1 до 9.")

    encr_res = encr_text(rus_tex, k)
    print("Зашифрованный текст:", encr_res)

except ValueError as e:
    print("ОШИБКА!!!", e)
