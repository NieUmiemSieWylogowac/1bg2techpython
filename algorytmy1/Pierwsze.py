
# Sprawdź czy dana liczba jest pierwsza

# n=int(input())
# for i in range(2, n):
#   if n % i ==0:
#     print("Liczba nie jest pierwsza")
#     exit(0)

#2. Generowanie liczb pierwszych (w przedziale [p,q])

# p, q = int(input()), int(input())

# for j in range(p, q+1):
#   for i in range(2,n):
#     if j % i == 0:
#       flaga=False
#       break
#   if flaga=True:
#       print(i, end=" ")

#3.Generowanie liczb pierwszych (pierwsze n liczb pierwszych)

n = int(input("Ile chcesz liczb pierwszych"))

k=2
ilosc = 0
while 1:
  flaga = True
  for j in range(p, q+1):
   for i in range(2,n):
     if j % i == 0:
       flaga=False
       break
   if flaga=True:
       print(i, end=" ")

        