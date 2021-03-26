# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

T = int(input())
for t in range(1, T+1):
    N, D = list(map(int, input().split()))
    A = list(map(int, input().split()))

    C = {}

    for a in sorted(A):
        if a not in C:
            C[a] = [(1,0)]
        else:
            C[a][0] = (C[a][0][0] + 1, 0)

        for k in C.keys():
            if a > k:
                if a % k == 0:
                    C[k].append((a//k, a//k-1))
                else:
                    C[k].append((a//k, a//k))

    for k in C.keys():
        C[k] = sorted(C[k], key=lambda x: x[1])


    # print(C)

    S = D-1
    for k, v in C.items():
        count = 0
        step = 0
        for c, s in v:
            count += c
            step += s
            if count >=D:
                news = s - (count-D)
                if count > D: news += 1
                if news < S:
                    S = news
                    # print(k, S)
                break

    print("Case #{}: {}".format(t, S))