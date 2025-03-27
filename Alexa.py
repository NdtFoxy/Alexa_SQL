import pymssql
from tabulate import tabulate
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

server = "mssql-2017.labs.wmi.amu.edu.pl"
user = "dbad_s498793"
password = "bWyQrhMOc3"
database = "dbad_s498793"

try:
    conn = pymssql.connect(
        server, user, password, database,
        charset='cp1250' 
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Pracownicy")
    rows = cursor.fetchall()

    if cursor.description:
        column_names = [col[0] for col in cursor.description]
        print(tabulate(rows, headers=column_names, tablefmt="grid"))
    else:
        print("Таблица пуста.")

    conn.close()

except Exception as e:
    print(f"Ошибка: {e}")