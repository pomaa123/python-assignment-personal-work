def function(l):
    m = 4
    return ((-2.2067*10**-12)*(l**m - 81*10**8))

def euler(l_0,h):
    
    # t = [30, 60, 120, 240, 480]
    
    # while h_0 < 480:
    for j in range(0,480,h):
        f_0f_l = function(l_0)
        l_1 = l_0 + f_0f_l *h
        l_0 = l_1
    # print(l_1)
    return l_1
tetha = []    
a = euler(1200,30)
tetha.append(a)

b = euler(1200,60)
tetha.append(b)
c = euler(1200,120)
tetha.append(c)
d = euler(1200,240)
tetha.append(d)
e = euler(1200,480)
tetha.append(e)
print("temperature = ",tetha)