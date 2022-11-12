visina_najviseg = 0
visina_najnizeg = 99999

broj_ucenika = int(input("unesite broj ucenika: "))
for i in range(broj_ucenika):
    visina = int(input("unesite visinu ucenika: "))
    if visina > visina_najviseg:
        visina_najviseg = visina
    if visina < visina_najnizeg:
        visina_najnizeg = visina
 
print("najvisi:", visina_najviseg)
print("najnizi:", visina_najnizeg)

