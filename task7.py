# def choose_plural(num: int, plurs: list) -> str:
   # if num[-1] == "0" or 20 >= int(num[-2:]) >= 11 or num[-1] in [str(i) for i in range(5, 10)]:
   #     return f"{num} {plurs[2]}"
   # elif num[-1] == "1":
   #     return f"{num} {plurs[0]}"
   # else:
   #     return f"{num} {plurs[1]}"

#print(choose_plural(input(), ["korova", "korovy", "korov"]))
"""Мое старое решение c функцией под множество подобных примеров"""


# поулучаем количество коров в виде строки
num = input()

# проверяем, оканчивается ли последний элемент строки на 0 или он находится в промежутках от 11 до 20 и от 5 до 10 включительно
if num[-1] == "0" or 20 >= int(num[-2:]) >= 11 or 10 >= int(num[-1]) >= 5:
    print(num + " korov") 

# проверяем, оканчивается ли строка на 1
elif num[-1] == "1":
    print(num + " korova")

else:
    print(num + " korovy")
