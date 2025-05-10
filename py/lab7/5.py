class shape:
    def perimeter(self):
     pass
    def area(self):
       pass
class rectangle(shape):
   def __init__(self,length,breadth):
      self.length=length
      self.breadth=breadth
   def perimeter(self):
      return 2*(self.length+self.breadth)
   def area(self):
      return self.length*self.breadth
class circle(shape):
   def __init__(self,rad):
      self.rad=rad
   def perimeter(self):
      return 2*3.14*self.rad
   def area(self):
      return 3.14*self.rad**2
while 1:
  c=int(input("enter 1 for rectangle \nenter 2 for circle \nenter 0 for exit:"))
  if c==1:
     l=float(input("enter the length:"))
     b=float(input("enter the breadth:"))
     r=rectangle(l,b)
     k=int(input("enter 1 for perimeter 2 for area:"))
     if k==1:
        print(r.perimeter())
     elif k==2:
        print(r.area())
  elif c==2:
     r=float(input("enter the radius:"))
     c=circle(r)
     k=int(input("enter 1 for perimeter 2 for area:"))
     if k==1:
        print(c.perimeter())
     elif k==2:
        print(c.area())
  elif c==0:
     break