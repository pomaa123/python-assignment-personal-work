u = 10.2
a = 10.01
t = 4

v = u + a*t
print(v)


# A function where u and t are the arguments.
def velocity(u,t):
    a = 10.01
    v = u + a*t
    return v

velocity(10.2,4)