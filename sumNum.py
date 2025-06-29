n = int(input("Enter n : "))
total = 0
x = 1
output = ""

if n <= 0:
    print("The entered Value must be greater than Zero!")
else:
    while x <= n:
        total += x
        output += str(x)
        if x < n:
            output += " + "
        x += 1
    print(f"{output} = {total}")