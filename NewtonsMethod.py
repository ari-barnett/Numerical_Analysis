from sympy import *

x = symbols('x')

def func():
    return (tan(x)-x) #Symbolic definition of the function Tan(x) = x


def NewtonsMethod(f,x0,M,TOL):
    i = 1;
    while abs(f.subs(x,x0)) > TOL and i<M: 
        
        y0 = f.subs(x,x0); #Function evaluation at xn
        yp = diff(f,x) #Derivative of the funcation
        x1 = x0 - y0/yp.subs(x,x0); # Newtons algorithm for xn1
        
        x0 = x1;
        i = i+1;
    
    return x0

a = NewtonsMethod(func(),4.5,2000,10**-12);
b = NewtonsMethod(func(),7.7,2000,10**-12);

print("The roots found are", a, "and", b)



