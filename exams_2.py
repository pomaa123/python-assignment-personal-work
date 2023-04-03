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
    print(l_1)

    
euler(1200,30)
euler(1200,60)
euler(1200,120)
euler(1200,240)
euler(1200,480)