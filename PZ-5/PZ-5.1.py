# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.

def horizontal(length, char='$'):
    print(char * length)

def vertical(height, char='$'):
    for i in range(height):
        print(char)

def frame(word, char='$'):
    word_length = len(word)
    horizontal(word_length + 4, char)
    print(f"{char} {word} {char}")
    horizontal(word_length + 4, char)

try:
    word = input("Введите слово, которое хотите заключить в рамку: ")
    frame(word)
except:
    print("ОШИБКА!")
