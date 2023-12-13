SELECT
    student_id,
    AVG(grade) AS average_grade
FROM
    Grades
GROUP BY
    student_id
ORDER BY
    average_grade DESC
LIMIT 5;
