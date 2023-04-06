'''
write an algorithm that uses the newton raphson's method to find the root of the equation 3x^2 +2x -1 
'''

def f(x):
    return (3*x**2 + 2*x - 1)

def f_prime(x):
    return (6*x + 2)



def newton_raphson(x, f, f_prime, tol):
    f_of_x = f(x)
    f_prime_x = f_prime(x)
    x1 = x - f_of_x/f_prime_x
    print(x1)
    while x > tol:
        x = x1
        f_of_x = f(x)
        f_prime_x = f_prime(x)
        x1 = x - f_of_x/f_prime_x

        if x1 == x:
            break
        print(x)
    

def secant_method(x0, x1, f, tol):
    f_of_x1 = f(x1)
    f_of_x0 = f(x0)
    x2 = x1 - (f_of_x1*(x1 - x0))/(f_of_x1 - f_of_x0)
    print(x2)
    while x1 > tol:
        x0 = x1
        x1 = x2
        f_of_x0 = f(x0)
        f_of_x1 = f(x1)
        x2 = x1 - (f_of_x1*(x1 - x0))/(f_of_x1 - f_of_x0)

        if x2 == x1:
            break
        print(x1)


def bisection_method(a, b, f, tol):
    c = (a + b)/2
    f_of_c = f(c)
    print (c)
    while c > tol:
        if f_of_c > 0:
            b = c
            c = (a + b)/2
            f_of_c = f(c)
        elif f_of_c < 0:
            a = c
            c = (a + b)/2
            f_of_c = f(c)
        
        if b - a < 0.000001:
            break

        print(c)
bisection_method(0, 1, f, 0.01)


newton_raphson(1, f, f_prime, 0.01)

secant_method(0, 1, f, 0.01)