#==============================
# Task 6-1: the square function
#==============================
def square(value):
  return value * value

print(square(5.0))


#==============================
# Task 6-2: the distance function
#==============================
# import the math module
import math

def distance(x1, y1, x2, y2):
  return math.sqrt(square(x2-x1) + square(y2-y1))

print(distance(0,0,1,1))


#==============================
# Task 6-3: the maximum function
#==============================
numbers = [4,7,3,2,6]

def maximum(list):
  result = 0
  for i in list:
    if i > result:
      result = i
  return result

print(maximum(numbers))
