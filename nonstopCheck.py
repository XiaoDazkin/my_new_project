sen = input("Enter a Sentence: ")

while True:
    n = input("Enter a Character (or 0 to quit): ")
    if n == '0':
        print("Stopping The Program.")
        break

    total = 0
    for c in sen:
        if c == n:
            total += 1

    print(f"Total number of character '{n}' in this sentence = {total}")
    print()