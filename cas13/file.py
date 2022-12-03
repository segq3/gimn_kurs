# a = 0

# while a<5:
#     print(a)
#     a += 1

# while True:
#     print("hello")

# lozinka = "asdf"
# odgovor = input("Loznika: ")
# print()
# 
# while lozinka != odgovor:
#     print("Upisali ste netacnu lozinku.")
#     odgovor = input("Loznika: ")
#     print()
# 
# print("Upisali ste tacnu lozinku.")

# tacan = 53
# unos = int(input("unesite broj: "))
# 
# while unos != 0:
#     if unos == tacan:
#         print()
#         print("uneli ste tacan broj!")
#         unos = int(input("unesite broj: "))
#     elif unos > tacan:
#         print()
#         print("uneli ste prevelik broj")
#         unos = int(input("unesite broj: "))
#     elif unos < tacan:
#         print()
#         print("uneli ste premali broj")
#         unos = int(input("unesite broj: "))

broj = int(input("unesite broj u rasponu 10-20: "))

while broj:
    if broj >= 10 and broj <= 20:
        print("broj je u rasponu 10-20")
    else:
        print("broj nije u rasponu 10-20")

    print()
    broj = int(input("unesite broj u rasponu 10-20: "))

    
