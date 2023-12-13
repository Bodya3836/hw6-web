SELECT
    G.student_id,
    AVG(G.grade) AS average_grade,
    S.subject_name
FROM
    Grades G
JOIN
    Subjects S ON G.subject_id = S.subject_id
WHERE
    S.subject_id = 71
GROUP BY
    G.student_id, S.subject_name
ORDER BY
    average_grade DESC
LIMIT 1;


