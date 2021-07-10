
# ------------------ Ro'yxat tartiblash -------------------
cars = ['Bmw','mercedes','volvo','general motors','tesla','audi']
# cars.sort() # [abc] alfavit boyicha tartiblash ammo ichida katta harf bilan yozilgani bo'lsa birinchi keladi.
# qoida sort funksiyasidan oldin stringdagi upper lower title capitalise funksiyalaridan foydalanishimiz tog'ri bo'ladi. 
# cars.sort(reverse=True) # [abc] dan teskari tartiblash
# print(sorted(cars))  # asl ruyxatga joyini ozgartirmagan xolda tartiblab ko'rsatish
sonlar = [12,22,33,42,55,65,78,-31,24.55]
sonlar.sort() # kichikdan boshlab taxlash
sonlar.sort(reverse=True) # kattadan boshlab taxlash
# print(sonlar)
# print(len(cars)) # nechta qiymat borligni sanaydi.
# print(len(sonlar)) # nechta qiymat borligni sanaydi.
# uzunlik = len(cars) # funksiyani o'zgaruvchiga o'zlashtirib qoyish
# print(uzunlik)
numbers = list(range(11,31)) # birinchi va ikkinchi sonlar orasidagi qiymatlar bilan to'ldirish, oxirgi qiymat kirmaydi
odd_numbers = list(range(1,20,2)) # toq sonlar bilan to'ldirish
even_numbers = list(range(0,20,2)) # juft sonlar bilan to'ldirish
# print(numbers)
count = list(range(0,101,10)) # o'nlik sonlar bilan to'ldirish
# print(count)
max_value = max(even_numbers) # eng katta qiymatni aniqlash
# print(max_value)
min_value = min(numbers) # eng kichkina qiymatni aniqlash
# print(min_value)
all_value = sum(numbers)
# print(all_value)

# ------------------- MIN , MAX , SUM ----------------
narxlar = [12000,31500,22300,500,325,43000]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
# print("Eng arzon narx" ,arzon,"\nEng qimmat narx",qimmat,"\nJami:" ,jami)

# print(cars[2:5]) # qaysidan qaysigacha kerak bo'lsa indexsigacha yozib ajratib chiqarish
# print(cars[:3]) # boshlangich indexni 0 dan oladi.
# print(cars[2:]) # oxirigacha chiqaradi.

my_cars = cars # copy qilib olish 
my_cars.remove("volvo") # nomi bilan olib tashlash
my_cars[0] = "spark" # qiymatni almashtirish

cars.append("bmw") # etibor beraylik ikkisiga ham qoshilib qoldi. chunki biz copy qilmagandik. shunchaki bitta listga ikkita nom berib qoygandik
my_cars2 =cars[:] # manabu kesish usuli bn copy qilsa bo'ladi. endi ochirib qoshib tekshirib ko'rsak bo'ladi.
# print(cars)
# print(my_cars)

# ------ TUPLE nomli o'zgarmas ro'yxat ----------------
toys = ('bus','car','bear','dino','snake','lizard') # qo'shish o'zgartirish ochirish qilib bo'lmaydi.
# print(type(toys)) # turini tekshirish
toys = list(toys) # turini ruyxatga o'zgartirish 
# print(type(toys)) 
# toys.append("teddy")
# print(toys) # korib turganizdek endi qoshilyabdi.
toys = tuple(toys) # turini tuple ga o'zgartirish

