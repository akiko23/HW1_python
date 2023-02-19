a, b = int(input()), int(input())

# проверка на бесконечное количество решений
if a == 0 and b == 0:
    print("INF")

# проверка через выражение, представленного в условии задачи
elif a * int(-b / a) + b != 0:
    print("NO")
else:
    print(int(-b / a))
