# unos = input("> ")
# slova = 0
# brojevi = 0
# for i in unos:
#     if i in ["0","1","2","3","4","5","6","7","8","9"]:
#         brojevi += 1
#     else:
#         slova += 1
# 
# print("slova:",slova)
# print("brojevi:", brojevi)

# h = int(input("visina: "))
# w = int(input("sirina: "))
# ans = []
# temp = []
# 
# for i in range(h):
#     for j in range(w):
#         temp.append(j * i)
#     ans.append(temp)
#     temp = []
# 
# print(ans)

for i in range(50):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
