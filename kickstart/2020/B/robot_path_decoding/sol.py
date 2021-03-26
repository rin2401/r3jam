#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

T = int(input())
for t in range(1, T+1):
    M = input()
    R = 10 ** 9
    X = [1]
    C = 1
    w, h = 0, 0

    for c in M:
        if c.isnumeric():
            x = int(c)
            X.append(x)
            C *= x
        if c == ")":
        	x = X.pop(-1)
        	C //= x 
        if c == "N":
            h -= C
        if c == "S":
            h += C
        if c == "E":
            w += C
        if c == "W":
            w -= C

    print("Case #{}: {} {}".format(t, w % R + 1, h % R + 1))