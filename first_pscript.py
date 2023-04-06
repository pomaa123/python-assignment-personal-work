

print("hello world")
a = True
res = 0
while a:
    res += 1
    print("Value of res: ", res)
    if (res >= 10):
        a = False

def func(x):
    res = x + 1
    print(res)

#Assignment one
u = 10.2
a = 10.01
t = 4

v = u + a * t
print(v)

def func1(u, t):
    a = 10.01
    res1 = u + a * t
    print("The final velocity is: ", res1)
    return res1

var1 = func1(10.2, 4)
print("Answer: ", var1)