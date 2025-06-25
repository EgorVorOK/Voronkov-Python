import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Форма регистрации")

tk.Label(window, text="Ваше имя:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Пароль:").pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Label(window, text="Возраст:").pack()
age_entry = tk.Entry(window)
age_entry.pack()

tk.Label(window, text="Пол:").pack()
gender = tk.StringVar(value="Мужской")
tk.Radiobutton(window, text="Мужской", variable=gender, value="Мужской").pack()
tk.Radiobutton(window, text="Женский", variable=gender, value="Женский").pack()

tk.Label(window, text="Ваши увлечения:").pack()
hobby1 = tk.IntVar()
tk.Checkbutton(window, text="Музыка", variable=hobby1).pack()
hobby2 = tk.IntVar()
tk.Checkbutton(window, text="Видео", variable=hobby2).pack()
hobby3 = tk.IntVar()
tk.Checkbutton(window, text="Рисование", variable=hobby3).pack()

def clear_all():
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender.set("Мужской")
    hobby1.set(0)
    hobby2.set(0)
    hobby3.set(0)

def submit():
    messagebox.showinfo("Успех", "Регистрация завершена!")
    print("Имя:", name_entry.get())
    print("Пароль:", password_entry.get())
    print("Возраст:", age_entry.get())
    print("Пол:", gender.get())
    print("Увлечения:", "Музыка" if hobby1.get() else "",
                     "Видео" if hobby2.get() else "",
                     "Рисование" if hobby3.get() else "")

tk.Button(window, text="Отменить", command=clear_all).pack()
tk.Button(window, text="Подтвердить", command=submit).pack()

window.mainloop()