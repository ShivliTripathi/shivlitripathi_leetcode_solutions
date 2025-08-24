-- Write your PostgreSQL query statement below
select name from Employee where id in
(select e1.id from 
Employee e1 join Employee e2
on e1.id = e2.managerId
group by e1.id
having count(e1.id)>=5)