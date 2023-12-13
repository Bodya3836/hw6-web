SELECT
    S.student_name,
    G.group_name
FROM
    Students S
JOIN
    Groups G ON S.student_id = S.student_id
WHERE
    G.group_id = 55;







