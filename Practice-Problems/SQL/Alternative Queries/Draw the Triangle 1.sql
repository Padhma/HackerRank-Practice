declare @var int
select @var = 20
while @var > 0
begin
print replicate('* ',@var)
set @var = @var - 1
end
