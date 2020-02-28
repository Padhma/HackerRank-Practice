DECLARE @i int=2;
declare @prime int = 0;
DECLARE @result nvarchar(1000) = '';
WHILE (@i<=1000)
begin
   DECLARE @j int = @i-1;
   SET @prime = 1;
   WHILE(@j > 1)
   begin
      IF @i % @j = 0
      begin 
         SET @PRIME = 0;
      end
    set @j = @j - 1;
   end
   
   IF @PRIME = 1
   BEGIN
      set @result += cast(@i as nvarchar(1000)) + '&';
   END
set @i = @i + 1;
end
set @result = SUBSTRING(@result, 1, LEN(@result) - 1)
select @result

