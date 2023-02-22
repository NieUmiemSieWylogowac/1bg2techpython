#zad 1
# k = int(input())
# suma=0
#  for i in range(100, 100+k):
#   suma = suma+i
# print(suma)

#zad 2
# n = int(input())
# a, b = 0, 1
# suma = 0
# for i in range(n):
#   a, b = b, a+b
#   suma = suma+b
# print(suma)

n = int(input())
if n <=2:
  print("NIE")
else:
  for i in   range(2, n):
    if n % i == 0:
      print("NIE")
      break
    else:
      print("TAK")
      break
