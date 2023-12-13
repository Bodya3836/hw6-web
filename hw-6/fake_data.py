import random
from faker import Faker
import psycopg2

def create_connection():
    conn_params = {
        'host': 'localhost',
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '8748'
    }

    return psycopg2.connect(**conn_params)

def generate_fake_data(conn, num_students=50, num_groups=3, num_subjects=8, num_teachers=5, max_grades_per_student=20):
    fake = Faker()
    cursor = conn.cursor()

    # Додавання викладачів
    teacher_ids = []
    for _ in range(num_teachers):
        cursor.execute("INSERT INTO Teachers (teacher_name) VALUES (%s) RETURNING teacher_id;", (fake.name(),))
        teacher_ids.append(cursor.fetchone()[0])

    # Додавання студентів
    student_ids = []  # Ініціалізація списку student_ids
    for _ in range(num_students):
        cursor.execute("INSERT INTO Students (student_name) VALUES (%s) RETURNING student_id;", (fake.name(),))
        student_id = cursor.fetchone()[0]
        student_ids.append(student_id)  # Додати student_id до списку

    # Додавання груп
    for group_name in ['Group A', 'Group B', 'Group C'][:num_groups]:
        cursor.execute("INSERT INTO Groups (group_name) VALUES (%s) RETURNING group_id;", (group_name,))
        group_id = cursor.fetchone()[0]

    # Додавання предметів
    subjects = [fake.word() for _ in range(num_subjects)]
    subject_ids = []

    for subject in subjects:
        teacher_id = random.choice(teacher_ids)
        cursor.execute("INSERT INTO Subjects (subject_name, teacher_id) VALUES (%s, %s) RETURNING subject_id;",
                       (subject, teacher_id))
        subject_id = cursor.fetchone()[0]
        subject_ids.append(subject_id)

    # # Додавання студентів до груп
    # cursor.execute("SELECT student_id FROM Students;")
    # student_ids = [row[0] for row in cursor.fetchall()]
    #
    # for student_id in student_ids:
    #     cursor.execute("INSERT INTO Groups (student_id, group_id) VALUES (%s, %s);", (student_id, random.randint(1, num_groups)))

    # Додавання оцінок
    for student_id in student_ids:
        for subject_id in subject_ids:
            num_grades = random.randint(1, max_grades_per_student)
            for _ in range(num_grades):
                grade = random.randint(60, 100)
                cursor.execute("INSERT INTO Grades (student_id, subject_id, grade) VALUES (%s, %s, %s);",
                               (student_id, subject_id, grade))

    conn.commit()
    cursor.close()

if __name__ == "__main__":
    connection = create_connection()
    generate_fake_data(connection)
    connection.close()

