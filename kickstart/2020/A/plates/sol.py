# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

T = int(input())

for i in range(T):
    N, K, P = [int(i) for i in input().split()]
    stacks = [[int(i) for i in input().split()] for _ in range(N)]

    for n in range(N):
        for k in range(K):

    print("Case #{}: {}".format(i+1, stacks))