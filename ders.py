# Ev tapsiriqlari izah


# mylist = input("deyerleri daxil edin: ").split()
# i = 0
# # newlist=[]
# while i < len(mylist):
#     if mylist[i].isdigit():
#         if int(mylist[i]) % 2 == 0:
#             print(mylist[i], end=" ")
#     i = i + 1

# 2. Sadə ədəd - o ədədə deyilir ki, yalnız 1ə və özünə
# bölünür. Məsələ, 13, 47, 31 və s. Daxil edilən ədədin sadə
# olub olmadığını yoxlayan kod yazın.


# num = int(input("ededi daxil edin: "))
#
# for i in range(2, num):      #2,3,4,5,6,7,8,9,10               11
#     if num % i == 0:
#         print("Murekkebdir")
#         break
# else:
#     print("Sadedir")


# 5. İstifadəçidən 3 ədəd alın, hansı böyükdürsə, onun
# rəqəmlərini newlist-ə əlavə edin


# num1 = int(input("1-ci ededi daxil edin: "))
# num2 = int(input("2-ci ededi daxil edin: "))
# num3 = int(input("3-cu ededi daxil edin: "))
# newlist = []
#
# if num1 > num2 and num1 > num3:
#     for i in str(num1):
#         newlist.append(int(i))
# elif num2 > num1 and num2 > num3:
#     for j in str(num2):
#         newlist.append(int(j))
# elif num3 > num1 and num3 > num2:
#     for z in str(num3):
#         newlist.append(int(z))
# else:
#     print("Wrong process")
#
# print(newlist)


# 6. İstifadəçidən bir parol alın, parolun uzunluğu 5dən
# böyük olmadığı təqdirdə parolu soruşmağa dəvam etsin,
# yəni dövr etsin.

# while True:
#     parol = input("Parolu daxil edin: ")
#
#     if "@" in parol:
#         print("Siz parolu duzgun daxil etdiniz")
#         break


# Istifadeci eded daxil edir. Ededin reqemlerini list-e elave edin, amma ele edin ki, tekrar reqemler
# olmasin

# Istifadeci 2 eded daxil edecek. Siz bu 2 eded arasinda olan ededlerin cemini tapmalisiniz.


# num1 = int(input("baslangici daxil edin: "))
# num2 = int(input("sonu daxil edin: "))
# cem = 0
#
# for i in range(num1 + 1, num2): # 5 ve 15
#     cem = cem + i
# print(cem)


# Istifadeci 2 eded daxil edecek. Siz bu 2 eded arasinda olan ededlerin hasilini tapmalisiniz.


# num1 = int(input("baslangici daxil edin: "))
# num2 = int(input("sonu daxil edin: "))
# cem = 1

# for i in range(num1 * 1, num2):  # 5 ve 15
#     cem = cem * i
# print(cem)


#NESTED - ic-ice


# mylist = [1,212,312,42,524,24234]
# mylist_2 = ['salam', 'sagol', 'ders']


# for i in mylist:
#     for j in mylist_2:

# for j in mylist_2:
#     print(j)




# mylist = [[1,2,3], [4,5,6], [7,8,9]]


# for i in mylist:
#     for j in i:
#         print(j)



# Istifadeciden parol alin. Eger parol "alma" sozune beraberdirse yaxud icinde "_" simvolu varsa ve
# uzunlugu
# 5den boyukdurse dovr dayansin ekrana parol duzdur cixsin


# while True:
#     parol = input("Parolu daxil edin: ")
#
#     if "@" in parol:
#         print("Siz parolu duzgun daxil etdiniz")
#         break


# while True:
#     parol = input("parolu daxil edin: ")
#
#     if (parol == 'alma' or "_" in parol) and len(parol) > 5:
#         print("Parol duzdur")
#         break

# 1. İstifadəçinin daxil etdiyi ədədin faktorialını tapın. (Faktorial 1dən həmin ədədə qədər olan ədədlərin hasilidir. Ədədin özü də daxildir).
# num1 = int(input("ededi daxil edin: "))
# hasil = 1

# for i in range(1,num1+1 ):
#     hasil = hasil * i
# print(hasil) 

# 2. Verilmiş ədədin tərsini çap edin. For loop ilə.
# mylist = [1, 2, 3, 4, 5]
# print(mylist)
# reversed_list = []
# for i in mylist:
#   reversed_list = [i] + reversed_list
# print(reversed_list) 
   

# 3. İstifadəçi 2 ədəd daxil edəcək. Bu 2 ədəd arasında olan sadə ədədləri bir newList-ə əlavə edin.

# num1 = int(input("birinci daxil edin: "))
# num2 = int(input("ikinci ededi daxil edin: "))             
# newlist = []
# for i in range(num1 + 1, num2):
#     if  i % i == 0:
#         print("Murekkebdir")
#         break
# else:
#    newlist.append(int(i))
# print(newlist)

# 4. For dövr operatorunun else halı nə vaxt işə düşür ?
# for dovrunde break ise dushmedikde  halda  ishe dushdur

# 5. İstifadəçi ədəd daxil edəcək, əgər ədədin rəqəmlərinin 
# kavdratları cəmi ədəddən böyük olarsa, 
# ekrana "Good number", əgər kiçik olarsa "Bad number"
#  çap edin. (Məsələn, 42 --> 4² + 2² = 20, 20 <42. 
# Ekrana "Bad number çap olunmalıdır".).

# nums = input("Ededleri daxil edin: ")
# nums = list(map(int, nums))

# num1 =nums[0]**2 + nums[1]**2
# nums=str(nums)
# num1=str(num1)
# for i in nums:
#  if nums < num1:
#    print(type(nums))
#   print("Bad number")
#  if nums > num1:
#   print("Good number")


# 6. İstifadəçi istədiyi qədər sözlər daxil edəcək. Bir dəyişənə bu sözlərin hamısının 
# birləşməsini mənimsədin. (Ekrana çap edərək birləşdirməyin, bir dəyişənə mənimsədərək
#  birləşdirin ki, sonra bu dəyişəni istifadə edə biləsiniz.).
# 7. mytuple = ("alma","armud","nar","kivi")
# bu tuple-ın elementlərini həm while
#  həm də for dövr operatorları vasitəsilə yeni bir 
# list-ə əlavə edin.
# mytuple = ("alma","armud","nar","kivi")
# newlist = []
# for i in mytuple:
#     newlist.append(i)
# print(newlist)
# ['alma', 'armud', 'nar', 'kivi']

