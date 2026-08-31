# размер таблицы в DataFrame
import psycopg2 as psycopg
import pandas as pd
import os

connection = {"sslmode": "require", "target_session_attrs": "read-write"}
postgres_credentials = {
    "host": os.getenv ("DB_DESTINATION_HOST"), 
    "port": os.getenv ("DB_DESTINATION_PORT"),
    "dbname": os.getenv ("DB_DESTINATION_NAME"),
    "user": os.getenv ("DB_DESTINATION_USER"),
    "password": os.getenv ("DB_DESTINATION_PASSWORD"),
}
assert all([var_value != "" for var_value in list(postgres_credentials.values())])

connection.update(postgres_credentials)

# определяем название таблицы, в которой хранятся наши данные
TABLE_NAME = "users_churn"


# эта конструкция создаёт контекстное управление для соединения с базой данных 
# оператор with гарантирует, что соединение будет корректно закрыто после выполнения всех операций с базой данных
# причём закрыто оно будет даже в случае ошибки при работе с базой данных
# это нужно, чтобы не допустить так называемую "утечку памяти"
with psycopg.connect(**connection) as conn:

# создаём объект курсора для выполнения запросов к базе данных 
# с помощью метода execute() выполняется SQL-запрос для выборки данных из таблицы TABLE_NAME
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {TABLE_NAME}")
				
				# извлекаем все строки, полученные в результате выполнения запроса
        data = cur.fetchall()

				# получаем список имён столбцов из объекта курсора
        columns = [col[0] for col in cur.description]

# создаём объект DataFrame из полученных данных и имён столбцов 
# это позволяет удобно работать с данными в Python с использованием библиотеки Pandas
df = pd.DataFrame(data, columns=columns)

print(f"Размер нашей таблицы: {df.shape[0]} строк; {df.shape[1]} столбцов")