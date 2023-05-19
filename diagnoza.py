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
#   print("BŁĄD","Liczba ma więcej lub mniej niż 3 cyfry")

#ALGORYTMY
#Sprawdź czy wpisana przez usera liczba jest pierwsza
# liczba = int(input("Podaj liczbę"))
# if liczba <= 2:
#   print("Nie")
# else:
#   for i in range(2,liczba):
#     if liczba % i == 0:
#       print("Nie")
#       break
#     else:
#       print("Liczba jest liczbą pierwszą")
#       break

#Sprawdź czy wpisana przez usera liczba jest złożona
# liczba = int(input("Podaj liczbę"))
# if liczba == 2:
#   print("Tak, liczba jest złożona")
# else:
#   for i in range(2,liczba):
#     if liczba % i == 0:
#       print("Tak, liczba jest złożona")
#       break
#     else:
#       print("Nie")
#       break

#Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24

#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# number = int(input("Podaj liczbę: "))

# if gcd(number, 24) == 1:
#     print("Liczba jest względnie pierwsza z 24.")
# else:
#     print("Liczba nie jest względnie pierwsza z 24.")

#Moja wersja
# a = int(input("Podaj liczbę"))
# b = 24
# from math import gcd
# if gcd(a,b) == 1:
#   print("Tak")
# else:
#   print("Nie")

# 