# # 8. mylist = [45, -4, 12, 16, 128, 0, 10]
# bu list-in maksimum elementini tapan kod yazın. 
# (Dövr və şərt operatorlarından istifadə edərək).
# mylist = [45, -4, 12, 16, 128, 0, 10]
# newlist = []
# for i in sorted(mylist):
#  newlist.append(int(i))
# print(newlist[-1::])
# i = 0
# newlist=[]
# while i == len(mylist):
#  mylist= newlist.append(int(i))
# newlist = str(mylist.sort())
# print(mylist[-1::])
# i = i + 1

# 9. mylist = [45, -4, 12, 16, 128, 0, 10]
# bu list-in minimum elementini tapan kod yazın.
#  (Dövr və şərt operatorlarından istifadə edərək).
# mylist = [45, -4, 12, 16, 128, 0, 10]
# newlist = []
# for i in sorted(mylist):
#  newlist.append(int(i))
# print(newlist[0:1])

# i = 0
# newlist=[]
# while i == len(mylist):
#  mylist= newlist.append(int(i))
# newlist = str(mylist.sort())
# print(mylist[0:1])
# i = i + 1

# 1. İstifadəçinin daxil etdiyi ədədin rəqəmlərindən 
# ən böyüyünü ekrana çap edən kod yazın.

# nums = input("ededi daxil edin: ").split()             
# newlist = []
# for i in nums:
#  newlist= sorted(nums)
#  print(newlist[-1::])

# 2. İstifəçidən bir söz alın və həmin sözdə 
# ən çox təkrarlanan hərfi tapın.
# mytuple = input("sozu daxil edin: ")
# count = 0
# for i in mytuple:
#     if i == 'a':
#         count = count + 1
# print("tekrar edilen herf say: "
#       + str(count))
# 3. random kitabxanasını araşdırın.
#  Hər hansı bir dəyişənə random bir ədəd mənimsətməyi öyrənin.                                                                                                      
#  (4cü məsələdə istifadə edəcəksiniz.).

# 4. Bir ədəd tipdə dəyişən yaradın və ona random
# kitabxanasından istifadə edərək, random bir ədəd mənimsədin. 
# Daha sonra istifadəçidən bu ədədi tapmasını tələb edin.
#  Məsələn, random ədəd 48dir. İstifadəçi 48dən yuxarı ədəd
#  daxil edəndə yazsın ki, aşağı düşün, 48dən aşağı ədəd daxil 
# etdikdə yazsın ki, yuxarı qalxın. Ta ki, ədədi tapana qədər.
#  Əgər taparsa dövr dayansın, və "Tebrikler" çap edilsin.

# 5. İstifadəçidən bir cümlə daxil etməsini tələb edin.
# Və bu cümlədə sözlər boşluqlarla ayrılmış şəkildədir. 
# Lakin siz elə edin ki, bu boşluqlar "@" işarələri ilə
#  əvəz olunsunlar.

# 6. Tuple, set, dictionary, list təkrarlayın. (Suallar verəcəm).

# 7. İstifadəçi 1dən 9a qədər(9da daxil olmaqla) 
# rəqəmlər daxil edə bilər. Hansı rəqəmi daxil etsə
#  həmin rəqəm saylı ən böyük ədədi çap etsin. 
# Məsələn 4dürsə, 9999 çap etsin.
# reqem = int(input("ededi daxil edin:"))
# for i in range(1,reqem ):
#  print(reqem)
# 8. (%, //, /) operatorları, and or operatorları təkrarlayın.
#  (Suallar verəcəm.).

# 9. İstifadəçidən bir hərf alın. 
# Daha sonra hərfin sait yaxud samit olduğunu tapın.
# herf = input("herfi daxil edin: ")
# saitler =('a','ı','o','u','i','ə', 'e', 'ö','ü') 
# if herf in saitler:
#     print("saitdir")
# else:
#       print("samitdir")
   

# 10. İstifadəçidən ədəd istəyin.
#  Ədədin rəqəmləri cəmi cütdürsə ekrana
#  "cüt", əks halda "tək" çap edin.

# nums = input("Ededleri daxil edin: ")
# nums = list(map(int, nums))
# num1 =nums[0]+ nums[1]
# if num1 % 2 == 0:
#     print("eded cutdur", num1)
# else:
#      print("eded tekdir",num1)
# importing the random module
# import random
# 3. İstifadəçidən ədədlər alın və həmin ədədlərin medianını tapın.
# (Median - sıralanmış sırada əgər ədədlərin sayı tək ədəddirsə tam ortadakı ədəd,
# əgər ədədlərin sayı cütdürsə, ortadakı 2 ədədin cəminin yarısıdır. Məsələn, 2,56,7,90,1
# --> burada medianı tapmaq üçün ədədləri azdan çoxa düzürük daha sonra ortadakı ədədi median
# qəbul edirik: 1,2,7,56,90 --> median = 7). Əgər ədədlərin
# sayı cüt olsa idi,məsələn; 1,2,7,11,56,90 --> median = (7+11)/2= 9 olacaq.

# 1,2,3,4,5,23,34,67

# 7 // 2 = 3

# nums = input("Ededleri daxil edin : ").split()
# nums = list(map(int, nums))
# median = 0
#
#
# if len(nums) % 2 == 1:
#     median = nums[len(nums)//2]
# else:
#     median = (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
#
# print(median)
# print(nums)

# 4.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# Dövr operatorlarından istifadə etməklə ekrana çap edin

# n = 6
#
# for i in range(1, n + 1, 1):
#     print("* " * i)
#
# for j in range(n - 1, 0, -1):
#     print("* " * j)

# eval() funksiyasını və ~ bu işarəni araşdırın

# print(~20)

# eval("print('555')")


# Kitabxanalar, modullar

# 3 cur olur :


# RANDOM


# import random
#
# mylist = ["apple", "banana", "cherry"]
#
# print(random.sample(mylist, k=3))


# import random
#
# mylist = ["apple", "banana", "cherry"]
#
# print(random.choice(mylist))


# import random
#
# print(random.randint(3, 9))


