import sqlite3
import db as repo

conn = sqlite3.connect("my.db")
i = 1
while i == 1:
    print("""\nВыбирете задачу:
1. Внесение данных.
2. Посмотреть данные.
3. Посмотреть весь список.
4. Информация для оплаты.
5. Справка.
6. Выход.""")
    a = int(input())
    if a == 1:
        entities = (str(input("Введите месяц: ")), int(input("Введите t1: ")), int(input("Введите t2: ")))
        repo.start(conn, entities)
        print("Данные внесены.")
    elif a == 2:
        query = (str(input("Введите месяц: ")))
        repo.read_insert(conn, query)
    elif a == 3:
        repo.read_all(conn)
    elif a == 4:
        query = (str(input("Введите этот месяц : ")))
        query1 = (str(input("Введите прошлый месяц : ")))
        repo.sum(conn, query, query1)
    elif a == 5:
        print("""Эта программа для расчета комуналки в съемных квартирах.
По схеме: (плата за месяц + электроэнергия + вода).
Расчет подходит для счетчиков по типу: День, Ночь.
Create by MR_Monnte.""")
    elif a == 6:
        print("Спосибо за выбор этой программы)")
        i = 0
        break