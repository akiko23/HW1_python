x, y, x2, y2 = int(input()), int(input()), int(input()), int(input())
coord1, coord2 = 4, 4

# определяем четверть первой точки
if x > 0 and y > 0:
    coord1 = 1
elif x < 0 and y < 0:
    coord1 = 3
elif x < 0 and y > 0:
    coord1 = 2


# определяем четверть второй точки
if x2 > 0 and y2 > 0:
    coord2 = 1
elif x2 < 0 and y2 < 0:
    coord2 = 3
elif x2 < 0 and y2 > 0:
    coord2 = 2

# проверяем, одинаковые ли у них четверти и выводим результат в консоль
if coord1 == coord2:
    print("YES")
else:
    print("NO")
