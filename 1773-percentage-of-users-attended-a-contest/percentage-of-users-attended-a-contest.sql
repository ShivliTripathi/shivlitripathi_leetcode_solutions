-- Write your PostgreSQL query statement below
select contest_id, 
round((100.00*count(*))/(select count(distinct user_id) from Users),2) as percentage
from Register 
group by contest_id
order by percentage desc,contest_id