import math
def f(t):
    return 2000 * math.log(140000/(140000-2100*t)) - 9.8*t

def trapezium_rule(lower_limit,upper_limit,n):
    a = lower_limit
    h = (upper_limit - a)/n
    
#range from the lower to the upper limit
    t = []
    t.append(a)
    for i in range(0, n):
        a = a + h
        t.append(a)
    print(t)
#loop over your t to calculate f(t)
    f_of_t = []
    for i in t:
        b = f(i)
        f_of_t.append(b)
    print(f_of_t)
    f_0 = f_of_t[0]
    fol = f_of_t[1:-1]
    f_n = f_of_t[-1]
    # printing y0 ,y1+....yn-1, yn
    print(fol)
    print(f_0)
    print (f_n)
    

     #calculation of the middle numbers y1 + y2 + ...+yn-1
    total = 0
    for elements in fol:
        total += elements

    print(total)
   
    trap =  (f_0 + 2*total +f_n) * h/2
    print("answer = ",trap)
    


trapezium_rule(8, 30, 1)