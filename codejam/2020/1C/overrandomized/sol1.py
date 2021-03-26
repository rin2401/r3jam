# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

import numpy as np

T = int(input())
for t in range(1, T+1):
    U = int(input())
    Q = []
    R = []
    for _ in range(10**4):
        q, r = input().split()

        Q.append(q)
        R.append(r)

    M = {}

    if int(Q[0]) != -1:
        for q, r in zip(Q,R):
            if len(q) == len(r):                
                for i, (cq, cr) in enumerate(zip(q,r)):
                    if cr not in M:
                        M[cr] = cq
                    elif cq < M[cr]:
                        M[cr] = cq

                    if i==0 and int(cq) ==1:
                        continue
                    elif i > 0 and int(cq) ==0:
                        continue
                    else:
                        break


    for c, i in sorted(M.items(), key=lambda x: x[1]):
        C += c

    print("Case #{}: {}".format(t, C))