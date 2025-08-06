-- Write your PostgreSQL query statement below
with cte as (select d.name as Department, e.name as Employee, e.salary as Salary,
dense_rank() over(partition by e.departmentId order by e.salary desc) as drnk
from 
Department d join Employee e on e.departmentId = d.id)

select Department, Employee, Salary from cte where drnk<=3