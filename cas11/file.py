# broj_ucenika = int(input("unesite broj ucenika: "))
# prirodan_broj = int(input("unesite prirodan broj: "))
# 
# for i in range(1,broj_ucenika+1, prirodan_broj):
#     print("ispitivati ce se ucenici sa rednim brojevima:", i)

# for i in range(10):
#     for j in range(10):
#         print("i:",i,"j:",j)

# broj = int(input("unesite neki broj: "))
# for i in range(1,broj+1):
#     if broj % i == 0:
#         print("broj je deljiv sa",i)

# for broj in range(1,11):
#     for i in range(1,broj+1):
#         if broj % i == 0:
#             print(broj,"je deljiv sa",i)
#     print("")

# for i in range(10):
#     if i == 7:
#         break
#     print(i)
# for i in range(10):
#     if i == 7:
#         continue
#     print(i)

mylist = ["apple", "banana", "cherry", "melon"]

# print(mylist)
# print(mylist[1])
 
# print(mylist[1:3])
# print(mylist[1:])
# print(mylist[:3])
 
# mylist[1] = "kiwi"
# mylist[1:3] = ["kiwi", "ananas"]
# mylist[1:3] = "ananas"
# mylist[1:3] = ["ananas"]

# print(len(mylist))
# print(type(mylist))

mylist.append("strawberry")
mylist.insert(1, "ananas")
print(mylist)
