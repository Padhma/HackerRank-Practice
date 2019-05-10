select ceiling(avg(Salary)-avg(replace(Salary,'0','')))
from employees
