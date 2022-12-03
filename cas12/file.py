thislist = ["apple", "banana", "cherry", "mango"]
# thislist.pop(1)
# thislist.remove("cherry")

# thislist.clear()

# del thislist[1:3]

# resenje 1
# for i in range(len(thislist)):
#     print(thislist[i])

# resenje 2
# for i in thislist:
#     print(i)

# for i in thislist:
#     if 'a' in i:
#         thislist.remove(i)

# temp = []
# for i in thislist:
#     if not 'a' in i:
#         temp.append(i)

# i = 0
# while i < len(thislist):
#     if "a" in thislist[i]:
#         thislist.pop(i)
#         i -= 1
#     i += 1

temp = [x for x in thislist if 'a' in x]
print(temp)
 
# for i in range(len(thislist)):
#     thislist[i] = thislist[i].upper()

# lista = ["a", "c", "d", "b"]
# print(lista.sort())
# lista = [200,3,10]
# print(lista.sort(reverse = True))

# lista = ["apple", "cherry", "apple"]
# print(lista.count("apple"))
