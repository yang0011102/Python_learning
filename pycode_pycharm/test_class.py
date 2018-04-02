#类
class Calculator:
    color='black'
    price=20
    def add(self,x,y):
        z=x+y
        print(z,self.color)
    def minus(self,x,y):
        z=x-y
        print(z)

cal=Calculator()
