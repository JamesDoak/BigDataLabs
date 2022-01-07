import cpoint
import ccircle

pt = cpoint.Point(1, 2)
print(pt.toString())
pt.move(10, 10)
print(pt.toString())

circ = ccircle.Circle(pt,5)
print(circ.toString())
print(circ.area())
print(circ.radius)

circ.radius = 10
print(circ.toString())
print(circ.area())

# circ = classes.Circle(pt,5)
# print(circ.toString())