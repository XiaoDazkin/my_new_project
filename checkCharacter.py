sen = input("Enter a Sentence: ")
n = input("Enter a Character: ")
total = 0

for c in sen:
    if c == n:
        total += 1

print(f"Total number character {n} in this sentence = {total}")