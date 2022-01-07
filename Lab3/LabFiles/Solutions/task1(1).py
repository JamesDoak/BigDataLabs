import calendar
# Sets the weekday (0 is Monday, 6 is Sunday) to start each week.
# The values MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY,
# and SUNDAY are provided for convenience.
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())
year = 2020
print(calendar.isleap(year))


import math
n=5
print(math.factorial(n))
x=-1
print(math.exp(x))


################################
# Define an alias to library
################################
import math as m
n2=5
print(m.factorial(n2))
x2=-1
print(m.exp(x2))


################################
# Import the entire name space
################################
from math import *
n3=5
print(factorial(n3))
x3=-1
print(exp(x3))