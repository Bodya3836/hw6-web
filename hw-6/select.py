import os
import psycopg2
import pathlib

# Отримання абсолютного шляху до теки скрипта
script_directory = os.path.dirname(os.path.abspath(__file__))

# Параметри підключення до бази даних
connection_params = {
        'host': 'localhost',
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '8748'
}

# Підключення до бази даних
conn = psycopg2.connect(**connection_params)
cursor = conn.cursor()

# Читання та виконання SQL-інструкцій з кожного файлу в теці скрипта
sql_files_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sql_files')
for filename in os.listdir(sql_files_folder):
    if filename.endswith(".sql"):
        filepath = os.path.join(sql_files_folder, filename)

        with open(filepath, 'r') as file:
            sql_queries = file.read()

# Збереження змін у базі даних
conn.commit()

# Закриття з'єднання та курсора
cursor.close()
conn.close()
