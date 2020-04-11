# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

po = [2**i for i in range(31)]

def solve(N):
    row = []
    for i in range(30,-1,-1):
        if po[i] + i <= N:
            row.append(i)
            N -= po[i]
        elif len(row):
            N -= 1
    S = 0
    rev = False
    for i in range(row[0]+N+1):
        if i in row:
            S += po[i]
            if rev:
                for j in range(i+1):
                    print(i+1, j+1)
            else:
                for j in range(i,-1,-1):
                    print(i+1, j+1)
            rev = not rev
        else:
            S += 1
            if rev:                
                print(i+1, 1)
            else:
                print(i+1, i+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print("Case #{}:".format(t))
    solve(N)