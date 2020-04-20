# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b63
# rin2401
# python interactive_runner.py python testing_tool.py 1 -- python sol.py

import sys
import numpy as np

T, A, B = [int(i) for i in input().split()]
print(T, A, B, file=sys.stderr)

nq = 0 
def query(x,y):
    global nq
    nq += 1
    print(x,y)
    sys.stdout.flush()
    r = input()
    return r

def define_circle(p1, p2, p3):
    """
    Returns the center and radius of the circle passing the given 3 points.
    In case the 3 points form a line, returns (None, infinity).
    """
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

    if abs(det) < 1.0e-6:
        return (None, np.inf)

    # Center of circle
    cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det

    radius = np.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
    return ((cx, cy), radius)

def findx(ox,oy, x): 
    while True:
        i = (ox + x)//2
        r = query(i, oy)
        if r == "HIT":
            ox = i
        elif r == "MISS":
            x = i

        if abs(x-ox) <= 1:
            return (ox, oy)

def findy(ox,oy, y): 
    while True:
        i = (oy + y)//2
        r = query(ox, i)
        if r == "HIT":
            oy = i
        elif r == "MISS":
            y = i

        if abs(y-oy) <= 1:
            return (ox, oy)

def solve():    
    for x in [-10**9//3, 10**9//3]:
        for y in [-10**9//3, 10**9//3]:
            if query(x,y) == "HIT": #always hit R >= W/2
                ox, oy = x, y
                break

    A = findx(ox,oy,10**9)
    B = findx(ox,oy,-10**9)
    C = findy(ox,oy,10**9)
    (x, y), R = define_circle(A, B ,C)
    x, y = round(x), round(y)
    
    for i in range(-2,3):
        for j in range(-2,3):
            if query(x+i, y+j) == "CENTER":
                return

for t in range(T):
    solve()

sys.exit()


