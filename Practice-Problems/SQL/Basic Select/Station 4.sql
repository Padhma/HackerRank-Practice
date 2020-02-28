declare @cc int
declare @dcc int

set @cc = (select count(city) from station)

set @dcc = (select count(distinct(city)) from station)

select @cc - @dcc                              