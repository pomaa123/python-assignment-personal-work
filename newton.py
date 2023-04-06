def func(x):
    return (3*x**2 + 2*x - 1)

def diff_func(x):
    return (6*x + 2)
    
def newton_raphson(x, func, diff_func,tol):
    f_of_x = func(x)
    f_prime_x = diff_func(x)
    x_1 = x - f_of_x/f_prime_x
    print(x_1)
    while x > tol:
        x = x_1
        f_of_x = func(x)
        f_prime_x = diff_func(x)
        x_1 = x - f_of_x/f_prime_x

        if x == x_1:
            break
        print(x)    

newton_raphson(1, func, diff_func,0.01)

    

