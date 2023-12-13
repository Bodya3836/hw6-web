SELECT
    Gr.group_id,
    S.subject_name,
    AVG(G.grade) AS average_grade
FROM
    Grades G
JOIN
    Groups Gr ON G.student_id = G.student_id
JOIN
    Subjects S ON G.subject_id = S.subject_id
WHERE
    G.subject_id = 72
GROUP BY
    Gr.group_id, S.subject_name
ORDER BY
    average_grade DESC;




