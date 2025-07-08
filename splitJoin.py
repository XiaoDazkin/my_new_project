sen = input("Enter a sentence: ")
new_sen = ""
for c in sen:
    if c == " ":
        new_sen += "-"
    else:
        new_sen += c
print(new_sen)