# mylist = [1, 2, 3, 4, 5]
# print(mylist)
# reversed_list = []
#
#
# for i in mylist:
#     reversed_list = [i] + reversed_list   # [1] + [] = [1], [2] + [1] = [2,1], [3] + [2,1] = [3,2,1]
# print(reversed_list)
# mylist_2 = list(reversed(mylist))
# print(mylist_2)

# IMTAHAN (Keçirilənlərin üzərində qurulmuşdur.)
# 1.Daxil edilən ədədin Armstronq olub olmamağını 
# yoxlayın. (Armstronq ədəd o ədədə deyilir ki, onun 
# rəqəmlərinin kubları cəmi özünə bərabər olsun. 
# Məsələn, 153 -- > 1^3 + 5^3 + 3^3 = 153).
# num1 = input("ededleri daxil edin:")
# num2 = 0
# for i in num1:
#  num2 = num2+int(i)**3
# if int(num1) == num2:
#     print("Eded Armstronqdur", num1)
# else:
#      print("Eded Armstronq deyil ",num1)


# 2.Daxil edilən ədədin polindrom olub olmadığını 
# yoxlayan kod yazın. (Polindrom ədəd o ədədə deyilir 
# ki, tərsi də özünə bərabər olsun, məsələn: 77, 121, 
# 1221 və s.)
# num = input("ededleri daxil edin: ")
# if num == num[::-1]:
#     print("Yes its a palindrome")
# else:
#     print("No, its not a palindrome")

# 3.Daxil edilən sözdə sait hərflərin sayını tapan python 
# kodu yazın.


# soz = input("sozu daxil edin: ")
# saitler =('a','ı','o','u','i','ə', 'e', 'ö','ü')
# saygac = 0
# for i in soz:
#    for j in saitler:
#          if j == i: 
#               saygac += 1
# print(saygac)


# 4.İstifadəçi tərəfindən daxil edilən 2 ədəd arasında olan
# ədədlərin hasilini tapan python kodu yazın.
# num1 = int(input("1-ci ededi daxil edin: "))
# num2 = int(input("2-ci ededi daxil edin: "))
# for i in range(num1, num2+1): 
#     for j in range(2,i):
        # print(int(i * j))

# 5.Üstü qüvvətə yüksəltmə operatoru hansıdır ? Və biz 
# kök altda 64ü bu operator vasitəsilə necə taparıq ? 
# (sualın 2-ci hissəsi riyazi biliyə əsaslanır, 
# bilməməyiniz problem deyil, bilməyiniz +dur)

# 6.İki ədədin bir-birinə bölünməsindən alınan qalığı 
# göstərən operatoru qeyd edin.
# %

# 7.Boş bir set tipli dəyişəni necə yarada bilərik ?
# myset = set()

# 8.Tuple-ların list-lərdən fərqli cəhətləri nədir?
# listler deyishile bilir ve dublikat qebul edir.
# tuple ise unchengeable .
# 9.Dictionary-lərdə yeni bir key,value cütünü necə əlavə
# edirik ? 
# mydict.update("key": "value")
# 10. Set tipini digər tiplərdən fərqləndirən əsas 
# cəhətləri sadalayın.
# tekrar qebul etmir
# 11. Set, str, tuple, list, dict – bunlardan hansılar 
# dəyişdirilməyəndirlər ?(UNCHANGABLE)


# 12.   *Daxil edilən ədəddə tək rəqəmlərin sayı 
# çoxdursa “Təklər qalib gəldi”. Cütlərin sayı çoxdursa 
# “Cütlər qalib gəldi” yazısını ekrana çıxarın.
# num = input("ededleri daxil edin:")

# cut_list = []
# tek_list = []

# cutler = 0
# tekler = 0

# for i in num:
#     if int(i) % 2 == 0:
#         cutler += 1
#         cut_list.append(int(i))
#     else:
#         tekler += 1
#         tek_list.append(int(i))

# if cutler > tekler:
#     print("cutler qalib geldi: ", cut_list)
# elif cutler == tekler:
#     print("beraber hal..") 
# else:
#     print("tekler qalib geldi: ",tek_list)


#
# 13. While dövr operatoru haqqında qısa məlumat 
# verin və bu dövr operatoru ilə kiçik bir tuple-nın 
# elementlərini ekrana çap edin

# mytuplu = ("alma","nar","gilas")
# i = 0
# while i < len(mytuplu):
        #  print(mytuplu[i])
        #  i = i + 1
# eded1 = input("ededi daxil edin:" )
# eded2 = input("ededi daxil edin:" )
# def hasil(eded1,eded2):
#     return eded1*eded2
# print(hasil(eded1,eded2))

# soz = input("sozu daxil edin:" )
# def len_soz(soz):
#     return len(soz)
# print(len_soz(soz))

# eded = input("ededi daxil edin:" )
# def reverse_num(eded):
#     return eded[::-1]
#     return reversed(eded)
# print(reverse_num(eded))

# eded = input("ededi daxil edin:" )
# def boyuk_eded(eded):
#     if eded %2 == 0:
#         return "cutdur" 
#     else:
#         return "tekdir"

# user_list= input("ededi daxil edin:" ).split()
# def print_list(user_list):
#         for i in user_list:
#                 print(i)
# print(print_list(user_list))

# my_list= input("ededi daxil edin:" ).split()
# def sum_list(my_list):
#     return int(sum(my_list))
# print(sum_list(my_list))

# user_list= input("ededi daxil edin:" ).split()
# def print_list(user_list):
#         for i in user_list:
#                 user_list=list(map(int,user_list))
#                 print(i)
# print(print_list(user_list))

# 1. Daxil edilen cumlede sait herflerin sayini qaytaran funksiya yazin.
# cumle = input("cumleni daxil edin:")
# saitler_r = ("a","i","o","u")
# def saitler(cumle):
#     cem = 0
#     for i in cumle:
#         for j in saitler_r:
#          if i == j:
#             cem+=1
#     return cem
# print(saitler(cumle))
    

# 2. Daxil edilen ededin reqemleri cemini qaytaran funksiya yazin.

# ededler = input("ededleri daxil edin: ")
# def cem(ededler):
#     cem1 = 0
#     for i in ededler:
#      cem1=cem1+int(i)
#     return cem1
# print(cem(ededler)) 


