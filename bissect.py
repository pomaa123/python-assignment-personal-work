# writing our function
def f(x):
    return 3*x**2 + 2*x - 1


 #writing out the f(a) and f(b)
#funct_a = f(iter_a)
#funct_b = f(iter_b)
#funct_c = f(iter_c)

#print(funct_a)
#print(funct_b)
#print(funct_c)
'''
finding the next a or b.
If f(a)*f(c) > 0, c replaces a
If f(a)*f(c) < 0, c repalces b
If f(a)*f(c) = 0, c is the root
'''



def bisect(f, iter_a, iter_b, tol):
    funct_a = f(iter_a)
    funct_b = f(iter_b)
    iter_c = (iter_a+iter_b)/2
    funct_c = f(iter_c)

    while iter_c > tol:
        if f(iter_a)*f(iter_c) < 0:
            iter_b = iter_c
            iter_c = (iter_a+iter_b)/2
        elif f(iter_a)*f(iter_c) > 0:
            iter_a = iter_c
            iter_c = (iter_a+iter_b)/2

        print("c = ", iter_c)
    return iter_c


bisect(f, 0, 1, 0.01)