
# ------------------------- LIST - Ro'yxat -------------------

mevalar = ["olma", "o'rik", "shaftoli", "nok"] # matnli hammasi mevalar ro'yxati
narxlar = [12000,18000,22000,24000,27000, -25000, 3.6001] # sonli hammasi
sonlar = ["bir","ikki","uch",4,5,6] # matn va son aralash ro'yxat
ismlar = [] # bu bo'sh ro'yxat albatta bo'sh royxat bo'lishi mumkin
# index tushunchasi. albatta 0dan boshlanadi. minus index ham bo'ladi.
# print(sonlar)
# print(mevalar[-1]) # oxirgi elementni olish. 
# print(mevalar[2].upper()) # metodlar bilan ham foydalanish
# print(narxlar[2],narxlar[4]) # xoxlagan 1 tadan ko'p elementni olish
# print(narxlar[1]+narxlar[3]) # albatta arifmetik amallarni ishlatish ham mumkin
# mevalar[0] = 'anor' # ro'yxat ichidan qiymatlarni o'zgartishish
# print(mevalar)
# ----------- qiymat qo'shish --------------
# mevalar.append("tarvuz") # list oxiriga qiymat qoshish
# mevalar.insert(1,"banan") # list xoxlagan joyiga index orqali qiymat qoshish
# print(mevalar)

# ----------- qiymat o'chirish --------------
# cars = []
# cars.append("matiz")
# cars.append("spark")
# cars.append("nexia")
# cars.append("cobalt")
# cars.append("lacetti")
# cars.append("gentra")
# cars.append("tracker")
# cars.append("tracker")
# cars.append("malibu")
# del cars[3] # index orqali ochiramiz.
# del cars[-1] # nechta bo'lishidan qat'iy nazar oxirgisini ochirish
# cars.remove("gentra") # nomi bilan ochirish
# cars.remove("tracker") # ikkita bo'lsa birinchisini o'chiradi.
# print(cars)
# cars.insert(3, "malibu 2")
# print(cars)  

# ---------------   qiymatni ko'chirish------------------
# bozorlik = ["yog'", "un","piyoz","banan","go'sht"]
# mahsulot = bozorlik.pop(3) # ro'yxatdan sug'urib olish
# print(mahsulot)
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: " , bozorlik)
# mahsulot2 = bozorlik.pop() # index bermasak oxirgi elementni sug'urib oladi.
# print(mahsulot2)

# -------------------------------------------
# narxlar[2] = 12345 # qiymat o'zgartirish
# narxlar[2] = narxlar[2] + 768 # qiymat ustiga qoshish
# narxlar.remove(3.6001)
# print(narxlar)

