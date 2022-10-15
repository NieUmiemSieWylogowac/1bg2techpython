#zad 1
# a,b = int(input()),int(input())
# if (a + b) % 2 == 0:
#   print("TAK")
# else:
#   print("NIE")

#zad 2
# a=int(input())
# g=int(input())
# if (a+g%2)==(a*g):
#   print("TAK")
# else:
#   print("NIE")

#zad 3
# k=int(input())
# l=int(input())
# # m=int(input());
# if k==l:
#    print("TAK")
#    print("k,l")
#  else:
#    print("NIE")

# if l==m:
#   print("TAK")
#   print("l,m")
# else:
#   print("NIE")

# if m==k:
#   print("TAK")
#   print("m,k")
# else:
#   print("NIE")

#zad 4
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min(a,b,c,d))

#zad 5
# a = int(input())
# b = int(input())
# c = int(input())
# if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
#    print("tak")
# else:
#   print("nie")

#zad 6
a = int(input())
b = int(input())
c = int(input())

if c < (a + b) and c**2 < (a**2+b**2):
  print("TAK")
  print("Trójkąt ostrokątny")
else:
  print("NIE")


if c < (a + b) and c**2 == (a**2+b**2):
  print("TAK")
  print("Trójkąt prostokątny")
else:
  print("NIE")

  
if c < (a + b) and c**2 > (a**2+b**2):
  print("TAK")
  print("Trójkąt rozwartokątny")
else:
  print("NIE")
