import time
import math
total = 0
n = 1
def calc_pi2o6(val):
    global total
    global n
    while n < val:
        
        total += 1/(n**2)
        n += 1
        print(total)
        if (n < val):
            calc_pi2o6(n)
        else:
            fileo = open("result.txt", "w+")
            fileo.write(str(total))

            break

def get_pi(res):

    return math.sqrt(res*6)

# calc_pi2o6(999999)
#1.6449330668467699

print(str(get_pi(calc_pi2o6(1000000000))))
