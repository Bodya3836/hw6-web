import psycopg2

# Параметри підключення до бази даних
conn_params = {
    'host': 'localhost',
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '8748'

}

# Підключення до бази даних
conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        student_id SERIAL PRIMARY KEY,
        student_name VARCHAR(255) NOT NULL
    );


    CREATE TABLE IF NOT EXISTS Groups (
        group_id SERIAL PRIMARY KEY,
        group_name VARCHAR(50) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Teachers (
        teacher_id SERIAL PRIMARY KEY,
        teacher_name VARCHAR(255) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Subjects (
        subject_id SERIAL PRIMARY KEY,
        subject_name VARCHAR(255) NOT NULL,
        teacher_id INT
    );

    CREATE TABLE IF NOT EXISTS Grades (
        grade_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES Students(student_id),
        subject_id INT REFERENCES Subjects(subject_id),
        grade INT,
        date_received DATE
    );
''')

# Збереження змін
conn.commit()

# Додавання зовнішніх ключів
cursor.execute('''
    ALTER TABLE Subjects
    ADD CONSTRAINT fk_teacher_id
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id);
''')

cursor.execute('''
    ALTER TABLE Grades
    ADD CONSTRAINT fk_student_id
    FOREIGN KEY (student_id) REFERENCES Students(student_id);
''')

cursor.execute('''
    ALTER TABLE Grades
    ADD CONSTRAINT fk_subject_id
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id);
''')

# Збереження змін та закриття підключення
conn.commit()
conn.close()
