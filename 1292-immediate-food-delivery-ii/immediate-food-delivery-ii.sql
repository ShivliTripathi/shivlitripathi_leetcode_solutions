-- Write your PostgreSQL query statement below
with cte as 
(select *,
dense_rank() over(partition by customer_id order by order_date) as rnk
from Delivery)

select round(100.00*count(distinct c1.customer_id)/(select count(*) from cte where rnk=1),2) 
as immediate_percentage
from cte c1 join cte c2 
on c1.delivery_id=c2.delivery_id and c1.customer_id=c2.customer_id
and c1.order_date=c2.customer_pref_delivery_date
where c1.rnk=1