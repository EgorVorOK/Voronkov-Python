"""
Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
Добавьте методы для вычисления процентных начислений и снятия денег.
"""


class Bank:
    def __init__(self, initial_amount=0, interest_rate=0):
        self.balance = initial_amount
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Счет пополнен на {amount}. Текущий баланс: {self.balance}"
        else:
            return "Сумма пополнения должна быть положительной"

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Снято {amount}. Текущий баланс: {self.balance}"
            else:
                return "Недостаточно средств на счете"
        else:
            return "Сумма снятия должна быть положительной"

    def calculate_interest(self, months):
        if months <= 0:
            return None

        interest = self.balance * self.interest_rate / 100 * months / 12
        return f"Процентные начисления за {months} мес.: {interest:.2f}"

    def __str__(self):
        return f"Баланс: {self.balance:.2f}, Процентная ставка: {self.interest_rate}% годовых"


my_account = Bank(initial_amount=1000, interest_rate=5)
print(my_account)

print("\n1. Пополнение счета:")
print(my_account.deposit(500))

print("\n2. Снятие денег:")
print(my_account.withdraw(200))
print(my_account.withdraw(2000))

print("\n3. Расчет процентов:")
print(my_account.calculate_interest(6))

print("\nИтоговое состояние счета:")
print(my_account)
