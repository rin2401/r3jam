# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

import numpy as np

T = int(input())
for i in range(T):
    N = int(input())
    M = np.zeros((N,N), dtype="int")
    trace = 0
    for j in range(N):
        M[j] = [int(m) for m in input().split()]
        trace += M[j,j]

    r = 0
    c = 0
    for k in range(N):
        for j in range(1, N+1):
            if j not in M[k]:
                r += 1
                break
                
    for k in range(N):
        for j in range(1, N+1):
            if j not in M[:, k]:
                c += 1
                break
                
    print("Case #{}: {} {} {}".format(i+1, trace, r, c))