# Homework 1 Question 4
# CSCI 4448
# Ryan Murphy

from random import randint

#Generic shape class defines a Shape at x,y,z.
class Shape:
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def draw(self):
        print("Shape drawn at coordinates {},{},{}".format(self.x,self.y,self.z))
    
    def __str__(self):
        return "Shape".ljust(15,' ')+"#"+" {},{},{}".format(self.x,self.y,self.z).rjust(17)

#Defines a circle at x,y,z with radius length radius.
class Circle(Shape):
    
    def __init__(self,x,y,z,radius):
        Shape.__init__(self,x,y,z)
        self.radius=radius

    def draw(self):
        print("Circle with radius of {} drawn at coordinates {},{},{}".format(self.radius,self.x,self.y,self.z))
    
    def __str__(self):
        return "Circle".ljust(15,' ')+"#"+" {},{},{}".format(self.x,self.y,self.z).rjust(17)

#Defines an equilateral triangle at x,y,z with legs length leg.
class Triangle(Shape):
    
    def __init__(self,x,y,z,leg):
        Shape.__init__(self,x,y,z)
        self.leg=leg

    def draw(self):
        print("Triangle with legs length {} drawn at coordinates {},{},{}".format(self.leg,self.x,self.y,self.z))

    def __str__(self):
        return "Triangle".ljust(15,' ')+"#"+" {},{},{}".format(self.x,self.y,self.z).rjust(17)

#Defines a regular square at x,y,z with side length side.
class Square(Shape):
    
    def __init__(self,x,y,z,side):
        Shape.__init__(self,x,y,z)
        self.side=side

    def draw(self):
        print("Square with sides length {} drawn at coordinates {},{},{}".format(self.side,self.x,self.y,self.z))

    def __str__(self):
        return "Square".ljust(15,' ')+"#"+" {},{},{}".format(self.x,self.y,self.z).rjust(17)

#A class that generates a random collection of squares circles and triangles with random coordinates and sizes and can draw and sort them.
class ShapeDriver:

    def __init__(self):
        self.list=[]
        self.numCircles=randint(4,10)
        self.numSquares=randint(4,10)
        self.numTriangles=randint(4,10)
    
    #Generate a random number of shapes
    def generateShapes(self):
        
        #Generate some random circles
        for i in range(0,self.numCircles):
            x=randint(-50,50)
            y=randint(-50,50)
            z=randint(-50,50)
            r=randint(1,10)
            self.list.append(Circle(x,y,z,r))
        
        #Generate some random triangles
        for i in range(0,self.numTriangles):
            x=randint(-50,50)
            y=randint(-50,50)
            z=randint(-50,50)
            leg=randint(1,10)
            self.list.append(Triangle(x,y,z,leg))
        
        #Generate some random squares
        for i in range(0,self.numSquares):
            x=randint(-50,50)
            y=randint(-50,50)
            z=randint(-50,50)
            side=randint(1,10)
            self.list.append(Square(x,y,z,side))

    #Sort the shapes by the Z axis
    def sortShapesByZ(self):
        self.list.sort(key=lambda x: x.z,reverse=True)

    #Print the draw statements for each shape
    def drawShapes(self):
        for shape in self.list:
            shape.draw()

    #Print the list of shapes as a table
    def printShapeTable(self):
        temp = "Shape Table".center(33,' ')+"\n"
        temp += "Shape Type".ljust(15,' ')+"#"+" Coordinates".rjust(17)+"\n"
        temp += "#"*33+"\n"
        for shape in self.list:
            temp+=str(shape)+"\n"
        print(temp)

    def getNumShapes(self):
        return len(self.list)

#Main
driver=ShapeDriver()
driver.generateShapes()

print("There are {} shapes.\n".format(driver.getNumShapes()))
print("Drawing Shapes:\n")

driver.sortShapesByZ()
driver.drawShapes()

print("\n"+
    "Below is a table for convenience since repeated print sentences are hard to look at.\n")

driver.printShapeTable()

print("\n"+
    "Notes:\n"+
    "1. I assumed that positive-z was into the screen and negative-z was out of the screen.\n"+
    "   Hence shapes at higher z values are behind shapes at lower z values.\n"+
    "2. The program generates a random number of random shapes each time it is run.\n")

