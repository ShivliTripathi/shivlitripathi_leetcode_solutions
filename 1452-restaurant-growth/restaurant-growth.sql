-- Write your PostgreSQL query statement below
with cte as
(select visited_on, sum(amount) as amount
from Customer
group by visited_on
order by visited_on),

cte2 as
(select visited_on,
sum(amount) over(order by visited_on rows between 6 preceding and current row) as amount,
round(sum(amount) over(order by visited_on rows between 6 preceding and current row)/7,2) as average_amount
from cte
group by visited_on, amount)

select * from cte2 
offset 6