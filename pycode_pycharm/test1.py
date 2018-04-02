w=None
print(w)
def fun(x,y):
    global w
    w=x*y
    z=x+y
    return z


ttt=fun(1,1)
print(ttt)
print('w=',w)