# 3. Daxil edilen ededin sade yaxud murekkeb oldugunu teyin eden funksiya yazin.
# eded = int(input("ededleri daxil edin: "))
# def sade_murekkeb(eded):
#   if eded % 2 == 1:
#     return "tekdir",eded
#   else:
#     return "cutdur",eded
# print(sade_murekkeb(eded))
            
# 4. Ededin polindrom olub olmadigini yoxlayan funksiya yazin.
# (Polindrom --> 77, 121, 212: terside ozune beraber olan)

# eded = input("ededi daxil edin: ") 
# def polindom(eded):
#     if eded==eded[::-1]:
#         return "eded polindom ededdir",eded
#     return "eded polindom eded deyil",eded
# print(polindom(eded))

# 5. Istifaciden aldiginiz 2 eded arasinda olan cut ededleri cap eden funskiya yazin.

# eded = int(input("ededi daxil edin: "))
# eded1 = int(input("ededi daxil edin: "))
# def cut_ededler(eded,eded1):
#     for i in range(eded,eded1+1):
#         if i %2==0:
#          print(i)
# cut_ededler(eded,eded1)

# 6. Ededin reqemlerinin sayi cutdurse "Good", tekdirse "Bad" qaytaran funskiya yazin.

# eded = (input("ededi daxil edin: "))
# def good_bad(eded):
    
#     if len(eded)%2==0:
#         return "Good"
#     return "Bad"
# print(good_bad(eded))

# 7. Daxil edilen sozun son herfini 10 defe 
# ozu ile birlesdiren funksiya yazin.

# soz = input("Sozu daxil edin; ")

# def last_letter(word):
#     return word + 10 * word[-1] 

# print(last_letter(soz))

# 8. Daxil edilen sozun eger butun herflerini kicilden 
# ve boyuden funksiya yazin.



# 9. Istifadeci istenilen sayda eded daxil ede biler, hemin ededlerin cemini qaytaran funksiya yazin.
# 10. Ele bir funksiya yazin ki, parol = "Estoniya" olsun.
#  Ve istifadeci bu parolu tapana qeder proqram dayanmasin.

# def find_password():
#     parol = "Estoniya"   
#     while True:
#         password = input("Parolu daxil et: ")

#         if password.lower() == parol.lower(): 
#             print("Siz tapdiniz")
#             break

# find_password()

# 11. Daxil edilen cumleni bir str tipi kimi
#  birlesdirib yeniden "i" herfine gore bolen bir funksiya yazin.


# 12. Daxil edilen ededin Armstronq olub olmadigini yoxlayan 
# funksiya yazin.
# (Armstronq - meselen 153 -- > 1^3 + 5^3 + 3^3 = 153).
# funksiya yazin.

# soz = input("Sozu daxil edin; ")

# def last_letter(word):
#     return word + 10 * word[-1] 

# print(last_letter(soz))

# 8. Daxil edilen sozun (eger) butun herflerini kicilden ve
# boyuden funksiya yazin.

# soz = input("sozu daxil edin: ")

# def upper_word(soz):
#         return soz.upper()
# print(upper_word(soz))


# soz = input("sozu daxil edin: ")

# def lower_word(soz):
#         return soz.lower()
# print(lower_word(soz))

# 9. Istifadeci istenilen sayda eded daxil ede biler,
# hemin ededlerin cemini qaytaran funksiya yazin.
 
# eded = input("ededleri daxil edin: ").split()
# eded = list(map(int,eded))
# def sum_eded(eded):
  
#   return int(sum(eded))
# print(sum_eded(eded))

# 10. Ele bir funksiya yazin ki, parol = "Estoniya" olsun.
# Ve istifadeci bu paroltapana qeder proqram dayanmasin.


# 11. Daxil edilen cumleni bir str tipi kimi birlesdirib 
# yeniden "i" herfine gore bolen bir funksiya yazin.


# cumle = input("Cumleni daxil edin : ")
# Salam necesiz ne var ne yox -- > ['Salam', 'necesiz', ...]

# def myfunc(sentence):
#     sentence = sentence.split()
#     sentence = "".join(sentence) # Salamnecesiznevarneyox
#     sentence = sentence.split("i")
#     return sentence

# print(myfunc(cumle))


# def myfunc():
#     return 4 + 5

# print(myfunc())

# 12. Daxil edilen ededin Armstronq olub olmadigini yoxlayan 
# funksiya yazin.
# (Armstronq - meselen 153 -- > 1^3 + 5^3 + 3^3 = 153).

# num1 = input("ededleri daxil edin:")

# def armstronq(num1):
#         num2 = 0
#         for i in num1:
#                 num2 = num2+int(i)**3
#         if int(num1) == num2:
#                 return "Eded Armstronqdur"
#         else:
#                 return "Eded Armstronq deyil "
# print(armstronq(num1))

# 13. Daxil edilen ededden 100 vahid geride ve 100 vahid 
# irelide duran cut ededleri bir list-e elave eden funksiya yazin.

# eded = int(input("ededi daxil edin: "))

# def myfunc(number):
#     newlist = []
#     if number > 100:
#         for i in range(number - 100, number + 101):
#             if i % 2 == 0:
#                 newlist.append(i)
#     print(newlist)

# myfunc(eded)

             
# 14.Ededin faktorialini tapan funksiya yazin. 
# (Faktorial --> 1den hemin edede qeder ededlerin hasilidir.)

# eded =  int(input("ededleri daxil edin: "))
# def myfunc(eded):
#     hasil = 1
#     for i in range(1,eded+1):
#         hasil = hasil*i
#     return hasil
# print(myfunc(eded))
        
# 15. Istifadecinin daxil etdiyi sozde a herfini i herfi
# ile evez eden funskiya yazin.
         

# soz =  input("sozu daxil edin: ")
# def my_func(soz):          
#     soz = soz.replace("a","i")
#     return soz
# print(my_func(soz))

# 16. Daxil edilen sozde boyuk herflerin sayini qaytaran
# funksiya yazi.
# soz =  input("sozu daxil edin:")
# def myfunc(soz):
#     saygac  = 0
#     for i in soz:
#         if i == i.upper():
#             saygac = saygac+1
#     return saygac  
# print(myfunc(soz))     
            
           

