from functools import lru_cache
import time
import math
import cProfile, pstats

total = 0
n = 1
@lru_cache(10)
def calc_pi2o6(val):
    global total
    global n
    while n < val:
        
        total += 1/(n*n)
        n += 1
        print(total)
        if (n < val):
            print(n)
            calc_pi2o6(n)
        else:
            fileo = open("result.txt", "w+")
            fileo.write(str(get_pi(total)))

            return total

def get_pi(res):

    return math.sqrt(res*6)

# calc_pi2o6(999999)
#1.6449330668467699

with cProfile.Profile() as pr:
    
    inp = input("please enter the number of iterations, more iterations mean better accuracy, but more time to execute: ")

    assert inp.isdigit(), "Please enter a digit!"

    pisquo6 = calc_pi2o6(int(inp))



stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()
print(f"PI: ~{get_pi(pisquo6)}")