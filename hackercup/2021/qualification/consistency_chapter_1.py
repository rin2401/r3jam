from collections import Counter
def solve(text):
    V = []
    C = []
    for t, c in Counter(text).most_common():
        if t in "AEIOU":
            V.append((t, c))
        else:
            C.append((t, c))
    
    sC = sum([x[1] for x in C])
    sV = sum([x[1] for x in V])
    
    ssC = sC
    if ssC:
        ssC -= C[0][1]
    ssV = sV
    if ssV:
        ssV -= V[0][1]
        
    return min(ssV * 2 + sC, ssC * 2 + sV)

test_path = "consistency_chapter_1"

with open(f"{test_path}_input.txt", encoding="utf-8") as f:
    texts = [l.strip() for l in f][1:]
    
with open(f"{test_path}_output.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(texts):
        f.write(f"Case #{i+1}: {solve(text)}\n")