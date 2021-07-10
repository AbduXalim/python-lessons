
# -------------- If elif else -------------------
# son = int(input("Sonni kiriting: >>>"))
# if son<0:
#    print("Manfiy son")
# else:
#    print("Musbat son")
# ------------- --------------------- -------------------


# -------------- Toshkent city ga kirish -----------------
# yosh = int(input("Yoshingiz nechida? >>>"))
# if yosh <=4:
#    print("Sizga kirish bepul")
# elif yosh<=12: # aks holda agar......
#    print("Sizga kirish 5000 so'm")
# elif yosh<=18: # bu bilan xoxlagancha shart kiritib ketish mumkin.
#    print("Sizga kirish 8000 so'm")
# else:
#    print("Sizga kirish 10 000 so'm")
# ------------------ ------------------ ----------------


# -------------- Toshkent city 2-sul -----------------
# yosh = int(input("Yoshingiz nechida? >>>"))
# if yosh <=4:
#     narh = 0
# elif yosh<=12: # aks holda agar......
#     narh =5000
# elif yosh<=18: # bu bilan xoxlagancha shart kiritib ketish mumkin.
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so'm")
# ------------------ ------------------ ----------------


# ------------------ Dam olish kunlarini aniqlash ----------------
# kun = input("Bugun nima kun? >>> ")
# if kun.lower()=="shanba" or kun.lower()=="yakshanba": # yoki yo unisi yo bunisi bajarilsa kiradi.
#     print("Bugun dam olish kun.")
# else:
#     print("Bugun ish kuni.")
# -------------- ---------------------- --------------------------


# ------------------ Dam olish kunlarida nima qilish ----------------
# kun = input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? >>>"))
# if kun.lower()=="yakshanba" and harorat>=30: # ikkita shart ham bajarilsagina kiradi.
#     print("Cho'milgani ketdik.")
# elif kun.lower()== "yakshanba" or kun.lower()=="shanba" and harorat<30: # kabi xoxlagancha shart kiritib ketishi mumkin.
#     print("Uyda dam olamiz!")
# boshqa kunlarga ham xoxlagancha kiritib yozishingiz mumkin.
# -------------- ---------------------- --------------------------


# ------------------ Restaranga dastur yozish ----------------
# narx = 15000 # mijoz 15 000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi.
# salat = False # mijoz salat olmadi.
# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narx = narx + 10000 # narxga 10000 so'm qoshamiz
# elif choy or salat: # agar mijoz choy yoki salat olgan bo'lsa
#     narx = narx + 5000 # narxga 5000 so'm qoshamiz.
# print(f"Sizning xisob {narx} bo'ldi")
# if elif qilib yozib ketaversak kamchiligi shundagi tepadan qaysi birinchi bajarilsa qoganlarini kirmaydi. shu zahoti to'xtaydi.
# -------------- ---------------------- --------------------------


# ------------------ Restaran 2-dastur ----------------
# True False bu Booleen malumotlar turi xisoblanadi.
# narx = 15000 
# choy = True 
# salat = False
# non = 1 # 1=True . son bilan ham yozib ketsak bo'ladi. 
# kampot = 0 # 0 = False ga teng
# salfetka = 1 # 1=true
# # quyida faqat if lar har bir shart alohida tekshiriladi kamchiliksiz.
# if choy: # agar mijoz choy olsa
#     narx = narx + 3000 
#     print("mijoz choy oldi,")
# if salat: # agar mijoz salat olsa
#     narx = narx + 5000 
#     print("mijoz salat oldi,")
# if non:
#     narx = narx+3000
#     print("mijoz non oldi,")
# if kampot:
#     narx = narx+4000
#     print("mijoz kampot oldi,")
# if salfetka:
#     narx = narx+2000
#     print("mijoz salfetka oldi,")
# print(f"Mijoz jami xisobi {narx} bo'ldi")
# -------------- ---------------------- --------------------------


# ----------------------- ----------------- ---------------------
# menu = ["osh", "qozonkabob",'shashlik','norin','somsa']
# 'manti' in menu # consoleda chiqarib koramiz. False qaytaradi.
# 'norin' in menu # True
# biz ruyhat ichida bor yoki yoqlini shunday tekshiramiz.
# ----------------------- ----------------- ---------------------


# --------------- Buyurtma qabul qilish dasturi ----------------
# menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
# ovqat = input("Nima ovqat zakas qilasiz? \n>>>")
# if ovqat.lower() in menu: # in menu -> ichida bormi?
#     print('Buyurtma qabul qilindi.')
# else:
#     print("Afsuski bizda bunaqa ovqat yo'q")
# ------------------- ----------------------------- ------------


# --------------- Buyurtma qabul qilish dasturi ----------------
# menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
# ovqat = input("Nima ovqat zakas qilasiz? \n>>>")
# if ovqat.lower() not in menu: # not in ichida yo'qmi?
#      print("Afsuski bizda bunaqa ovqat yo'q") 
# else:
#      print('Buyurtma qabul qilindi.')
# ------------------- ----------------------------- ------------


# --------------- Buyurtma qabul qilish 2-dasturi ----------------
# ko'p buyurtmalarni menudan tekshirish
menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
buyurtmalar =['osh','somsa','manti','shashlik']
buyurtmalar2 = []
if buyurtmalar2: # avvalo ruyxatimiz bo'sh emasligini tekshirishimiz kerak chunki albatta client dan zakas olamiz.
    for taom in buyurtmalar2:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz menuda {taom} yo'q")
else:
    print("Savatchangiz bo'sh")
# ------------------- ----------------------------- ------------




