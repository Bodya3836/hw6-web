SELECT DISTINCT
    S.student_name,
    Su.subject_name
FROM
    Students S
JOIN
    Groups Gr ON S.student_id = S.student_id
JOIN
    Subjects Su ON Gr.group_id = Gr.group_id;













