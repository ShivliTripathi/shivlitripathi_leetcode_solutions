# Write your MySQL query statement below
WITH df AS (
    SELECT 
        E.name AS Employee,
        D.name AS Department,
        E.salary AS Salary
    FROM Employee E
    JOIN Department D ON E.departmentId = D.id
),
df1 AS (
    SELECT 
        Employee,
        Department,
        Salary,
        DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS rnk
    FROM df
)
SELECT Department, Employee, Salary
FROM df1
WHERE rnk <= 3;
