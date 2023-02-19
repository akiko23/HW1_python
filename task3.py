n = int(input())
price_for_1, price_for_10, price_for_60 = 15, 125, 440

tickets1, tickets10, tickets60 = 0, 0, 0

# вычисление единиц в числе количества поездок
ed = n - (n // 10 * 10)

# в этом промежутке самый выгодный билет будет на 60 поездок
if 60 >= n > 34:
    tickets60 += 1

# промежуток от 60 до бесконечности, также самый выгодный билет на 60 поездок
elif n > 60:
    tickets60 += n // 60
    
    # формируем оставшиеся десятки, вычитая те поездки, которые мы приобрели с билетами на 60 поездок
    des = n // 10 - n // 60 * 6
    
    # проверяем, выгоднее ли в оставшихся поездках приобрести билеты на 10 или 1 билет на 60 поездок
    if des * 10 + ed <= 34:
        tickets10 += des

        # проверка на выгодность 1 билета на 10 поездок или некольких на 1
        if ed > 8:
            tickets10 += 1
        else:
            tickets1 += ed
    else:
        tickets60 += 1

# промежуток между 1 и 43, самый выгодный вариант - билеты на 10 поездок
else:
    tickets10 += n // 10

    # проверка на выгодность 1 билета на 10 поездок или некольких на 1 поездку
    if ed > 8:
        tickets10 += 1
    else:
        tickets1 += ed

print(tickets1, tickets10, tickets60)

