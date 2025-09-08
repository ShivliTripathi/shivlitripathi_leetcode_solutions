-- Write your PostgreSQL query statement below
select p.product_name, sum(o.unit) as unit
from Products p join Orders o 
on p.product_id=o.product_id
where to_char(o.order_date,'yyyy-mm')='2020-02'
group by p.product_name
having sum(o.unit)>=100