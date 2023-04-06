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
        
bisection_method(0, 1, f, 0.01)

