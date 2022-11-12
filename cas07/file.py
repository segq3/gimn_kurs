# broj = float(input("unesite neki broj: "))
# if broj > 0:
#     print("broj je pozitivan")
# elif broj < 0:
#     print("broj je negativan")
# else:
#     print("broj je jednak nuli")

# string = "hello"
# if "hello" in string:
#     print(string)

# broj = int(input("unesite neki broj: "))
# if broj < 20:
#     print("broj je manji od 20")
#     if broj % 2 == 0:
#         print("broj je paran")
#     else:
#         print("broj je neparan")
# else:
#     print("broj je veci od 20")

# pitanje = input("zelite li da pomnozite brojeve?: ")
# if pitanje == "da":
#     broj1 = float(input("unesite prvi broj: "))
#     if broj1<=10:
#         print("broj je u rasponu od 10")
#         broj2 = float(input("unesite drugi broj: "))
#         if broj2<=10:
#             print("broj je u rasponu od 10")
#             print(broj1*broj2)
#         else:
#             print("broj nije u rasponu od 10")
#     else:
#         print("broj nije u rasponu od 10")
# else:
#     print("izlazak iz programa")

# a+b>c
# a+c>b
# b+c>a

a = float(input("unesite stranicu a: "))
b = float(input("unesite stranicu b: "))
c = float(input("unesite stranicu c: "))

if a+b>c and a+c>b and b+c>a:
    print("trougao postoji")
    if a == b and b == c:
        print("trougao je jednakostranican")
    elif a == b or b == c or a == c:
        print("trougao je jednakokrakan")
    else:
        print("trougao je raznostranican")
else:
    print("trougao ne postoji")
