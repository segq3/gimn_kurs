# suma = 0
# for i in range(21):
#     if i % 2 == 0:
#         suma = suma + i
#         print("nakon broja",i,"zbir je",suma)

# for i in range(3):
#     print("python")
# for i in range(3):
#     print("je super")

# broj = int(input("unesite neki broj: "))
# for i in range(1,broj+1):
#     print(i)

# broj = int(input("unesite neki broj: "))
# for i in range(1,broj+1):
#     if i % 2 == 0:
#         print(i)

brojevi = []
broj_brojeva = int(input("unesi broj brojeva: ")) # unos brojeva
for i in range(broj_brojeva):
    x = int(input("unesi broj: "))
    brojevi += [x]

parni = 0
neparni = 0

for i in brojevi:
    if i % 2 == 0:
        parni += i
    else:
        neparni += i

print("zbir parnih:", parni)
print("zbir neparnih:", neparni)
