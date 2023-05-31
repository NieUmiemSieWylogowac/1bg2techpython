#Oblicz sumę liczb trzycyfrowych
# suma=0
# for i in range(100,999):
#  suma=suma + i
# print(suma)

#Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
# suma=0
# ilość=0
# for i in range(12,100,6):
#   suma = suma + i
#   ilość += 1
# print(suma)
# print(ilość)

# Znajdź największą liczbę pośród wylosowanych przez program liczb 4-cyfrowych

# import random


# najwieksza_liczba = 0


# ll_do_wylosowania = 5

# #Pętla losująca liczby i aktualizująca największą liczbę
# for _ in range(ll_do_wylosowania):
#   wylosowane_liczby = random.randint(1000, 9999)
#   print(wylosowane_liczby)
#   if wylosowane_liczby > najwieksza_liczba:
#     najwieksza_liczba = wylosowane_liczby


# print("Największa liczba to:", najwieksza_liczba)


#Podaj sumę cyfr w dowolnej liczbie
# liczba = int(input("Podaj liczbę"))
# sumacyfr = 0

# while liczba != 0:
#   cyfra = liczba % 10
#   sumacyfr += cyfra
#   liczba //= 10
# print("Suma cyfr wynosi",sumacyfr)

# Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
# liczba=input("Podaj TRZYCYFROWĄ liczbę: ")
# if len(liczba) == 3:
#    najmniejsza_cyfra = min(int(cyfra) for cyfra in liczba)
#    print("Najmniejsza cyfra to", najmniejsza_cyfra)
# else:
#    print("BŁĄD","Liczba ma więcej lub mniej niż 3 cyfry")

#ALGORYTMY
#Sprawdź czy wpisana przez usera liczba jest pierwsza
# liczba = int(input("Podaj liczbę"))
# if liczba <= 2:
#  print("Nie")
# else:
#  for i in range(2,liczba):
#    if liczba % i == 0:
#     print("Nie")
#     exit()
# print("Liczba jest liczbą pierwszą")

#Sprawdź czy wpisana przez usera liczba jest złożona
# liczba = int(input("Podaj liczbę"))
# if liczba <= 2:
#   print("Nie")
# else:
#    for i in range(2,liczba):
#      if liczba % i == 0:
#        print("Tak, liczba jest złożona")
#        break
#      else:
#       print("Nie")
#       break

#Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24

# a = int(input("Podaj liczbę"))
# b = 24
# from math import gcd
# if gcd(a,b) == 1:
#   print("Tak")
# else:
#   print("Nie")

# Zakoduj szyfrem cezara i kluczem k słowo s

# def szyfr_cezara(slowo, klucz):
#     zaszyfrowane_slowo = ""
#     for litera in slowo:
        
#         if litera.isupper():
#             pozycja = ord(litera) - ord('A')
#             nowa_pozycja = (pozycja + klucz) % 26
#             nowa_litera = chr(nowa_pozycja + ord('A'))
#             zaszyfrowane_slowo += nowa_litera
        
#         elif litera.islower():
#             pozycja = ord(litera) - ord('a')
#             nowa_pozycja = (pozycja + klucz) % 26
#             nowa_litera = chr(nowa_pozycja + ord('a'))
#             zaszyfrowane_slowo += nowa_litera
        
#         else:
#             zaszyfrowane_slowo += litera

#     return zaszyfrowane_slowo

# slowo = input("Wprowadź słowo: ")
# klucz = int(input("Wprowadź klucz k: "))
# zaszyfrowane_slowo = szyfr_cezara(slowo, klucz)
# print("Zaszyfrowane słowo:", zaszyfrowane_slowo)


#Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# x, y = b, d
# ilocz = x * y
# while y > 0:
#   x, y = y, x % y
# nww = ilocz // x

# e = (nww // b) * a
# f = (nww // d) * c
# licznik = e + f
# mianownik = nww

# # Ułamek nieskracalny 

# print(f"{a}/{b} + {c}/{d} = {licznik}/{mianownik}")

# from math import gcd
# nwd = gcd(licznik,mianownik)
# licznikskr = licznik//nwd
# mianownikskr = mianownik//nwd
# print("Po skróceniu ułamka wychodzi", f"{licznikskr} / {mianownikskr}")

# # Liczba mieszana 

# całkowita = licznik // nww
# reszta = licznik % nww
# print ("Liczba mieszana to", f"{całkowita} {reszta}/{nww}")


# Znajdź NWW dwóch wpisanych przez usera liczb
# # Modulo
# a, b = int(input()), int(input())
# iloczyn = a * b
# while b > 0:
#     a, b = b, a%b
# nwd = a
# print(iloczyn // nwd)

# # Odejmowanie
# a, b = int(input()), int(input())
# iloczyn = a * b
# while a != b:
#     if a > b : a = a - b
#     if b > a : b = b - a
# nwd = a
# print(iloczyn // nwd)

# Znajdź ilość liter C we wpisanym napisie
# napis = input()
# ilosc = 0
# ilosc = napis.count("C")
# print(ilosc)

# Sprawdź czy literki w napisie są w porządku nierosnącym

# napis = input()
# for i in range(len(napis)):
#   if napis[i+1]<napis[i]:
#     print("TAK")
#     break
#   else:
#     print("NIE")
#     break

# Podaj najdłuższy z 3 wpisanych przez usera wyrazów
# a = input()
# b = input()
# c = input()
# if len(a) > len(b) and len(a) > len(c):
#   print("Najdłuższy wyraz to", a)
# else:
#   if len(b) > len(c):
#     print("Najdłuższy wyraz to", b)
#   else:
#     print("Najdłuszszy wyraz to", c)



    
                           
  


  
