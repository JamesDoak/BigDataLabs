class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def toString(self):
        return "(" + str(self.x) + " , " + str(self.y) + ")"

pt = Point(1,2)
print(pt.toString())
pt.move(10,10)
print(pt.toString())