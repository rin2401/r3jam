def solve(text):
    hand = None
    count = 0
    for s in text:
        if s != "F" and hand != s:
            hand = s
            count += 1
    
    if count > 0:
        count -= 1 

    return count

test_path = "weak_typing_chapter_1"

with open(f"{test_path}_input.txt", encoding="utf-8") as f:
    texts = [l.strip() for l in f][2::2]
    
with open(f"{test_path}_output.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(texts):
        print(f"Case #{i+1}:", solve(text))
        f.write(f"Case #{i+1}: {solve(text)}\n")