# for i in range(5,0,-1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# lista = [10,20,30,40,50]
# lista.sort(reverse=True)
# for i in lista:
#     print(i)

# for i in range(-10,0):
#     print(i)

# start = 25
# end = 50
# prost = True
# for i in range(start,end+1):
#     for j in range(2,i):
#         if i % j == 0:
#             prost = False
#     if prost:
#         print(i)
#     prost = True

broj = int(input("unesite broj: "))
factorijal = 1
for i in range(1,broj+1):
    factorijal *= i
print(factorijal)
