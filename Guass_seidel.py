##Gauss Seidel Method

# Defining equations to be solved
'''
    25x + 5y + z = 106.8
    64x - 8y + z = 177.2
    144x + 12y + z = 279.2
    '''

f1 = lambda x,y,z: (106.8 - 5*y - z) / 25
f2 = lambda x,y,z: -(177.2 - 64*x - z)/8
f3 = lambda x,y,z: (279.2 - 144*x + 12*y)

# Initial setup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
x0 = 0
y0 = 0
z0 = 0
count = 1

# Tolerance:
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)

    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))

    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    e3 = abs(z0-z1)
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))