# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e
# rin2401
# python interactive_runner.py python local_testing_tool.py 1 -- python sol.py

import sys

T, B = [int(i) for i in input().split()]
numq = 0
bits = [None] * B

def query(index):
    global numq
    numq += 1
    print(index + 1)
    sys.stdout.flush()
    return int(input())

def flip(index):
    for i in range(index):
        bits[i] ^= 1
        bits[B-i-1] ^= 1

def swap(index):
    for i in range(index):
        bits[i], bits[B-i-1] = bits[B-i-1], bits[i]

def update(index):
    same = -1
    diff = -1
    for i in range(index):
        if bits[i] == bits[B-i-1]:
            same = i
        else:
            diff = i

    if same != -1 and diff == -1:
        if query(same) != bits[same]:
            flip(index)
        query(same)

    if same == -1 and diff != -1:
        if query(diff) != bits[diff]:
            swap(index)
        query(diff)

    if same != -1 and diff != -1:
        qs = query(same)
        qd = query(diff)
        if qs != bits[same] and qd == bits[diff]:
            swap(index)
            flip(index)
        if qs == bits[same] and qd != bits[diff]:
            swap(index)
        if qs != bits[same] and qd != bits[diff]:
            flip(index)


def solve():
    global numq, bits
    numq = 0
    bits = [None] * B

    for i in range(B//2):
        if numq and numq % 10 == 0:
            update(i)

        bits[i] = query(i)
        bits[B-i-1] = query(B-i-1)

    bstr = "".join([str(b) for b in bits])
    print(bstr)
    sys.stdout.flush()
    print(input().strip() , bstr, file=sys.stderr)

for _ in range(T):
    solve()

sys.exit()


