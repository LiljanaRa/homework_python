import pymysql
from pymysql.cursors import DictCursor
from db_queries import QueryHandler


dbconfig = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'database': '160924_social_blogs',
    'charset': 'utf8mb4',
    'cursorclass': DictCursor
}

def main(dbconfig, action: str, **params):
    query_handler = QueryHandler(dbconfig)
    dict_actions = {
        "get_all_roles": query_handler.get_all_roles,
        "get_role_id_by_name": query_handler.get_role_id_by_name,
        "work_with_tables": query_handler.work_with_tables
    }

    try:
        key = ( action.lower())
        if dict_actions.get(key):
            result = dict_actions.get(key)(**params)
            return result
        return "Действия не существует!"
    except pymysql.Error as e:
        print("SQLError", e)
    except Exception as e:
        print("Error", e)


res_w_w_t = main(dbconfig, "work_with_tables", table_name ="News" )
#res_w_w_t1 = main(dbconfig, "work_with_tables1", table_name ="Role" )

# res_all_roles = main(dbconfig, "get_all_roles")
# res_id_roles = main(dbconfig, "get_role_id_by_name", name_role="admin")
# res_id_roles1 = main(dbconfig, "get_role_id_by_name1", name_role="admin")

# print(res_all_roles)
# print(res_id_roles)
# print(res_id_roles1)
# print(res_w_w_t1)