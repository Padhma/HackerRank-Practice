declare @var int
select @var = 0
while @var < 21
begin
print replicate('* ', @var)
set @var = @var + 1
end