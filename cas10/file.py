# visina_najviseg = 0
# visina_najnizeg = 99999
# 
# broj_ucenika = int(input("unesite broj ucenika: "))
# for i in range(broj_ucenika):
#     visina = int(input("unesite visinu ucenika: "))
#     if visina > visina_najviseg:
#         visina_najviseg = visina
#     if visina < visina_najnizeg:
#         visina_najnizeg = visina
#  
# print("najvisi:", visina_najviseg)
# print("najnizi:", visina_najnizeg)

pozitivna_suma, negativna_suma, pozitivni_broj_temp, negativni_broj_temp = 0, 0, 0, 0
for i in range(10):
    temp = int(input("unesite temperaturu: "))
    if temp > 0:
        pozitivna_suma += temp
        pozitivni_broj_temp += 1
    elif temp < 0:
        negativna_suma += temp
        negativni_broj_temp += 1

print("srednja temperatura iznad nule: ", pozitivna_suma/pozitivni_broj_temp)
print("srednja temperatura ispod nule: ", negativna_suma/negativni_broj_temp)
