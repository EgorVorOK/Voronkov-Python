"""
Приложение БАНК для отслеживания накапливаемых на счетах клиентов банка
сумм. Таблица Клиент должна содержать следующую информацию: Код клиента,
Клиент (Ф.И.О.), Периодический платеж, Годовой %, Срок вклада, Пластиковая карта
(логическое поле), Конечная сумма.
"""

import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Клиент (
                      Код_клиента INTEGER PRIMARY KEY AUTOINCREMENT,
                      ФИО TEXT NOT NULL,
                      Периодический_платеж REAL NOT NULL,
                      Годовой_процент REAL NOT NULL,
                      Срок_вклада INTEGER NOT NULL,
                      Пластиковая_карта BOOLEAN,
                      Конечная_сумма REAL,
                      Дата_открытия TEXT)''')
    conn.commit()
    conn.close()

def add_client():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    print("\nДобавление нового клиента:")
    fio = input("ФИО клиента: ")
    payment = float(input("Периодический платеж: "))
    percent = float(input("Годовой процент: "))
    term = int(input("Срок вклада (мес): "))
    card = input("Пластиковая карта (да/нет): ").lower() == 'да'

    total = calculate_total(payment, percent, term)

    cursor.execute('''INSERT INTO Клиент 
                      (ФИО, Периодический_платеж, Годовой_процент, 
                       Срок_вклада, Пластиковая_карта, Конечная_сумма, Дата_открытия)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (fio, payment, percent, term, card, total, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()
    print("Клиент успешно добавлен!")

def calculate_total(payment, percent, term):
    monthly_percent = percent / 12 / 100
    total = 0
    for _ in range(term):
        total = (total + payment) * (1 + monthly_percent)
    return round(total, 2)

def view_clients():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM Клиент''')
    clients = cursor.fetchall()

    print("\nСписок клиентов:")
    print("= " * 100)
    print("| {:3} | {:30} | {:8} | {:5}% | {:3}мес | {:^8} | {:12} | {:10} |".format(
        "Код", "ФИО", "Платеж", "Проц", "Срок", "Карта", "Конечная сумма", "Дата"))
    print("= " * 100)

    for client in clients:
        card = "Да" if client[5] else "Нет"
        print("| {:3} | {:30} | {:8.2f} | {:5.1f}% | {:3}мес | {:^8} | {:12.2f} | {:10} |".format(
            client[0], client[1], client[2], client[3], client[4], card, client[6], client[7]))

    conn.close()


init_db()

while True:
    print("\nБАНК - Управление клиентами")
    print("1. Добавить клиента")
    print("2. Просмотреть всех клиентов")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_client()
    elif choice == '2':
        view_clients()
    elif choice == '3':
        break
    else:
        print("Неверный ввод, попробуйте снова.")
