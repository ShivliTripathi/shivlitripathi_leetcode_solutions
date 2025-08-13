-- Write your PostgreSQL query statement below
select distinct v1.author_id as id 
from Views v1 join Views v2
on v1.article_id=v2.article_id
where v1.author_id=v2.viewer_id