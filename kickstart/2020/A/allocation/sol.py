# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

n = int(input())
for c in range(n):
    t, b = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a = sorted(a)
    s = 0
    r = 0
    for i in a:
        s += i
        if s <= b:
            r += 1
        else: 
        	break
        
    print("Case #{}: {}".format(c+1, r))