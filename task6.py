a, b, c = int(input()), int(input()), int(input())

discriminant = b**2 - 4 * a * c


x1 = int(-b - discriminant**0.5 / (2 * a))
x2 = int(-b + discriminant**0.5 // (2 * a))

if x1 == x2:
    print(x1)
else:
    print(x1)
    print(x2)
