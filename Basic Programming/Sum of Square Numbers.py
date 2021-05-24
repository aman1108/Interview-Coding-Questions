import math
def solve(c):
    high=int(math.sqrt(c))+1
    for i in range(high):
        val=c-(i*i)
        v=int(math.sqrt(val))
        if (v*v==val):
            return 1
    return 0
        
