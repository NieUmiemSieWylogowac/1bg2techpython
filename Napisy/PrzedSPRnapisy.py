#1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
# napis = int(input())
# print(a[0], a[-1])

#2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# b = input()
# for i in range(1, len(b)-1):
#   print(b[i], end="")
# print()

# print(b[1:len(b)-1])

# L = list(b)
# l.pop(0)
# l.pop(-1)
# b ="".join(L)
# print(b)

#3. Waga napisu to suma kodow ascii jego liter. Zważ wpisany napis

# d = input()
# s = 0
# for x in d:
#   s += ord(x)
# znak = s // len(d)
# print(chr(znak))

#4. Policz ile we wpisanym napisie jest liter A.

# e = input()
# ilosc = 0
# for x in e:
#   if x == "A":
#     ilosc += 1
# print(ilosc)

# SAMO = ["A", "E", "I", "O", "U", "Y"]

# ilosc_samo = 0
# for x in e:
#   if x in SAMO:
#     ilosc_samo += 1
# print(ilosc_samo)

#5. Podaj dominującą literkę we wpisanym napisie

# f = input()
# maksiu = 0
# for x in f:
#   if f.count(x) > maksiu:
#       maksiu = f.count(x)
#       literka = x
# print(literka, maksiu)

#6. Sprawdź, czy w napisie występują trzy podciągi "LA"

h=input()
ilosc=0
for i in range(len(h)):
  if h[i:i+2] == "LA":
    ilosc += 1

# ZAGADNIENIA NA SPRAWDZIAN NAPISY
# - len for foreach ord chr
# - funkcje - sort-
# - indeksy, zakresy
# - konwersje list <-> napis
# - list - sort reverse
# - split, join
# - Algorytmy - anagram, palindrom, Boyer-Moore

