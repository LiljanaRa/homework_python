import pymysql
from pymysql.cursors import DictCursor


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

def table_users(manager):
    manager.execute(
        """
        SELECT *
        FROM Users
        """
    )
    users_info = cursor.fetchall()
    return users_info

def table_products(manager):
    manager.execute(
        """
        SELECT *
        FROM Products
        """
    )
    products_info = cursor.fetchall()
    return products_info

def table_sales(manager):
    manager.execute(
        """
        SELECT *
        FROM Sales
        """
    )
    sales_info = cursor.fetchall()
    return sales_info


table_name = {
    "Users": table_users,
    "Products": table_products,
    "Sales": table_sales
}

user_input = input("Введите название таблицы: ").strip().capitalize()

data = table_name.get(user_input)

if not data:
    print("Некорректный ввод.")
else:
    print(data(cursor))

cursor.close()
connector.close()