import math
class vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def magnitude(self):
         print((self.x**2+self.y**2)**0.5)
    def angle(self):
         print(math.atan(self.y/self.x))
    def distance(self):
         a,b=map(int,input("enter the 2nd vector x and y coordinate:").split())
         print(((self.x-a)**2+(self.y-b)**2)**0.5)
    def dotproduct(self):
         a,b=map(int,input("enter the 2nd vector x and y coordinate:").split())
         print(self.x*a+self.y*b)
    def vectorproduct(self):
         a,b=map(int,input("enter the 2nd vector x and y coordinate:").split())
         print(self.x*b-self.y*a)
class vector3d(vector2d):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def magnitude(self):
         print((self.x**2+self.y**2+self.z**2)**0.5)
    def angle(self):
         print(math.atan((self.z**2+self.y**2)**0.5/self.x))
    def distance(self):
         a,b,c=map(int,input("enter the 2nd vector x and y and z coordinate:").split())
         print(((self.x-a)**2+(self.y-b)**2+(self.z-c))**0.5)
    def dotproduct(self):
         a,b,c=map(int,input("enter the 2nd vector x and y and z coordinate:").split())
         print(self.x*a+self.y*b+self.z*c)
    def vectorproduct(self):
         a,b,c=map(int,input("enter the 2nd vector x and y and z coordinate:").split())
         print(f"{self.y*c-self.z*b}i+{self.z*a-self.x*c}j+{self.x*b-self.y*a}k")
while(1):
 c=int(input("enter 1 for 2d vector and 2 for 3d vector:"))
 if c==1:
   x,y=map(int,input("enter the vector coordinate x and y:").split()) 
   a=vector2d(x,y) 
 else:
   x,y,z=map(int,input("enter the vector coordinate x and y and z coordinate:").split())
   a=vector3d(x,y,z)
 while(1):
   b=int(input("enter 1 for magnitude\n enter 2 for angle\n enter 3 for distance\n enter 4 for dot product\n enter 5 for cross product\n enter 6 to go for next vector\n enter 7 to exit :"))
   match b:
     case 1:
          a.magnitude()
     case 2:
          a.angle()
     case 3:
          a.distance()
     case 4:
          a.dotproduct()
     case 5:
          a.vectorproduct()
     case 6:
          break
     case 7:
          break
          break
     