class Polygon():
    def __init__(self, shape ):
        self.shape = shape

    def circleArea(self):
        print("The name of this shape is:", self.shape)
        print("get area of circle")
        r = float(input("your radius is: "))
        area = 22/7*r*r
        print("Your area is:", area) 
  
    def triangleArea(self):
        print("The name of this shape is:", self.shape)
        print("get area of triangle")
        b = float(input(" Your base  is: "))
        h = float(input(" Your height is: "))
        area = 1/2*b*h
        print("Your area is:", area) 

    def squareArea(self):
        print("The name of this shape is:", self.shape)
        print("get area of square")
        s = float(input(" Your side  is: "))
   
        area = s**2
        print("Your area is:", area) 

    def rectangleArea(self):
        print("The name of this shape is:", self.shape)
        print("get area of rectangle")
        l = float(input(" Your length  is: "))
        b = float(input(" Your breadth  is: "))
        area = l*b
        print("Your area is:", area) 

    def parrallelogramArea(self):
        print("The name of this shape is:", self.shape)
        print("get area of parallelogram")
        b = float(input(" Your base  is: "))
        h = float(input(" Your height  is: "))
        area = b*h
        print("Your area is:", area) 
        
        
        

equation1 = Polygon("triangle")
equation1.triangleArea()
    

    