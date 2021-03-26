# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

T = int(input())
for t in range(1, T+1):
    U = int(input())
    C = {}
    R = []
    for _ in range(10**4):
        q, r = input().split()
        R.append(r)
        if r[0] not in C:
            C[r[0]] = 1
        else:
            C[r[0]] += 1

    char = set("".join(R))
    for c in char:
        if c not in C:
            C[c]=0

    C = sorted(C.items(), key=lambda x: x[1], reverse=True)
    # print(C)
    R = ""
    for c, _ in C:
        R += c
    R = R[-1] + R[:-1]

    print("Case #{}: {}".format(t, R))