SELECT project_id, ROUND(sum/count, 2) AS average_years
FROM (
SELECT p.project_id, SUM(e.experience_years) AS sum, COUNT(p.project_id) AS count
FROM Project p
LEFT JOIN Employee e 
ON e.employee_id = p.employee_id
GROUP BY project_id) AS result
