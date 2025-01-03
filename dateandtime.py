#current date & time
import datetime
now = datetime.datetime.now()
print(now)


#current date
import datetime
current_date = datetime.date.today()
print(current_date)



#attribute of date & time
import datetime
print(dir(datetime))


#date object
import datetime
d = datetime.date(2025, 1, 3)
print(d)


#today's date
from datetime import date
todays_date = date.today()
print("Today's date =", todays_date)


#timestamp
from datetime import date
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)


#yy-mm-dd
from datetime import date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


#representation
from datetime import time
a = time()
print(a)

b = time(4, 12, 56)
print(b)

c = time(hour = 4, minute = 12, second = 56)
print(c)

d = time(4, 12, 56, 234566)
print(d)



#minute-second-microsec
from datetime import time
a = time()
print(a)

b = time(4, 36, 37)
print(b)

c = time(hour = 4, minute = 36, second = 47)
print(c)

d = time(4, 36, 47, 236784)
print(d)





#time delta
from datetime import datetime, date
t1 = date(year = 2024, month = 12, day = 31)
t2 = date(year = 2025, month = 1, day = 3)

t3 = t1 - t2

print("t3 =", t3)

t4 = datetime(year = 2024, month = 12, day = 31, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2015, month = 1, day = 3, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)
print("Type of t3 =", type(t3)) 
print("Type of t6 =", type(t6))  




#two diff. delta
from datetime import timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)



#in sec
from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())


