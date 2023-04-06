# Trapezium Rule

import numpy as np

def f(t):
     return 2000 * np.log(140000/(140000-(2100 * t))) - 9.8*t

def trapezium_rule(lower_limit,upper_limit, n):
     h = (upper_limit - lower_limit)/ n
     
     t = [lower_limit]
     
     for i in range(1, n+1): # correction: added 1 to n so the upper limit is captured
          t.append(t[i - 1] + h)
     print(t)
     
     
     
     f_of_t = []
     for i in range(len(t)):
          f_of_t.append(f(t[i]))
     print(f_of_t) 
       
     trap = []
     for i in range(len(f_of_t)):
          if i == 0 or i == len(f_of_t) - 1:
               trap.append((1/2) * h * f_of_t[i])
          else:
               trap.append(h * f_of_t[i])
     print(trap)
     
     print("The area under the curve = ", sum(trap))
                    
trapezium_rule(lower_limit = 3, upper_limit = 30, n = 6) 