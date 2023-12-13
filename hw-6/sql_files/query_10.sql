select DISTINCT
    S.student_name,
    Su.subject_name,
    T.teacher_name
FROM
    Students S
JOIN
    Groups Gr ON S.student_id = S.student_id
JOIN
    Subjects Su ON Gr.group_id = Gr.group_id
JOIN
    Teachers T ON Su.teacher_id = T.teacher_id
WHERE
    S.student_id = 910
    AND T.teacher_id = 105;














