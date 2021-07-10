# --------------- If else shartlari va tarmoqlanish ------------------

avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#    print(avto.title()) # ruyxatdagi har bir qiymatni bosh harfda yozib beradi.

# for avto in avtolar: # avtolar ichidagi har bir avto uchun...
#    if avto == 'bmw': # agar avto bmw ga teng bo'lsa ...
#        print(avto.upper()) # avto nomini hamma harflarini kattalashtirib yoz
#    else: # ... aks holda
#        print(avto.title()) # avto nomini faqat birinchi harfini kattalashtir
# console da true false farqini tenglashtirib tushuntirish
# true false matnni katta kichik harfligi ham etiborga olinadi. shuning imkon qadar lower() funksiyasi yordamida kichiklashtirib olish kerak
a = 5
a == 5 # true # teng
a == 6 # false
a != 6 # true # teng emas
a != 5 # false
# ------------- ------------------ -----------


# ------------- ------------------- ---------
# ism = input("ismingizni kiriting?\n>>>")
# if ism.lower() != 'ali':
#    print(f"Uzr, {ism.title()} biz Alini kutyabmiz.")
# else:
#    print("Salom, Ali xush kelibsiz.")
# ------------- ------------------ -----------


# ------------ -------------- -----------------
#javob =float(input("12x6 nechiga teng? >>>"))
# if javob !=72:
#    print("javob xato")
# else yozish majburiy emas.
# ------------- ------------------ -------------


# -------------- ----------------- -------------
# yosh = int(input("yoshingiz nechida? >>>"))
# if yosh>=18: # katta yoki teng bo'lsa
#    print("Xush kelibsiz!")
# else:
#    print("Kirish mumkin emas.")

b = 5
b > 6 # false # kichik
b < 6 # true  # katta
b >= 6 # false # teng yoki kichik
b <= 6 # true # teng yoki katta
# ------------- ------------------ ------------


# ------------ ---------------- ---------------
# login = input("yangi login kiriting:")
# if len(login)<=5: # login uzunligini tekshiramiz
#    print("Login 5 harfdan katta bo'lishi shart!")
# else:
#    print("Yangi login muvaffiqiyatli saqlandi.")
# ------------- ------------------ ---------------


# ------------- ------------------ ---------------
# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2020-yil<18: # foydalanuvchi yoshini xisoblaymiz.
#    print(f"Yoshingiz {2020-yil} da ekan")
#    print("Sizga kirish mumkin emas!")
# else:
#    print("Xush kelibsiz.")
# ---------------- ---------------- -----------------



# ---------------- ------------------ ---------------
# yosh = int(input("Yoshingiz nechida? >>>"))
# if yosh>65: print("Sizda COVID-19 chalinish extimolligi yuqori") # bitta qatorda yozish

x,y = 50,55
print("x>y") if x>y else print("x<y") # hammasini bir qatorda yozish
# ------------- ------------------ ---------------



