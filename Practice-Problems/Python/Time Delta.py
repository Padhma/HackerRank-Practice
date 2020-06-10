
from datetime import datetime, date

for _ in range(int(input())):
    time1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs((time1 - time2).total_seconds())))