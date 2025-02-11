import pymysql
from pymysql.cursors import DictCursor
import pprint

dbconfig = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'database': 'ich_edit',
    'charset': 'utf8mb4',
    'cursorclass': DictCursor
}

connector = pymysql.connect(**dbconfig)
cursor = connector.cursor()

def users_names(manager):
    manager.execute(
        """
        SELECT name
        FROM Users
        """
    )
    us_names = cursor.fetchall()
    return us_names

def users_products(manager):
    manager.execute(
        """
        SELECT prod
        FROM Products as p 
        JOIN Sales as s 
        ON p.pid = s.pid
        JOIN Users as u 
        ON u.id = s.id
        WHERE name = %s
        """,
        (user_input,)
    )
    us_prod = cursor.fetchall()
    if not us_prod:
        print("У этого пользователя пока нет покупок.")
    return us_prod

pprint.pprint(users_names(cursor))

user_input = input("Выберите имя из предложенных, чтобы увидеть все покупки этого пользователя: ").strip().capitalize()

pprint.pprint(users_products(cursor))

cursor.close()
connector.close()