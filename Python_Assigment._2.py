## bisection method
'''
with bisection the intial points are a, b and c
c is the mean of a and b which draws you closer to the point
f(c) is used to determine which of the points is changing 
'''

def f(x):
    return 3*x**2 + 2*x - 1



def bisection_method(initial_a, initial_b, f, tol):
    c = (initial_a + initial_b)/2
    f_of_c = f(c)
    while c > tol:
        if f_of_c > 0:
            initial_b = c
            c = (initial_a + initial_b)/2
            f_of_c = f(c)

        elif f_of_c < 0:
            initial_a = c
            c = (initial_a + initial_b)/2
            f_of_c = f(c)
        print(c)

        if initial_b - initial_a < 0.0001:
            break
    return c
    


# findind the roots of the function with newton raphson's method
def diff_func(x):
    return (6*x + 2)
    
def newton_raphson(x, f, diff_func,tol):
    f_of_x = f(x)
    f_prime_x = diff_func(x)
    x_1 = x - f_of_x/f_prime_x
    print(x_1)
    while x > tol:
        x = x_1
        f_of_x = f(x)
        f_prime_x = diff_func(x)
        x_1 = x - f_of_x/f_prime_x

        if x == x_1:
            break
        print(x)    



# finding the roots of the equation with secant method

def secant_method(x_0, x_1, f, tol):
    f_of_x_0 = f(x_0)
    f_of_x_1 = f(x_1)
    x_2 = x_1 - (f_of_x_1*(x_1 - x_0) / (f_of_x_1 - f_of_x_0))
    ##print(x_2)
    while x_2 > tol:
        x_0 = x_1
        x_1 = x_2
        f_of_x_0 = f(x_0)
        f_of_x_1 = f(x_1)
        x_2 = x_1 - (f_of_x_1*(x_1 - x_0) / (f_of_x_1 - f_of_x_0))
        
        if x_1== x_2:
            break
        
        print(x_2)
    return x_2

bisection_method(0, 1, f, 0.01)

newton_raphson(1, f, diff_func,0.0001)

secant_method(0, 1, f, 0.0001)





