k, m, n = int(input()), int(input()), int(input())
time_for_one_podhod = m*2

if n*2 % k == 0:
    podhodi = n*2 // k
    res = m * podhodi


elif n <= k:
    res = time_for_one_podhod

else:
    podhodi = n*2 // k
    res = m*(1 + (podhodi))

print(res)

