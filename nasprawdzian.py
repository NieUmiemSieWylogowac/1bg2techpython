#Liczby pierwsze

#Czy liczba jest liczbą pierwszą
# n = int(input("Podaj liczbę"))
# if n <= 2:
#   print("NIE")
# else:
#   for i in range(2, n)
#   if n % i == 0:
#     print("NIE")
#     break
# else:
#   print("TAK")

# Podaj liczby pierwsze w zakresie od n do e
# n = int(input())
# e = int(input())
# for i in range(n,e+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end="")

#Podaj liczby pierwsze do wpisanej liczby
# n = int(input("Do ilu mam znaleźć liczby pierwsze?"))
# for i in range(2, n+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end=" ")

# NWD
# a = int(input())
# b = int(input())
# from math import gcd
# print(gcd(a,b))

# NWW
# a = int(input())
# b = int(input())
# from math import gcd
# iloczyn=a*b
# NWD=gcd(a,b)
# NWW=iloczyn//NWD
# print(NWW)

#ułamki dodawanie
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# from math import gcd
# x, y = b, d
# iloczyn = x*y
# nwd=gcd(x,y)
# nww=iloczyn//nwd
# e=(nww//b)*a
# f=(nww//d)*c
# g=e+f
# print(f"{g}/{nww}")

# Cezar
# napis=input()
# szyfr=" "
# for i in range(len(napis)):
#   szyfr=szyfr+chr(65+ ((ord(napis[i])-65+3)%26))
#   print(szyfr)