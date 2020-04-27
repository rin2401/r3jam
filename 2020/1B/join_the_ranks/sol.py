# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b64
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

def solve(R, S):
    queue = []
    steps = []
    A = list(range(1,R+1)) * S
    E = [i for i in range(1, R+1) for _ in range(S)]
    for a in range(1, R*S+1):
        for b in range(a+1, R*S+1):
            s = (a, b-a)
            steps.append(s)
            queue.append((A, [s]))

    while queue:
        A, ss = queue.pop(0)
        a, b = ss[-1]
        A = A[a:a+b] + A[:a] + A[a+b:]
        
        c = 1
        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                c+=1

        if c == R and A == E:
            # print(E, ss)
            return ss            
        elif c > len(A) - 2*len(ss):
            continue
        elif c==len(A) - 2*len(ss):
            queue = []
            for s in steps:
                queue.append((A, ss+[s]))



T = int(input())
for t in range(1, T+1):
    R, S = list(map(int, input().split()))

    ss = solve(R,S)

    print("Case #{}: {}".format(t, len(ss)))
    for a, b in ss:
        print(a, b)