# 17. Daxil edilen cumlede icerisinde @ isaresi olan 
# sozlerin sayini qaytaran funksiya yazin.
    
# soz =  input("sozu daxil edin:")
# def myfunc(soz):
#     saygac = 0
#     for i in soz:
#         if i == "@":
#             saygac = saygac + 1
#     return saygac
# print(myfunc(soz))

# 1. İstifadəçinin daxil etdiyi cümlədə "*" işarələrinin
# sayını tapan funksiya yazın.

# cumle = input("cumleni daxil edin: ")
# def find_simvol(cumle):
#     saygac = 0
#     for i in cumle:
#         if i == "*":
#             saygac = saygac +1 
#     return saygac
# print(find_simvol(cumle))


# 2. mydict = {
#         '1': 'Lesson',
#         '2': 'Lesson2',
#         '3': 'Lesson3',
# }
# myNewdict = {}
# Bu dictionary-nin elementlərini dövr operatoru vasitəsilə
# myNewdict-ə əlavə edən funksiya yazın.

# mydict = {
#         1: 'Lesson',
#         2: 'Lesson2',
#         3: 'Lesson3',
# }

# myNewdict = {}


# for key in mydict.keys(): #[1,2,3]
#     for value in mydict.values(): #[Lesson, Lesson2, Lesson3]
#         myNewdict.update({key:value})
# print(myNewdict)


# 3. *args və **kwargs nədir ?



# 4. İstifadəçi float tip bir ədəd daxil edəcək. 
# Bu ədddə vergüldən sonrakı hissənin rəqəmlərini bir
# list-ə əlavə edən funksiya yazın.

 # eded = float(input("Ededi daxil edin: ")) # 8.55786 -- > '8.55786' --> ['8', '55786']

# def myfunc(eded):
#     newlist = []
#     str_eded = str(eded).split(".")
#     second_part = str_eded[1]
#     for i in second_part:
#         newlist.append(i)
#     newlist = list(map(int, newlist))
#     return newlist
# print(myfunc(eded))
# #8.5

# 5. Daxil edilən sözdə ə, ı, ü, ş, ç, ğ olduğu zaman onları 
# ingilis hərfi ilə əvəz edən funksiya yazın.

# soz = input("Sozu daxil edin: ")

# def myfunc(soz):
#     for i in range(len(soz)): #salam -- >  for i in soz: 
#         if soz[i] == 'ə':
#             soz = soz.replace(soz[i], "a")
        
#         if soz[i] == "ü":
#             soz = soz.replace(soz[i], "u")
           
#     return soz


# print(myfunc(soz))
# soz = input("sozu daxil edin: ") # əleykim
# mylist = []
# az_elifba = ['ə','ü', 'ı', 'ğ', 'ö', 'ç', 'ş']

# for i in range(97,123):
#     mylist.append(chr(i))
# print(mylist)
# for i in soz:
#     if i in az_elifba:
#         if i == 'ə':
#             soz = soz.replace(i, 'a')
#         if i == 'ü':
#             soz = soz.replace(i, 'u')
#         if i == 'ı':
#             soz = soz.replace(i, 'i')
# print(soz)
# 6. myls = [[25,45],['salam', 'sagol'],[1,1,False]]
# list-nin elementlərini çap edən funksiya yazın.


# myls = [[25,45],['salam', 'sagol'],[1,1,False]]
# for i in myls:
#     for j in i:
#         print(j)

# 7. İstifadəçi 2 ədəd daxil edəcək, o ədədlərdən hansı 
# böyükdürsə onun sadəliyini yoxlayıb qaytaran funksiya yazın

# eded1 = input("ededi daxil edin: ")
# eded2 = input("ededi daxil edin: ")>>


 
   



           
# 1. Birinci python kodu vasitəsilə bir test.txt 
# faylı yaradın. Daha sonra python kodu vasitəsilə
# içinə bu şəkildə:
# Salam
# Əsas
# İndidir
# sözləri yazılsın. Və burada i hərfinin sayını
# tapın.

# with open("test1.txt", "r+") as file1:
   
#     file1.write("\nsalam""\nesas""\nindidir") 
#     print(file1.readlines())
# file1 = open("test1.txt")
# with open("test1.txt","r") as file1:
#  cem = 0
#  mystr = "".join(file1.readlines())
#  for i in mystr:
#   if i == "i":
#    cem = cem + 1
# print(cem)

# 2. Daxil edilən cümlənin özündə deyil,
#  hər bir sözündə təkrarlanan hərfləri silən
# funskiya yazın. Məsələn cümlə belədirsə:
# Salam dərsimiz başladı --> Salm dərsimz başldı
# bu şəkildə olmalıdır.

# soz = input("sozu daxil edin: ")
# def tekrar(soz):
#   for i in soz:
#    set?

# 3. Daxil edilən ədədin sadəliyini yoxlayan 
# funksiya yazın (əvvəlki misallara baxmayın,
#  özünüz yazmağa cəhd edin, sadə ədəd yalnız 
#  1ə və özünə bölünən ədəddir).



# 4. Daxil edilən 2 ədədin cəminin fərqindən
# neçə dəfə böyük olduğunu qaytaran funksiya yazın.


# 5. Elə bir funksiya yazın ki, test.txt 
# faylında olan böyük hərfləri bir newlist-ə
# əlavə etsin.

# with open("test1.txt", "r+") as file1:
#     print(file1.readlines())
#     file1.write("\nSalam""\nEsas""\nIndidir")
  


# 6. 2lik və 10luq say sistemlərini araşdırın.
# 2lik say sistemindən 10 luq say sisteminə
# necə keçirilir və 10luq say sistemindən 
# 2lik say sisteminə necə keçirilir.
# Bunu tam dərk etdikdən sonra istifadəçidən aldığınız ədədi 2lik say sisteminə keçirən funskiya yazmağa cəhd edin.


# 7. Kalkulyator funksiyası yazın.
# 2 ədəd üçün nəzərdə tutulsun.
# Bütün əməliyyatları etmək mümkün olsun.

# num1 = int(input("ededi daxil edin"))
# num2 = int(input("ededi daxil edin"))
# def add(num1, num2):
#     return num1+num2
# def subtract(num1, num2):
#     return num1 - num2
# def multiply(num1, num2):
#     return num1*num2
# def divide(num1, num2):
#     return num1 / num2
# print(add(num1,num2))
# print(subtract(num1,num2))
# print(multiply(num1,num2))
# print(divide(num1,num2))



