
# --------------- STRING USTIDA AMALLAR ------------------
# ism = "Abduxalim"
# familiya = "To'xtayev"
# print(ism + familiya) # o'zgaruvchilarni bir biriga qo'shish
# print(ism + ' '+familiya) # o'rasini ochib qo'shish    

# print("Mening ismim " + ism) # + plus ishorasi yordamida qoshish

# ----- f-string usuli -----
# ism_sharif = f"{ism} {familiya}" # bu usul yordamida ham o'zgaruvchilarni qo'shishimiz mumkin
# print(ism_sharif) 
# print(f"Salom, mening ismim {ism}. {ism} {familiya}")

# ---------- Maxsus Belgilar--------
# print("Hello world!")
# print("Hello \tworld!")
# print("Hello \nwordl!")

# ---------- String metodlari ----------
# ism = 'James'
# familiya = "bond"
# ism_familiya = f"{ism} {familiya}"
# print(ism_familiya.upper()) # hamma harflarni katta harflar bilan yozadi.
# print(ism_familiya.lower()) # hamma harflarni kichik harflar bilan yozadi.
# print(ism_familiya.title()) # barcha so'zlarni birinchi harfini katta harf bilan yozadi.
# print(ism_familiya.capitalize()) # faqat birinchi harfini katta harf bilan yozadi.

# meva = "    olma    "
# print(meva)
# print("men " + meva.lstrip() + "yaxshi ko'raman") # chap tomonidagi bo'shliqni olib tashlaydi.
# print("men " + meva.rstrip() + " yaxshi ko'raman") # o'ng tomonidagi bo'shliqni olib tashlaydi.
# print("men " + meva.strip() + " yaxshi ko'raman") # har ikki tomonidagi bo'shliqni olib tashlaydi.
# print("men " + meva + " yaxshi ko'raman")

# ---------- Input funksiyasi ---------
# name = input("Ismingiz nima?") # console yordamida foydalunuvchidan malumot olish
# print("Assalomu aleykum, "+name)
name = input("Ismingiz nima?\n>>> ")
print("Assalomu aleykum," +name.title()) # bosh harf bilan yozib berish metodi
