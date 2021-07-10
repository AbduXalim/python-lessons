
# -------------- Sintax Errors ---------------
# print "Hello world!" # console dagi xatoni koramiz va tarjima qilamiz.
# print ("Hello world!" # bunda xatolik qayerdaligini ko'rsatmaydi. EOF
# print("Hello world!) # EOL xatolik
# ---------- --------------- ----------------
       

# --------------- IndentationError ------------
#  print("Hello world!") # bo'sh joy qolib ketdi. tarjima qilib ko'ring.
# print("O'ngacha sanaymiz:") 
# for n in range((10)):
# print(n+1) # for sikl ichiga kirgandan so'ng space bo'lishi kerak. Aslida qancha joy tashash farqi yoq ammo bitta tab yoki 4 ta space tashash dasturchilar sintax.
#   print(n+2) # ikki xil joy tashalsa ham xato beradi.
# ----------- ---------------- ----------------


# -------------- TypeError --------------------
# son = input("Istalgan son kiriting: >>>")
# print(type(son))
# son = int(son) # shunday qilib type ni o'zgartirib olishimiz kerak.
# print(f"{son} ning kvadrati {son**2} ga teng.") # ishlamaydi chunki str bo'lib kelyabdi.
# ----------- ---------------- ----------------

# ---------------- NameError ------------------
# prit("Hello world!") # xar qanday atalgan nomlar xato yozilsa.
# mevalar = ['olma','uzum','nok','banan','anor']
# for meva in mevlar: 
#     print(meva)
# ----------- ---------------- ----------------


# ---------------- ValueError -----------------
# son = int(input("Istalgan son kiriting:>>>")) # shu yerda 12.5 kabi 10lik son kiritsak xatolik beradi. buni yechimi yoki float type ga o'tqazish kerak yoki istalgan son demaslik kerak:)
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
# ----------- ---------------- ----------------

# -------------------- IndexError -------------
# mevalar = ['olma','gilos','anjir','uzum']
# print(mevalar[4]) # xatoni tarjima qilib ham tezda bilib olishimiz mumkin.
# ----------- ---------------- ----------------


# ------------- ZeroDivisionError -------------
# x,y = 50,50
# z = 250/(x-y)
# print(z) # sababi dasturlashda nolga bo'lib bo'lmaydi.
# ----------- ---------------- ----------------

# ---------- ----------------- ----------------
# mevalar = ['olma','gilos','anjir','uzum']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi.") 
# ---------- ----------------- ----------------






