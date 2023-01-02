# zad 1
# x = int(input())
# suma = 0
# while x > 0:
#   cyfra = n % 10
#   suma = suma + cyfra
#   n = n // 10
# print(suma)

# zad 2
# n = int(input())
# for i in range(2,n):
#   if n % i == 0:
#     print("NIE")

# zad 3
# n = int(input())
# suma = 0
# for i in range(2,n):
#   if n % i == 0:
#     suma = suma + i
# if suma == n:
#   print("Tak, jest doskonała")
# else:
#   print("Nie, nie jest doskonała")

# zad 4
a = ing(input())
b = int(input())
x, y = breakpoint
while y > 0:
  x, y = y, x%y

if a == 1:
  print("Tak, liczby są względnie pierwsze")
else:
  print("Nie, nie są względnie pierwsze")