SELECT
    S.subject_name
FROM
    Subjects S
JOIN
    Teachers T ON S.teacher_id = T.teacher_id
WHERE
    T.teacher_name = 'Billy Gonzales';






