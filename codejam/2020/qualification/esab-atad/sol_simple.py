# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e
# rin2401
# python interactive_runner.py python local_testing_tool.py 1 -- python sol_simple.py

import sys
import numpy as np

def swap(a, b):
    n = len(a)
    for i in range(n//2):
        if a[i] != 2 and a[n-i-1] != 2 and b[i] != 2 and b[n-i-1] == 2:
            b[n-i-1] = a[i] ^ a[n-i-1] ^ b[i]
        if a[i] != 2 and a[n-i-1] != 2 and b[i] == 2 and b[n-i-1] != 2:
            b[i] = a[i] ^ a[n-i-1] ^ b[n-i-1]   
        if a[i] == 2 and a[n-i-1] != 2 and b[i] != 2 and b[n-i-1] != 2:
            a[i] = a[n-i-1] ^ b[i] ^ b[n-i-1]
        if a[i] != 2 and a[n-i-1] == 2 and b[i] != 2 and b[n-i-1] != 2:
            a[n-i-1] = a[i] ^ b[i] ^ b[n-i-1]
    return a, b
        
T, B = [int(i) for i in input().split()]

if B == 10:
    for i in range(T):
        bstr = ""
        for j in range(1, B + 1):
            print(j)
            sys.stdout.flush()
            bstr += input().strip()
        
        print(bstr)
        sys.stdout.flush()

        print(input().strip(), bstr, file=sys.stderr)


if B == 20:
    for _ in range(T):
        S = np.ones((3, B), dtype="int") * 2

        for j in list(range(1, 6)) + list(range(16, 21)):
            print(j)
            sys.stdout.flush()
            S[0][j-1] = input().strip()

        for j in range(6, 16):
            print(j)
            sys.stdout.flush()
            S[1][j-1] = input().strip()

        for j in range(1, 11):
            print(j)
            sys.stdout.flush()
            S[2][j-1] = input().strip()
    
        S[2], S[0] = swap(S[2], S[0])
        S[2], S[1] = swap(S[2], S[1])

        bstr = "".join([str(i) for i in S[2]])
        print(bstr)
        sys.stdout.flush()

        print(input().strip(), bstr, file=sys.stderr)

if B == 100:
    pass
        
sys.exit()