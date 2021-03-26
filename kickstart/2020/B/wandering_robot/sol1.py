# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

import numpy as np

T = int(input())
for t in range(1, T+1):
    W, H, L, U, R, D = list(map(int, input().split()))
    M = np.zeros((W+1, H+1))
    for y in range(1, H+1):
        for x in range(1, W+1):
            if x == 1 and y == 1:
                M[x,y] = 1
            elif x >= L and x <= R and y >= U and y <= D:
                continue
            elif x == W and y == H:
                M[x,y] = M[x-1,y] +  M[x,y-1]
            elif x == W:
                M[x,y] = M[x-1,y]/2 +  M[x,y-1]
            elif y == H:
                M[x,y] = M[x-1,y] +  M[x,y-1]/2
            else:
                M[x,y] = M[x-1,y]/2 +  M[x,y-1]/2

    print("Case #{}: {}".format(t, M[W][H]))
    print(M.T)