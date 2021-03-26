# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

T = int(input())
for t in range(1, T+1):
    N, D = list(map(int, input().split()))
    X =  list(map(int, input().split()))
    d = D
    for x in X[::-1]:
        d = d//x * x
        
    print("Case #{}: {}".format(t, d))