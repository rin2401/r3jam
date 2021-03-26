# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

T = int(input())
for t in range(1, T+1):
    X, Y , M = input().split()
    X = int(X)
    Y = int(Y)
    
    # print(X,Y,M)
    r = "IMPOSSIBLE"

    for i, s in enumerate(M):
        if s == "W":
            X -= 1
        elif s == "E":
            X += 1
        elif s == "N":
            Y+= 1
        elif s == "S":
            Y-= 1
        
        if abs(X)+abs(Y) <= i+1:
            r = i+1
            break

    print("Case #{}: {}".format(t, r))