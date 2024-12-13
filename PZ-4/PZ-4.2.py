#Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
#деления, найти количество и сумму его цифр.

def count_and_sum_digits(n):
    count = 0
    total_sum = 0

    while n > 0:
        last_digit = n % 10
        count += 1
        total_sum += last_digit
        n //= 10
    return count, total_sum

try:
    n = int(input("Введите целое число N (> 0): "))
    if n > 0:
        print(count_and_sum_digits(n))
        digit_count, digit_sum = count_and_sum_digits(n)
        print(f"Количество цифр: {digit_count}")
        print(f"Сумма цифр: {digit_sum}")
    else:
        print("Число должно быть больше 0.")
except ValueError:
    print("ОШИБКА!")
