select months*salary as earning,count(*) 
from employee
group by earning
order by earning desc limit 1
