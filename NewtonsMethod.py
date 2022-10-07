from sympy import *

x = symbols('x')

def func():
    #return x**2 + x - 2;
    #return(x**8 - 36*x**7 + 546*x**6 - 4536*x**5 + 22449*x**4 - 67284*x**3 + 118124*x**2 - 109584*x + 40320)
    return (tan(x)-x)
    #return (x**-1 - 2)

def NewtonsMethod(f,x0,M,TOL):
    i = 1;
    while abs(f.subs(x,x0)) > TOL and i<M:
        
        y0 = f.subs(x,x0);
        yp = diff(f,x)
        x1 = x0 - y0/yp.subs(x,x0);
        
        x0 = x1;
        i = i+1;
    
    return x0

a = NewtonsMethod(func(),4.5,2000,10**-12);
b = NewtonsMethod(func(),7.7,2000,10**-12);

print("The roots found are", a, "and", b)



