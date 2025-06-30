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

def search_clients():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    print("\nПоиск клиентов:")
    print("1. По ФИО")
    print("2. По наличию пластиковой карты")
    print("3. По сроку вклада (больше указанного)")
    choice = input("Выберите критерий поиска: ")

    if choice == '1':
        fio = input("Введите ФИО или часть ФИО: ")
        cursor.execute("SELECT * FROM Клиент WHERE ФИО LIKE ?", (f'%{fio}%',))
    elif choice == '2':
        card = input("Есть пластиковая карта? (да/нет): ").lower() == 'да'
        cursor.execute("SELECT * FROM Клиент WHERE Пластиковая_карта = ?", (card,))
    elif choice == '3':
        term = int(input("Введите минимальный срок вклада (мес): "))
        cursor.execute("SELECT * FROM Клиент WHERE Срок_вклада >= ?", (term,))
    else:
        print("Неверный выбор.")
        return

    clients = cursor.fetchall()
    if not clients:
        print("Клиенты не найдены.")
        return

    print("\nРезультаты поиска:")
    print("= " * 100)
    print("| {:3} | {:30} | {:8} | {:5}% | {:3}мес | {:^8} | {:12} | {:10} |".format(
        "Код", "ФИО", "Платеж", "Проц", "Срок", "Карта", "Конечная сумма", "Дата"))
    print("= " * 100)

    for client in clients:
        card = "Да" if client[5] else "Нет"
        print("| {:3} | {:30} | {:8.2f} | {:5.1f}% | {:3}мес | {:^8} | {:12.2f} | {:10} |".format(
            client[0], client[1], client[2], client[3], client[4], card, client[6], client[7]))

    conn.close()

def delete_client():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    print("\nУдаление клиента:")
    print("1. По коду клиента")
    print("2. По ФИО")
    print("3. Клиентов без пластиковой карты")
    choice = input("Выберите критерий удаления: ")

    if choice == '1':
        client_id = int(input("Введите код клиента: "))
        cursor.execute("DELETE FROM Клиент WHERE Код_клиента = ?", (client_id,))
    elif choice == '2':
        fio = input("Введите ФИО клиента: ")
        cursor.execute("DELETE FROM Клиент WHERE ФИО = ?", (fio,))
    elif choice == '3':
        cursor.execute("DELETE FROM Клиент WHERE Пластиковая_карта = 0")
    else:
        print("Неверный выбор.")
        return

    conn.commit()
    print(f"Удалено {cursor.rowcount} клиентов.")
    conn.close()

def edit_client():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    print("\nРедактирование клиента:")
    client_id = int(input("Введите код клиента для редактирования: "))

    cursor.execute("SELECT * FROM Клиент WHERE Код_клиента = ?", (client_id,))
    client = cursor.fetchone()
    if not client:
        print("Клиент не найден.")
        return

    print("\nТекущие данные клиента:")
    print(f"1. ФИО: {client[1]}")
    print(f"2. Периодический платеж: {client[2]}")
    print(f"3. Годовой процент: {client[3]}")
    print(f"4. Срок вклада: {client[4]} мес")
    print(f"5. Пластиковая карта: {'Да' if client[5] else 'Нет'}")

    field = input("Выберите поле для редактирования (1-5): ")
    if field == '1':
        new_value = input("Введите новое ФИО: ")
        cursor.execute("UPDATE Клиент SET ФИО = ? WHERE Код_клиента = ?", (new_value, client_id))
    elif field == '2':
        new_value = float(input("Введите новый периодический платеж: "))
        cursor.execute("UPDATE Клиент SET Периодический_платеж = ? WHERE Код_клиента = ?", (new_value, client_id))
    elif field == '3':
        new_value = float(input("Введите новый годовой процент: "))
        cursor.execute("UPDATE Клиент SET Годовой_процент = ? WHERE Код_клиента = ?", (new_value, client_id))
    elif field == '4':
        new_value = int(input("Введите новый срок вклада (мес): "))
        cursor.execute("UPDATE Клиент SET Срок_вклада = ? WHERE Код_клиента = ?", (new_value, client_id))
    elif field == '5':
        new_value = input("Есть пластиковая карта? (да/нет): ").lower() == 'да'
        cursor.execute("UPDATE Клиент SET Пластиковая_карта = ? WHERE Код_клиента = ?", (new_value, client_id))
    else:
        print("Неверный выбор.")
        return

    conn.commit()
    print("Данные клиента успешно обновлены.")
    conn.close()

init_db()

while True:
    print("\nБАНК - Управление клиентами")
    print("1. Добавить клиента")
    print("2. Просмотреть всех клиентов")
    print("3. Поиск клиентов")
    print("4. Удалить клиента")
    print("5. Редактировать клиента")
    print("6. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_client()
    elif choice == '2':
        view_clients()
    elif choice == '3':
        search_clients()
    elif choice == '4':
        delete_client()
    elif choice == '5':
        edit_client()
    elif choice == '6':
        break
    else:
        print("Неверный ввод, попробуйте снова.")