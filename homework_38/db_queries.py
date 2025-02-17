from db_connection import DBConnector


class QueryHandler(DBConnector):
    def __init__(self, dbconfig):
        super().__init__(dbconfig)

    def get_all_roles(self):
        cursor = self.get_cursor()
        cursor.execute(
            """
            SELECT *
            FROM Role
            """
        )
        record = cursor.fetchall()
        return record

    def get_role_id_by_name(self, name_role: str):
        cursor = self.get_cursor()
        cursor.execute(
            """
            SELECT id
            FROM Role
            WHERE name = %s
            """,
            (name_role,)
        )
        record = cursor.fetchone()
        if record:
            return record
        return None

    def work_with_tables(self, table_name):
        cursor = self.get_cursor()
        all_tables = ["Role", "User", "News", "Comment"]
        if table_name in all_tables:
            cursor.execute("DESCRIBE %s" % table_name)
            all_fields = [row["Field"] for row in cursor.fetchall()]
            print(f"Список полей таблицы {table_name}:\n" + "\n".join(all_fields))
        else:
            raise ValueError("Такой таблицы нет в списке.")

        field_name = input("Выберите поле, из имеющихся в таблице: ")
        if field_name in all_fields:
            operator = input("Выберите оператор сравнения (>, <, =): ")
        else:
            raise ValueError("Поле с таким названием отсутствует.")

        operators = [">", "<", "="]
        if operator in operators:
            value = input("Введите значение для сравнения: ")
        else:
            raise ValueError("Такого оператора нет в списке.")

        cursor.execute(
            f"""
                SELECT * 
                FROM {table_name}
                WHERE {field_name}
                {operator} %s
                """,
            (value,)
        )
        result = cursor.fetchall()
        print("Полученный результат: ")
        for row in result:
            print(row)

