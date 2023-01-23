#PendingDeprecationWarning

# pętla liczb dwucyfrowych od 10 do 21
# for i in range(10, 22):
#   print(i, end=" ")

# pętla liczb dwucyfrowych nieparzystych od 15 do 31
  # for i in range(15,33,2):
  #   print(i, end=" ")

# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1):
#   print(i, end=" ")

#pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,100,1):
#   print(109-i, end=" ")
#pętla liczb 3-cyfrowych podzielnych przez 20
# for i in range(100, 1000, 20): print(i, end=" ")
#   print()
# for i in range(5, 50) : print(20*i, end=" ")

# zad 1
# n = int(input())
# for i in range(n):
#   print(i**3 + 3, end=" ")

# zad 2
# for i in range(105,1000,15):
#   print(105-i , end=" ")

# PRE 2

# Pętle for liczb trzycyfrowych podzielnych przez 13
# for i in range(104, 999, 13): print(i, end=" ")


# Pętle for liczb dwycfrowych parzystych
# for i in range(10,99,2):
#   print(i, end=" ")


# Pętle for potęg cyfr 0, 1, 4, 9, 16 .. 81
# for i in range(10):
#   print(i**2, end=" ")

  # zad 4
# suma = 0
# for i in range(10,100):
#   suma = suma + i # 0 + 10 + 11 + 12 + 13 + .... + 99
# print(suma)

# DOD - suma liczb trzycyfrowych parzystych
# suma = 0
# for i in range(100,1000,2):
#   suma = suma + i # 100 + 102 + 104 + 106  + .... + 998
# print(suma)

#zad 5
# n = int(input())
# suma = n * (n+1) // 2

# for i in range(n-1):
#   k = int(input())
#   suma = suma - k
# print("Nie podałeś: " suma)

#zad 6

n = int(input())
a, b = 0, 1

for i in range(n):
  a, b = b, a + b
  print(a, end=" ")