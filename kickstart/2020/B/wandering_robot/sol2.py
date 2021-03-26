# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

import numpy as np

N = 2*100000
po = np.zeros(N+1)
for i in range(1, N+1):
    po[i] = po[i-1] + np.log2(i)


def prob(x,y):
    x, y = x-1, y-1
    return 2**(po[x+y] - po[x] - po[y] - x - y)

T = int(input())
for t in range(1, T+1):
    W, H, L, U, R, D = list(map(int, input().split()))

    S = 1
    for y in range(U, D+1):
        if y == H:
            S -= prob(L-1,y)
        else:
            S -= prob(L-1,y)/2
    for x in range(L, R+1):    
        if x == W:
            S -= prob(x, U-1)
        else:
            S -= prob(x, U-1)/2
    if D==H:
        for x in range(1,L-1):
            S -= prob(x,H) / 2
    if R==W:
        for y in range(1,U-1):
            S -= prob(W,y) / 2

    print("Case #{}: {}".format(t, S))

    S = 0.0
    if D < H:
        for x in range(1,L):
            if L+D-x <= H:
                S+= prob(x, L+D-x)
            else:
                S+= prob(x, H) / 2
    if R < W:
        for y in range(1, U):
            if U+R-y <= W:
                S += prob(U+R-y, y)
            else:
                S += prob(W, y)/2
        
    print("Case #{}: {}".format(t, S))
