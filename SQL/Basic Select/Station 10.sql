select distinct city
from station
where city not like '%[aeiou]'