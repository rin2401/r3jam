# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()
    
import numpy as np

T = int(input())
for i in range(T):
    S = input().strip()
    C = []
    cb = 0
    for c in S:
        if len(C) == 0:            
            v = int(c)
            C.append("(" * v)
            cb += v
        elif c > C[-1]:
            v = int(c) - int(C[-1]) 
            C.append("(" * v)
            cb += v
        elif c < C[-1]:
            v = int(C[-1]) - int(c)
            C.append(")" * v)
            cb -= v
        C.append(c)
        
    C.append(")" * cb)

            
    print("Case #{}: {} ".format(i+1, "".join(C)))