# Anagramy
# anagramy np adam dama mada amda aamd

# a = input()
# b = input()
# X, Y = list(a), list(b)
# X.sort()
# Y.sort()
# a = "".join(X)
# b = "".join(Y)
# print(a,b)
# if a == b:
#     print("TAK")
# else:
#     print("NIE")

# Palindromy


# s = input()
# L = list(s)
# R = L.copy()  # R = list(s)
# R.reverse()
# if L == R:
#     print("TAK")
# else:
#     print("NIE")

# palindrom ver 2
# s = input()
# for i in range(len(s)//2):
#     if s[i] != s[len(s)-1-i]:
#         exit("NIE")
# exit("TAK")

# Wydawanie reszty
# T = [50,20,10,5,2,1]
# T.sort(reverse=True)
# x = int(input("Reszta: "))
# for i in T:
#     ilość = x // i
#     if ilość > 0:
#         x = x - ilość * i
#         print(f"{ilość} razy {i}")

# b = input()
# for i in range(1, len(b)-1):
#   print(b[i], end=" ")
# print()

# print(b[1:len(b)-1])

# L = list(b)
# L.pop(0)
# L.pop(-1)
# b = "".join(L)
# print(b)

# d = input()
# s = 0
# for x in d:
#   s += ord(x)
# znak = s // len(d)
# print(chr(znak))

# e = input()
# ilosc = 0
# for x in e:
#   if x=="a":
#     ilosc+=1
# print(ilosc)

# e = input()
# samo = ["a", "e", "i", "o", "u", "y"]
# ilosc_samo=0
# for x in e:
#   if x in samo:
#     ilosc_samo+=1
# print(ilosc_samo)

#Dominująca literka we wpisanym napisie
f = input()
maksiu=0
for x in f:
  if f.count(x)>maksiu:
    maksiu = f.count(x)
    literka=x
print(literka, maksiu)
