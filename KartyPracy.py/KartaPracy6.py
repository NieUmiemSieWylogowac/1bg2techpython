#zad1
# a = int(input())
# b = int(input())
# c = int(input())

# if c - b == a:
#  print("Tak, jest to ciąg geometryczny")
#  print(a,b,c)
# else:
#   print("nie")

#zad 3

# for i in range(99,9,-1):
#   if i % 7 == 0:
#     podzielnik = 1
#     break

# ilosc = 0
# for i in range(1000, 10000):
#   if i % podzielnik == 0:
#     ilosc += 1
# print(ilosc)

#zad 4

ilosc=0
for i in range(10,100):
  cd = i // 10
  cj = i % 10
  if cd >= 2*cj:
    ilosc = ilosc + 1
print(ilosc)