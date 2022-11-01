# broj = 7
# if broj > 10:
#     print("broj je veci od 10")
# else:
#     print("broj je manji od 10")

# broj = int(input("unesite broj: "))
# if broj > 0:
#     print("pozitivan")
# else:
# print("negativan")

# broj = int(input("unesite neki broj: "))
# if broj % 2 == 0:
#     print("broj je deljiv sa dva")
# else:
# print("broj nije deljiv sa dva")

# broj = int(input("unesi broj od 1-12: "))
# if broj == 1:
#     print("januar")
# elif broj == 2:
#     print("februar")
# elif broj == 3:
#     print("mart")
# elif broj == 4:
#     print("april")
# elif broj == 5:
#     print("maj")
# elif broj == 6:
#     print("jun")
# elif broj == 7:
#     print("jul")
# elif broj == 8:
#     print("avgust")
# elif broj == 9:
#     print("septembar")
# elif broj == 10:
#     print("oktobar")
# elif broj == 11:
#     print("novembar")
# elif broj == 12:
#     print("decembar")

# broj1 = float(input("unesite prvi broj: "))
# broj2 = float(input("unesite prvi broj: "))
# operacija = input("unesite neku operaciju: ")
# 
# if broj2 > broj1:
#     broj1, broj2 = broj2, broj1
# 
# if operacija == "+":
#     print(broj1+broj2)
# elif operacija == "-":
#     print(broj1-broj2)
# elif operacija == "*":
#     print(broj1*broj2)
# elif operacija == "/":
#     print(broj1/broj2)
# else:
#     print("niste uneli validnan znak")

# x>65 100
# x<8 besplatno
# 18>x>8 200
# 65>x>19 500

godine = int(input("koliko imate godina? "))

if godine<8:
    print("besplatan ulaz")
elif godine>7 and godine<19:
    print("cena karte je 200 dinara")
elif godine>65:
    print("cena karte je 100 dinara")
else:
    print("cena karte je 500 dinara")
