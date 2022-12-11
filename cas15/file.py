# i = 1
# while i < 11:
#     print(i)
#     i += 1

# lista = []
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# broj = int(input("unesite broj: "))
# suma = 0
# proizvod = 1
# for i in range(1, broj + 1):
#     suma += i
#     proizvod *= i
# print(suma)
# print(proizvod)

# broj = int(input("unesite broj: "))
# for i in range(1,11):
#     print(i * broj)

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

broj = 12435
suma = 0
# print(len(str(broj)))
for i in str(broj):
    suma += int(i)
print(suma)
