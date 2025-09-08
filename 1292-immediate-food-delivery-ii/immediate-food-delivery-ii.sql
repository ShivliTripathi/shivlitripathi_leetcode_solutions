-- Write your PostgreSQL query statement below
with cte as (select *,
rank() over (partition by customer_id order by order_date) as rn
from Delivery)

select round(100.00*count(customer_id)/(select count(distinct customer_id) from Delivery),2)
as immediate_percentage
from cte where rn=1 and order_date=customer_pref_delivery_date