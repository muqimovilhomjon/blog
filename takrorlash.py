#GUIDO van ROSSUM 1980 yillar oxiri
#pythonda malumot turlari asosiy 6ta
#int  butun sonlar
#float haqiqiy sonlar
#bool mantiqiy tip true yoki false   togri yoki notogri
#str yozuvli malumotlar uchun 
#list kop malumotlarni ozida saqlash uchun  [1,2,'salom]
#dict kop malumotlarni kalit sozlar bilan saqlash uchun {"ism":"botir"}
#  --------**-------  daraja belgisi

#from datetime import datetime
#today = datetime.now()
#print(today.strftime('%y-%m-%d'))



#narx = 3500.70
#soni = int(input('nechta non olasiz: '))
#natija = narx*soni
#print('summa: ',natija)



#a = int(input())
#b = int(input())
#print(b,a)



#from math import sqrt
#a = sqrt(25)
#print("a=",a)


#s = input('kiriting: ')
#format()  ikki so'zni birlashtiradi
#truncate long string     uzun bir so'zning qanchadir qismini chiqarish
#print('{:.5}'.format(s))   uzun bir so'zning qanchadir qismini chiqarish
#print('salom {}'.format(s))  ikki so'zni birlashtirib chiqaradi
#print(s.capitalize())  #so'zni birinchi harfini katta qiladi
#print(s.casefold()) #matndagi barcha sozni kichik harfda qiladi
#print(s.count('a'))   #berilgan gapda nechta soz yoki belgi qatnashganini aniqlaydi


#s = 'assalom'
#print(len(s)) #soz uzunligi
#print(s[2:])
#print(s[::-1].capitalize())

#inputdan ikkita soz oqib olinadi masalan ((salom dunyo)) shuni ((dunyo salom)) deb chiqarish kk
#a = input()
#print(a)


#shart operatorlari
#if ----------------------------> agar 
#elif---------------------------> aks holda agar
#else---------------------------> aks holda
#from random import randint
#a = randint(1,200)
#b = randint(1,200)

#c = int(input('{} + {} ='.format(a,b)))
#if c == (a+b):
#    print('togri')
#else:
#    print('wrong')

#HOMEWORK    

#a = int(input())
#if a % 4 == 0:
#    print('kabisa yili')
#else:
#    print('kabisa yili emas')


#python package  modul
#import math        #kutubxona matematik
#print(math.ceil(9.6))
#print(math.floor(9.6))


#ikki xil vaqt kiritiladi
#time1 = soat1,minut1,sekund1
#time2 = soat2,minut2,sekund2

#soat1 = int(input('soat1 '))
#minut1 = int(input('minut1 '))
#sekund1 = int(input('sekund1 '))

#soat2 = int(input('soat2 '))
#minut2 = int(input('minut2 '))
#sekund2 = int(input('sekund2 '))

#vaqt = (soat2-soat1)*3600+(minut2-minut1)*60+(sekund2-sekund1)
#print('farq ',vaqt)


#HOMEWORK
#3 xonali son inputdan oqib olinadi va uni raqamlari yigindisi topiladi masalan 685   6+8+5=19
#son = int(input())


#summa = input()
#if summa.isdigit() and int(summa)>0 and  int(summa)<100000000000:   # and---------> va degani 1*1*1=1  0*1*1=0  1*0*1=0  1*1*0=0
#    print('wonderfull')
#else:
#    print('one more time')


#name = input('ismingizni kiriting: ')
#surname = input('familyangizni kiriting: ')
#if name or surname:     # or-----> yoki degan manoda keladi name=0=false  surname=1=true  0+1=1   false+true=true
#    print('hello')
#else:
#    print('ism yoki familya kiriting')


# son kiritilganda uni soz bilan yozib beruvchi dastur masalan    1----->  bir
#son = input('1 dan 30 gacha son kiriting: ')
#if son.isdigit():
#        son = int(son)
#        if   son>0 and son<30:
#           qoldiq = son % 10
#           letter = ' '
#           if son>9 and son<20:
#            letter = 'on '
#           elif son>19 and son<30:
#            letter = 'yigirma '
#
#           if qoldiq==1:
#            letter +='bir'
#          elif qoldiq==2:
#          letter +='ikki'
#        elif qoldiq==3:
#         letter +='uch'       
#         elif qoldiq==4:
#           letter +='tort'
#          elif qoldiq==5:
#           letter +='besh'
#          elif qoldiq==6:
#           letter +='olti'
#          elif qoldiq==7:
#           letter +='yetti'
#          elif qoldiq==8:
#           letter +='sakkiz'
#          elif qoldiq==9:
#           letter +='toqqiz'
#          print(letter)
#       else:
#           print('now')
#else:
#       print('nowaday')          



#HOMEWORK   dasturga harf kiritilganda uni unli yoki undosh ekanligi aniqlansin 
#soz = input()


#range(1,31)     #1,2,3,4,5,6,7,.....,,30
#for son in range(1,32): 
#   print(son)

#karra = 8
#for son in range(1,11):
#    natija = karra * son
#    print('{} x {} = {}'.format(karra,son,natija))

a = int(input('tugilgan yilingizni kiriting: '))
c = 2021-a
print(f'siz {c} yoshdasiz')
