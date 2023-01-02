# Funkcja ord() - zwraca kod ascii danego znaku

# print(ord("A"))
# print(ord("B"))
# print(ord("X"))

# # Funkcja chr() - zwraca znak danego kodu ascii
# (print(chr(68))
# (print(chr(93))
# (print(chr(72))

# znaki ASCII od A-Z mają kody 65-90!

 #wypiszcie pętlą for cały alfabet A-ZeroDivisionError
# for i in range(65, 90):
#   print(chr(i), end=" ")

# jak słowo rozbić na litery?

# napis = "POLSKA"
# print(len(napis)) # zwraca długość napisu
# print(napis[0])   # napis to lista
# print(napis[1])
# print(napis[2])

# wypiszcie kody ASCII napisu POLSKA
# napis = "POLSKA"
# for i in range(len(napis)):
#   print(ord(napis[i]))

# wypiszcie kody ASCII literek napisu
for i in range(len(napis)):
  print( chr( ord(napis[i])+ 3))
 
 