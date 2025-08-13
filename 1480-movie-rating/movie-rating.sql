-- Write your PostgreSQL query statement below
with cte as (select u.name as results
from Users u join MovieRating mr
on u.user_id=mr.user_id
group by u.name
order by count(mr.movie_id) desc, u.name limit 1),

cte2 as (select m.title as results
from Movies m join  MovieRating mr 
on m.movie_id=mr.movie_id
where created_at between '2020-02-01' and '2020-02-29'
group by m.title
order by avg(mr.rating) desc,m.title limit 1)

select * from cte
union all
select * from cte2