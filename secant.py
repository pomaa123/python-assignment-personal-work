def func(x):
    return 3*x**2 + 2*x - 1
    



def secant_method(x_0, x_1, func, tol):
    f_of_x_0 = func(x_0)
    f_of_x_1 = func(x_1)
    x_2 = x_1 - (f_of_x_1*(x_1 - x_0) / (f_of_x_1 - f_of_x_0))
    ##print(x_2)
    while x_2 > tol:
        x_0 = x_1
        x_1 = x_2
        f_of_x_0 = func(x_0)
        f_of_x_1 = func(x_1)
        x_2 = x_1 - (f_of_x_1*(x_1 - x_0) / (f_of_x_1 - f_of_x_0))
        
        if x_1== x_2:
            break
        
        print(x_2)
    return x_2

secant_method(0, 1, func, 0.01)