# 8. while dövr operatoru vasitəsilə ədədin 
# sadə olub-olmadığını yoxlayan proqram yazın.
# mylist = input("ededi daxil edin: ")
# i = 0
# while i < len(mylist):
#         if int(mylist[i]) % 2 == 1:
#             print("eded tekdir")
#         else:
#               print("eded cutdur")
#         i = i + 1

# 9. bir list yaradın və içinə ədədlər əlavə edin.
# (minimum 5 ədəd olsun içində)
# Daha sonra bu ədədləri istifadəçiyə göstərin,
# istifadəçi bir ədəd təxmin edəcək, daha sonra
# siz random modulundan istifadə edərək, 
# bu list-dən bir ədəd çıxarın, əgər həmin 
# ədəd istifadəçinin təxmin etdiyi ədədə 
# bərabərdirsə, "siz qazandınız", 
# əks halda "məğlub oldunuz" çap olunsun.

# import random
# list1 = [1, 2, 3, 4, 5, 6]
# print(list1)
# deyisen = random.choice(list1)

# print(deyisen)

# user = int(input("ededi daxil edin"))
# if user == deyisen:
#     print("siz qazandınız")
# else:
#     print("məğlub oldunuz")

# 10. İstifadəçi boşluqla istədiyi qədər ədəd
# daxil edə bilər, bu ədədlərdən neçəsinin cüt
# olduğunu qaytaran funksiya yazın.

# user = input("ededleri daxil edin: ").split()
# def cutsayi(newlist):
#   newlist = list(map(int, newlist))
#   count = 0
#   for i in newlist:
#    if i % 2 == 0:
#         count = count+1 
#   return count
                        
# print(cutsayi(user))

# 1. Daxil edilən sözdə təkrarlanan hərfi
# yeni bir list-ə əlavə edən funskiya yazın.

# 2. İstənilən sayda daxil edilən ədədin ədədi
# ortaslnı hesablayan funskiya yazın.

# nums = input("Ededleri daxil edin : ").split()


# 3. Daxil edilən ədədin rəqəmlərindən 
# cüt olanlarını cut_list=[] -ə,
# tək olanlarını isə tek_list=[]- ə əlavə edin.

# num =  input("ededleri daxil edin: ")
# cut_list = []
# tek_list = []

# cutler = 0
# tekler = 0

# for i in num:
#     if int(i) % 2 == 0:
#         cutler += 1
#         cut_list.append(int(i))
#     else:
#         tekler += 1
#         tek_list.append(int(i))
# print(cut_list)
# print(tek_list)

#  

# 4. Daxil edilən sözün hərflərinin ASCİİ
# əlifbasındakı dəyərlərini bir list-ə əlavə
# edən funskiya yazın.
# soz = input("sozu daxil edin:" )
# mylist = []
# for i in soz:
#  mylist.append(ord(i))
# print(mylist)
    

# 5. İstifadəçi bir sətrdə boşluqlarla ədədlər
# daxil edəcək və ASCİİ dəyərlərinə uyğun gələn 
# hərf və simvolları birləşmiş bir str tip dəyər
# şəklində return edən funskiya yazın.

# soz = input("sozu daxil edin:" ).split()
# soz = list(map(int,soz))
# mystr = ""
# for i in soz:
#     mystr+=chr(i)
# print(mystr) tekrar et !!!
    

# 6. Sözdə böyük hərflərin və kiçik hərflərin 
# sayını qaytaran funskiya yazın.

# soz =  input("sozu daxil edin:")
# def myfunc(soz):
#     saygac  = 0
#     saygac1 = 0
#     for i in soz:
#         if i == i.upper():
#             saygac = saygac+1
#         if i == i.lower():
#              saygac1 = saygac1+1
#     return saygac , saygac1 
# print(myfunc(soz))   

# 7. Daxil edilən cümlənin uzunluğu cütdürsə,
# cümləni boşluqlara görə ayrııb list-ə
# əlavə edən, Təkdirsə,  vergüllərə
# görə ayıran funksiya yazın.

# soz  = input("cumleni daxil edin: ")

# def myfun(soz):
#   if len(soz) % 2 == 0:
#         soz = soz.split()
#   else:
#         soz = soz.split(",")
#   return soz
# print(myfun(soz))

# 8. Bir dict yaradın və içərisinə key, 
# value cütü kimi 5 ölkənin ad və 
# paytaxtını qeyd edin. Daha sonra 
# key-i A ilə başlayan cütləri qaytaran bir
# funskiya yazın.

# mydict = {
#         "Azerbaycan": "Baku",
#         "Turkiye": "Ankara",
#         "Estoniya": "Tallin",
#         "  Rasiyya": "Moskva",
# }
# def myfunc():
#   mylist = []
#   for key in mydict.keys():
#     if key.startswith("A"):
#       mylist.extend([key,mydict[key]])
#   return mylist         
# print(myfunc())


# 9. Üçbucaq, kvadrat, çevrə. Bunların sahəsini
# hesablayan funskiya yazın. Məsələn, funksiya 
# işə düşdükdə bu 3 fiqurun adları görünsün.
# Hər hansı biri seçilərsə, ona uyğun sahəni
# hesablamaq üçün parametrlər soruşulsun və
# nəticə hesablanıb return edilsin. +

# 10. num dəyərinə random bir ədəd 
# mənimsədin(1,100 aralığından).
# Və daha sonra istifadəçidən o ədədi 
# tapmasını tələb edin, ədəddən yuxarı 
# deyilərsə aşağı düş, aşağı deyilərsə
# yuxarı qalx yazısı çap olunsun. 
# Tapdıqda təbriklər çap olunsun. 
# Bunlar baş verərkən proqram dayanmasın.


# 1. Daxil edilen ededin reqemleri cemini 
# qaytaran funksiya yazin.

# eded = input("ededleri daxil edin: ")
# def sum_eded(eded):
#   cem = 0
#   for i in eded:
#     cem+=int(i) 
#   return cem
# print(sum_eded(eded)) tekar et!!

