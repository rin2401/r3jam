# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b64
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

R = None
S = None

def find(A):
    steps = []

    if len(A)-R > 1:
        for b in range(len(A)-1, 1, -1):
            if A[b-1][0]==A[0][0]:
                break
        for a in range(b-1, 0, -1):
            if A[a-1][0] == A[b][0]:
                break
    else:
        a = 1
        b = len(A) - 1

    sa = sum([x[1] for x in A[:a]])
    sb = sum([x[1] for x in A[a:b]])

    if len(A)-R > 1:
        A[b] = (A[b][0], A[b][1] + A[a-1][1])
        A[b-1] = (A[b-1][0], A[b-1][1] + A[0][1])
    else:
        A[b] = (A[b][0], A[b][1] + A[a-1][1])

    A = A[a:b] + A[1:a-1] + A[b:]

    return A, (sa, sb)

def count(A):
    c = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            c+=1
    return c

def solve(R, S):
    steps = []
    A = [(i,1) for i in range(1,R+1)] * S
    for i in range((R*S-R+1)//2):
        A, s = find(A)
        steps.append(s)

    return steps

T = int(input())
for t in range(1, T+1):
    R, S = list(map(int, input().split()))

    ss = solve(R,S)

    print("Case #{}: {}".format(t, len(ss)))
    for a, b in ss:
        print(a, b)