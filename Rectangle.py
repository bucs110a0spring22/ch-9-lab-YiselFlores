class Rectangle:
  def __init__(self, x, y, height, width):
    self.x =max(0,x) 
    self.y = max(0,y)
    self.height = max(0,height)
    self.width = max(0,width)
    
    
    
  def __str__(self):
   return f'Rectangle({self.x},{self.y},{self.height},{self.width})'
    