# 2. Istifadeciden muxtelif deyerler alin 
# ve bir list-de olsun bu deyerler. 
# Daha sonra bu deyerler eded olanlari 
# bir ayri bir list-e yigin. 
# Daha sonra bu ededler olan listden cut 
# ededleri ayri bir list-e yigan funskiya yazin.

# mylist = input("deyerleri daxil edin:").split()
# print(mylist)
# newlist = mylist
# newlist1 = []
# newlist2 = []
# print(mylist)
# for i in newlist:
#         if i.isdigit():
#          newlist1.append(i)
# newlist1 = list(map(int, newlist1))
# for j in newlist1:
#             if j % 2 == 0: 
#              newlist2.append(j) 
# print(newlist2)
       


# 3. Daxil edilen cumlede sozlerin butun 
# herflerini boyuden funksiya yazin.

# soz = input("sozu daxil edin: ")
# def upper_word(soz):
#         return soz.upper()
# print(upper_word(soz))


# 4. Istifadeci bir eded daxil edecek. 
# Ferz edekki murekkeb eded olacaq
# (yeni yalniz 1-e ve ozune bolunmeyecek,
#   basqa ededlere de bolunecek).  
# Eger bu ededin bolenlerinin sayi 
# 2den coxdursa, onu return etsin 
# eks halda None return etsin.


      
# 5. Vurma emeliyyatini for dovr 
# opeartoru vasitesile yazmaga cehd edin. 
# (funksiya seklinde yazin)

    

# 6. Istifadeci bir setrde ad,soyad,ata adi, 
# yas, yasadigi seher qeyd edecek.
# Siz bu deyerleri bir dict-e elave eden
# funksiya yazin.
# Mes; {ad: Intigam, soyad:Guluzade...}
# ad = input("adinizi daxil edin ")
# print(ad)
# soyad = input("soyadinizi daxil edin ")
# print(soyad)
# ataadi = input("atanizin adini daxil edin ")
# print(ataadi)
# yash = int(input("yashinizi daxil edin "))
# print(yash)
# sheher = input("sheradini daxil edin ")
# print(sheher)
# def melumatlar(ad,soyad,ataadi,yash,sheher):
#    mydic = {}
#    mydic.update({
#       "ad":ad,
#       "soyad":soyad,
#       "yash":yash,
#       "ataadi":ataadi,
#       "sheher":sheher
#    })
#    return mydic
# print(melumatlar(ad,soyad,ataadi,yash,sheher))
# 7. Istifadecinin daxil etdiyi
# 2 eded arasinda olan sade ededleri
# bir list-e elave eden funskiya yazin 
# (tekrar tapsiriq)
# eded1 = int(input("eded-1:"))
# eded2 = int(input("eded-2:"))
# def sade_eded(eded1,eded2):
#   new_list =[]
#   new_list1 = []
#   for i in range(eded1,eded2):
#      for j in range(2,i):
#        if i % j == 0:
#          new_list.append(i)
#          break
#      else:
#       new_list1.append(i)
#   return new_list,new_list1
# print(sade_eded(eded1,eded2))

# 8. Ele bir funksiya yazın ki, 
# test.txt faylında olan böyük hərfləri 
# bir newlist-ə əlavə etsin.
# with open("test1.txt", "r+") as file1:
#     print(file1.readlines())
#     file1.write("\nSalam""\nEsas""\nIndidir")
  
# with open("test1.txt","r+") as file1:
#     new = file1.readlines()
# newlist = []
# for i in "".join(new):
 
#  if i == i.upper():
#         newlist.append(i)
# print(newlist)


# 9. while dövr operatoru vasitəsilə
#  ədədin sadə olub-olmadığını yoxlayan
#  proqram yazın.

# 1. Daxil edilen ededlerin icerisinden 
# en boyuk ve en kiciyinin ferqini qaytaran
# funksiya yazin.
# mylist = input("ededleri daxil edin: ").split()
# newlist = [] 
# newlist1 = []
# mystr=()
# def myfunc(mylist):
#  mylist = list(map(int, mylist))
#  mylist.sort()
#  return mylist[-1]- mylist[0]
# print(myfunc(mylist))


# 2. Daxil edilen cumlenin icinde bosluqlarin 
# sayini tapan funskiya yazin.
# soz = input("sozu daxil edin: ")
# print(soz)
# x = soz.count(" ")
# print(x)  

# 3. Daxil edilen ededler arasindan armstronq
#  olanlarini bir list-e elave eden funksiya
# yazin.(Armstronq -- > 153 = 1^3 + 5^3 + 3^3)
# nums =input("ededleri daxil edin:")
# cem = 0
# for i in nums: 
#   cem = cem + int(i)**3
# if int(nums) == cem:
#   print("armstromqdur")
# else:
#   print("armstromq deyil")
  

# 4. Istifadeci muxtelif herfler daxil edecek 
# ve bu herflerden random sozler duzelden
# funksiya yazin.


# 5. Istifadeci 3 eded daxil edecek,
#  bu ededleri str tipinde birlesdirin
# ve birlesdirdikden sonra reqemlerden
# en boyuyunu qaytaran funksiya yazin.
# eded1 = input("ededleri daxil edin:")
# eded2 = input("ededleri daxil edin:")
# eded3 = input("ededleri daxil edin:")

# eded =eded1+eded2+eded3
# newlist = []
# for i in eded:
#     newlist.append(i)
# newlist=list(map(int,newlist))
# newlist.sort()
# print(newlist[-1])


# 6. mytuple = ('salam')
# for dovr operatoru ile bu deyisenin 
# icine girin ve ne cap eleyeceyini onceden
# texmin edin.
# mytuple = ("salam") 
# for i in mytuple:
#     print(i)


# Alinan neticeyle bagli fikirlerinizi bildirin.
# #WHILE TAPSIRIQLARI

# 1. Istifadeciden muxtelif herf 
# ve ededler alin, ve while ile ekrana cap edin.
# soz = input("daxil edin: ").split()
# i = 0
# while i < len(soz):
   
#     print(soz[i])

#     i = i +1

# 2. While dovr operatoru ile 
# 1,100 araliginda olan cut ededleri ekrana
# cap edin
# i =2
# while i < 100:
    
#     print(i)
#     i = i + 2

