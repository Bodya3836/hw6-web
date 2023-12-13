SELECT
    T.teacher_name,
    Su.subject_name,
    AVG(G.grade) AS average_grade
FROM
    Teachers T
JOIN
    Subjects Su ON T.teacher_id = Su.teacher_id
JOIN
    Grades G ON Su.subject_id = G.subject_id
GROUP BY
    T.teacher_name, Su.subject_name;










