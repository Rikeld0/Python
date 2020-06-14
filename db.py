import sqlite3
from  sqlite3 import Error
             
def create_conn():
  conn = None
  try:
    conn = sqlite3.connect("my.db")
  except Error as e:
    print(f"The error '{e}' occured")
  return conn

def create_table(conn):
  c = conn.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS мосэнерго_2020(
    id text PRIMARY KEY,
    t1 integer,
    t2 integer)""")
  conn.commit()

def add_insert(conn, entities):   
  c = conn.cursor()
  c.execute("INSERT INTO мосэнерго_2020(id, t1, t2) VALUES(?, ?, ?)", entities)
  conn.commit()

def read_insert(conn, query):
  c = conn.cursor()
  result = None
  try:
    c.execute("SELECT t1, t2 FROM мосэнерго_2020 WHERE id = ? ", [query])
    result = c.fetchone()
    print(result[0], result[1])
  except Error as e:
    print(f"The error '{e}' occurred")

def read_all(conn):
  c = conn.cursor()
  try:
    c.execute("SELECT * FROM мосэнерго_2020")
    rows = c.fetchall()
    for row in rows:
        print(row[0], row[1], row[2])
  except Error as e:
    print(f"The error '{e}' occurred")

def sum(conn, query, query1):
  i = 1
  while i == 1:
    print("""
    Выбирете опцию:
    1. Расход электроэнергии за месяц. 
    2. Счет за электроэнергию.
    3. Весь счет.
    4. Назад.""")
    q = int(input())
    if q == 1:
      t1, t2 = 5.35, 1.50
      c = conn.cursor()
      c.execute("SELECT t1, t2 FROM мосэнерго_2020 WHERE id = ? ", [query])
      r1 = c.fetchone()
      c.execute("SELECT t1, t2 FROM мосэнерго_2020 WHERE id = ? ", [query1])
      r2 = c.fetchone()
      print("T1:", (r1[0] - r2[0]), "\nT2:", (r1[1] - r2[1]))
    elif q == 2:
      t1, t2 = 5.35, 1.50
      c = conn.cursor()
      c.execute("SELECT t1, t2 FROM мосэнерго_2020 WHERE id = ? ", [query])
      r1 = c.fetchone()
      c.execute("SELECT t1, t2 FROM мосэнерго_2020 WHERE id = ? ", [query1])
      r2 = c.fetchone()
      f = float(((r1[0] - r2[0]) * t1) + ((r1[1] - r2[1]) * t2))
      print("\nСумма к оплате: ", f)
    elif q == 3:
      t1, t2 = 5.35, 1.50
      c = conn.cursor()
      c.execute("SELECT t1, t2 FROM мосэнерго_2020 WHERE id = ? ", [query])
      r1 = c.fetchone()
      c.execute("SELECT t1, t2 FROM мосэнерго_2020 WHERE id = ? ", [query1])
      r2 = c.fetchone()
      f = float(((r1[0] - r2[0]) * t1) + ((r1[1] - r2[1]) * t2))
      a = float(input('Введите Х/В: '))
      b = float(input("Введите Г/В: "))
      c = float(input("Введите Водоотвод: "))
      d = int(input("Укажите оплату замесяц: "))
      summ = int(a + b + c + d + f)
      print ("\nСумма к оплате: ", summ)
    elif q == 4:
      i = 0
      break

def start(conn, entities):
  conn = create_conn()
  create_table(conn)
  add_insert(conn, entities)
  conn.close()