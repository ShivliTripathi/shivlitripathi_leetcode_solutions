# Write your MySQL query statement below
/* Write your PL/SQL query statement below */

select MAX(Salary) as SecondHighestSalary from Employee where Salary <(select max(Salary) from Employee)
