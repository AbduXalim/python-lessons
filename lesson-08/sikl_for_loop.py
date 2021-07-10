
# ---------- FOR LOOP ------------------

mehmonlar = ["Ali",'Vali','Hasan','Husan']
# print("salom",mehmonlar[0])
# print("salom",mehmonlar[1])
# print("salom",mehmonlar[2])
# print("salom",mehmonlar[3]) # ammo bu usul notog'ri
# for mehmon in mehmonlar:
#    print("Salom",mehmon)
# print('Hayr', mehmon) # etibor bering sikldan tashqariga yozildi bu. abzaz joy tashash sababli
    
# for mehmon in mehmonlar:
#    print("Hurmatli {mehmon}, sizni 20 dekabr kuni nahorgi oshga taklif qilamiz")
#    print("Hurmat bilan, Palonchiyevlar oilasi.")

# sonlar = list(range(0,11))
# for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")
# endi shu sonlar kvadratini bir ruyhatga saqlab qoyamiz.

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#    sonlar_kvadrati.append(son**2)  
# print(sonlar)
# print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting \n >>>")) # n+1 sababi 0 dan boshlamasligi uchun
print(dostlar)



