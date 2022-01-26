class Rectangle:
 def _init_(self,length,width):
  self._length=length
  self._width=width
 def area(self):
  return self._length*slef._width
 def _It_(self,other):
  return self.area()>other.area()
 l1=int(input("enter he length of the first rectangle:"))
 w1=int(input("enter the width of the firstrectanle:")) 
 rectangle1=(l1,w1)
 l2=int(input("enter he length of the second rectangle:"))
 w2=int(input("enter the width of the second rectanle:")) 
 rectangle2=(l2,w2)
 if rectangle1 < rectangle2:
  print("area of rectangle 1 is smaller")
 else:
  print("area of rectanle 2 is smaller")
