class circle:
    def __init__(self, radius=1.0,color="red"):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius = radius
    
    def getColor(self):
        return self.color
    
    def setColor(self,color) :
        self.color = color
    
    def toString(self):
        return f"radius : {self.getRadius()} , color : {self.getColor()}"
    
    def getArea(self):
        return 3.14 * (self.getRadius()**2)

class cylinder(circle):
    def __init__(self, radius=1.0, color="red", height=1.0):
        super().__init__(radius, color)
        self.height = height

    def getHeight(self):
        return self.height
    
    def setHeight(self,height):
        self.height = height
    
    def toString(self):
        return f"radius : {self.getRadius()} , color : {self.getColor()} , height = {self.getHeight()}, area = {self.getArea()} , volume = {self.getVolume()}"
    
    def getVolume(self):
        return self.getArea() * self.getHeight()


# print(circle().getArea())
print(cylinder().toString())

