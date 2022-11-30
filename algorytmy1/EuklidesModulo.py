# a=int(input())
# b=int(input())
# while b > 0:
#   a,b = b,a, a%b



print("Obliczę NWW dwóch liczb")
a = int(input("Wpisz pierwszą liczbę"))
b = int(input("Wpisz drugą liczbę"))
iloczyn = a*b
while a !=b:
  if a > b : a = a - b
  if b > a : b = b - a
print(iloczyn // a)
nwd = a


