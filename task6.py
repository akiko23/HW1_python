a, b, c = int(input()), int(input()), int(input())

# вычисление дискриминанта
discriminant = b**2 - 4 * a * c

# проверка на отрицательный дискриминант
if discriminant < 0:
    print("Нет решений")

else:
    # вычисление 1 и 2 корней по известным всем формулам
    x1 = int(-b - discriminant**0.5 / (2 * a))
    x2 = int(-b + discriminant**0.5 // (2 * a))

    # проверка на совпадение корней
    if x1 == x2:
        print(x1)
    else:
        print(x1)
        print(x2)
