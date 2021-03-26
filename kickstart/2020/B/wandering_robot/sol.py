# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
# rin2401
# python sol.py

f = open("test.txt")
def input():
    return f.readline()

ct = 0
cf = 0
W, H, L, U, R, D = [0]*6

def move(x,y,p):
    global ct
    global cf
    if x == W and y == H:
        ct += p
        return
    if x >= L and x <= R and y >= U and y <= D:
        cf += p
        return
    if y == H:
        move(x+1, y, p)
    elif x == W:
        move(x, y+1, p)
    else:
        move(x+1, y, p/2)
        move(x, y+1, p/2)

T = int(input())
for t in range(1, T+1):
    ct = 0
    cf = 0
    W, H, L, U, R, D = list(map(int, input().split()))
    move(1,1, 1)
    print("Case #{}: {}".format(t, ct))
