num = input()

edinitsi = ''
desatki, sotni = '', ''


if int(num) > 9:
    if int(num[0]) == 4:
        desatki = "XL"
    elif 9 > int(num[0]) >= 5:
        desatki = "L" + "X" * (int(num[0]) - 5)
    elif int(num[0]) == 9:
        desatki = "XM"
    elif int(num) == 100:
        desatki = "M"
    else:
        desatki = "X" * int(num[0])
if num[-1] == "4":
    edinitsi = "IV"
elif num[-1] == "5":
    edinitsi = "V"
elif num[-1] == "6":
    edinitsi = "VI"
elif num[-1] == "7":
    edinitsi = "VII"
elif num[-1] == "8":
    edinitsi = "VIII"
elif num[-1] == "9":
    edinitsi = "IX"
elif num[-1] == "1":
    edinitsi = "I"
elif num[-1] == "2":
    edinitsi = "II" 
elif num[-1] == "3":
    edinitsi = "III"

print(desatki + edinitsi)
