#类定义
class Calculator:
    def __init__(self,color,price,height=0.5,width=10):
        self.color=color
        self.price=price
        self.height=height
        self.width=width
        print('self.color:',self.color,
              'self.price:',self.price,
              'self.height',self.height,
              'self.width',self.width)
    def add(self,x,y):
        z=x+y
        print(z)
    def minus(self,x,y):
        z=x-y
        print(z)

