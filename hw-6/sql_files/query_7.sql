SELECT
    S.student_name,
    Gr.group_name,
    Su.subject_name,
    G.grade
FROM
    Students S
JOIN
    Groups Gr ON S.student_id = S.student_id
JOIN
    Grades G ON S.student_id = G.student_id
JOIN
    Subjects Su ON G.subject_id = Su.subject_id
WHERE
    Gr.group_id = 56
    AND G.subject_id = 75;









