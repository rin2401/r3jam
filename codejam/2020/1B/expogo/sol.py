# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

import numpy as np
po = [2**i for i in range(31)]

def solve(x, y):
    n = abs(x)+abs(y)
    if n % 2 == 0:
        return "IMPOSSIBLE"
    path = ""
    for i in range(int(np.floor(np.log2(n))),-1, -1):
        if abs(x) >= abs(y):
            if x >=0:
                path = "E" + path
                x -= po[i]
            else:
                path = "W" + path
                x += po[i]   
        else:
            if y >=0:
                path = "N" + path
                y -= po[i]
            else:
                path = "S" + path
                y += po[i]
    return path

T = int(input())
for t in range(1, T+1):
    x, y = list(map(int, input().split()))
    print("Case #{}: {}".format(t, solve(x,y)))