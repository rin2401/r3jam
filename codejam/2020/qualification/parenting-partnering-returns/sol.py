# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()
    
import numpy as np

def is_overlap(a, b):
    if a[0] < b[1] and a[1] > b[0]:
        return True
    return False

def is_overlap_list(SE, l):
    for x in l:
        if is_overlap(SE, x):
            return False
    return True

T = int(input())
for i in range(T):
    N = int(input())
    W = []
    C = []
    J = []
    R = ""
    W = []
    for j in range(N):
        W.append([int(n) for n in input().split()])
    for SE in sorted(W, key=lambda x: x[0]):
        if is_overlap_list(SE, C):
            C.append(SE)
        elif is_overlap_list(SE, J):
            J.append(SE)
        else:
            R = "IMPOSSIBLE"
            break
    if R == "":
        for SE in W:
            if SE in C:
                R += "C"
                C.remove(SE)
            else:
                R += "J"
                J.remove(SE)
                
    print("Case #{}: {} ".format(i+1, R))