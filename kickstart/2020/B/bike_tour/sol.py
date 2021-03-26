# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

T = int(input())
for i in range(1, T+1):
    N = int(input())
    H = [int(x) for x in input().split()]

    count = 0
    for j in range(1, N-1):
        if H[j] > H[j-1] and H[j] > H[j+1]:
            count += 1

    print("Case #{}: {}".format(i, count))