# 3. While dovr operatoru ile list-in
#  icinde eded tipe cevrile bilen deyerleri
# basqa bir list-e elave edin.
# mylist = ["2","a","d","1","9","f"]
# newlist = []
# i =0
# while i<len(mylist):
#     if mylist[i].isdigit():
#         newlist.append(mylist[i])
#     i = i+1
# print(newlist)

# 4. While dovr operatoru vasitesile 
# iki ededin hasilini hesablayin.


# 5. While dovr operatoru ile bir 
# list-in icinde olan butun ededlerin 
# cemini tapin.

# mylist = [1,3,5,6]
# cem = 0
# i =0
# while i <len(mylist):
#     cem = cem+mylist[i]
    
#     i = i+1
# print(cem)


# 6. While dovr operatoru vasitesile
#  ededin reqemleri cemini tapin.
# eded = input("ededleri daxil edin:")
# count = 0
# i = 0
# while i < len(eded):
#     count +=int(eded[i])
#     i = i+1
# print(count)

    

# 7. While dovr operatoru ile daxil
#  edilen 2 eded arasindaki tek ededleri
# ekrana cap edin.
   
# eded1 = int(input("ededi daxil edin:"))
# eded2 = int(input("ededi daxil edin:"))
# i = eded1
# while  i < eded2:
#     if i %2 == 1:
#         print("eded tekdir",i)
#     else:
#         print("eded murekkebdir",i)

#     i = i+1 

# 10. Üçbucaq, kvadrat, çevrə. 
# Bunların sahəsini hesablayan funskiya yazın.
# Məsələn, funksiya işə düşdükdə bu 3 fiqurun
# adları görünsün. Hər hansı biri seçilərsə, 
# ona uyğun sahəni hesablamaq üçün parametrlər
# soruşulsun və nəticə hesablanıb return edilsin.

# eded1 = int(input("ededi daxil edin:"))
# eded2 = int(input("ededi daxil edin:"))
# hasil = 1
# i = eded1
# while i < eded2:
#   hasil = hasil *i
#   i = i+1
# print(hasil)




# 1. Daxil edilən ədədlərdən cüt olanları bir
# list-ə əlavə edin. Bunu while dövr operatoru ilə edin.

# eded =  input("ededleri daxil edin: ").split()
# new = []
# i = 0
# while i < len(eded):
#     if int(eded[i]) % 2 == 0:
#         new.append(eded[i])
#     i= i + 1
# print(new)


# 2. Daxil edilən ədədlərdən neçəsinin cüt olduğun tapın.
# (While dövr operatoru ilə)

# eded = input("ededleri daxil edin: ").split()
# count = 0
# i = 0
# while i < len(eded):
#     if int(eded[i]) % 2 == 0:
#         count+=1
#     i=i+1
# print(count)


# 3. Daxil edilən cümlədə boşluqların sayını tapın.
# (While dövr operatoru ilə)

# cumle = input("cumleni daxil edin: ")
# count = 0
# i = 0
# while i <len(cumle):
#     if cumle[i] == " ":
#         count+=1
#     i = i+1
# print(count) 

# 4. İstifadəçi müxtəlif sözlər daxil edəcək.
# Əgər istifadəçi daxil etdiyi söz "li" yaxud
# "zade" ilə bitərsə həmin sözləri bir soyad=[] list-inə
# əlavə edin. (While dövr operatorundan istifadə edin)

# soz = input("sozleri daxil edin:").split()
# print(soz)
# soyad = []
# i= 0
# while i < len(soz):
#     if soz[i][-1:-3:-1][-1::-1]=="li" or soz[i][-1:-5:-1][-1::-1]=="zade":
#         soyad.append(soz[i])
#     i+=1
# print(soyad)


# 5. İstifadəçi bir cümlə daxil edəcək.
# Və o cümlədə təkrarlanan sözü və yaxud 
# sözləri ekrana çap edin. (While dövr operatoru ilə)

# cumle = input("cumleni daxil edin:").split()
# count = 0
# i = 0
# while i< len(cumle):
#     if cumle.count(cumle[i])>1:
#         count+=1
#     i+=1
# print(count)
    

# 6. Daxil edilən ədədin rəqəmlərindən tək olanlarını çap edin.
# (While dövr operatoru ilə)

# eded1 = input("ededi daxil edin:")
# i = 0
# while  i < len(eded1):
#     if int(eded1[i]) % 2 == 1:
        
#         print("eded tekdir",eded1[i])
#     else:
#         print("eded murekkebdir",eded1[i])
#     i = i+1  

# 7. Daxil edilən cümlədə son 2 hərfi eyni olan 
# sözləri çap edin. (While dövr operatoru ilə)

# cumle = input("cumleni daxil edin:").split()
# i = 0
# while i<len(cumle):
#   if cumle[i][-1:-3:-1] == "**":
   
#    print(cumle[i])

#   i+=1

# 8. İstənilən sayda ədəd daxil edilə bilər. 
# Həmin ədədlərin ədədi ortasını tapın. 
# (Ədədi orta --> 2,3,4,5,15 --> (2+3+4+5+16)/5 = 6.0)
# (While dövr operatoru ilə)
# eded = input("ededleri daxil edin: ").split()
# cem = 0
# i = 0
# while i < len(eded):
#   cem+=int(eded[i])
#   i+=1
# netice = cem // len(eded) 
# print(netice)

    
# 9. Daxil edilən sözün hərflərinin ascii qarşılıqlarından
# hansı böyükdürsə, həmin o ASCİİ qarşlığı olan ədədi ekrana 
# çap edin. (While dövr operatoru ilə) yaz

# 10. İstifadəçi boşluqla hərflər daxil edəcək,
# əgər hərf böyükdürsə kiçildilmiş, kiçikdirsə 
# böyüdülmüş şəkildə list-ə əlavə olunacaq.
# (While dövr operatoru ilə)
# i= i.lower() yaz



# 11. Istifadecinin daxil etdiyi eded cutdurse, daha 
# sonra onun reqemlerinin sayi cutdurse, daha sonra 
# reqemlerinden sonuncusu cutdurse 
# ekrana "CUT UGURLU" yazdirin, eger tekdirse,
# daha sonra onun reqemlerinin sayi tekdirse, 
# daha sonra sonuncu reqemi tekdirse ekrana "TEK UGURLU" yazdirin.
# Diger butun hallar ucun "UGURSUZ" yazdirin. yaz
