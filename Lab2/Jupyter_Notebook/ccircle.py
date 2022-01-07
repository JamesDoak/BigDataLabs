class Circle:
    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def toString(self):
        return "Centre at " + self.centre.toString() + ", radius=" + str(self.radius)