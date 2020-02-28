-- shortest city name
select top 1 city, len(city)
from station
order by len(city), city asc

--longest city name
select top 1 city, len(city)
from station
order by len(city) desc