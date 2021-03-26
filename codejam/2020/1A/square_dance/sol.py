# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

import numpy as np

T = int(input())
for t in range(1, T+1):
    R, C = list(map(int, input().split()))
    S = []

    for _ in range(R):
        row = list(map(int, input().split()))
        S.append(row)
    
    S = np.array(S, dtype="int")
    D = np.ones((R, C), dtype="int")
    count = 0

    for _ in range(R*C):
        count += S.sum()
        E = S.astype("bool").astype("int")
        P = np.zeros((R, C))

        for i in range(R):
            for j in range(C):
                if D[i,j]:
                    e = 0
                    p = 0
                    for ii in range(i-1, -1, -1):
                        if S[ii, j]:
                            p += S[ii,j]
                            e += 1
                    for ii in range(i+1, R, 1):
                        if S[ii, j]:
                            p += S[ii,j]
                            e += 1
                    for jj in range(j-1, -1, -1):
                        if S[i, jj]:
                            p += S[i,jj]
                            e += 1
                    for jj in range(j+1, C, 1):
                        if S[i, jj]:
                            p += S[i, jj]
                            e += 1

                    if e:
                        # p = S[:,j].sum() + S[i,:].sum() - 2*S[i,j]
                        P[i,j] = p / e
                        if P[i,j] > S[i,j]:
                            D[i,j] = 0

        print("S\n", S)
        print("P\n", P)
        print("S*D\n", S*D)

        if (S == S * D).all():
            break
        else:
            S = S * D                

    print("Case #{}: {}".format(t, count))