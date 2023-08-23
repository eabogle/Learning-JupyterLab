def pythagoras(a, b):
    return (a ** 2 + b ** 2) ** 0.5

for i in range(9):
    a = i
    b = i + 1
    print(f"a = {a}, b = {b}, c = {pythagoras(a, b)}")