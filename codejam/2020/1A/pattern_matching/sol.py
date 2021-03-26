# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b3034
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

def solve(a):
    a = [x.split("*") for x in a]
    b = sorted([x[0] for x in a], key=lambda x: len(x), reverse=True)
    e = sorted([x[-1] for x in a], key=lambda x: len(x), reverse=True)
    
    n = max([len(x) for x in a])
    
    for x in b[1:]:
        if len(x) !=0 and b[0][:len(x)] != x:
            return "*"
    for x in e[1:]:
        if len(x) !=0 and e[0][-len(x):] != x:
            return "*"
    mid = ""
    for x in a:
        mid += "".join(x[1:-1])
        
    return b[0] + mid + e[0]

T = int(input())
for i in range(1, T+1):
    N = int(input())
    a = [input().strip() for _ in range(N)]
    print("Case #{}: {}".format(i, solve(a)))