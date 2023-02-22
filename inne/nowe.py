n = int(input())
if n <= 2:
  print ("NIE")
else:
  for i in range(2, n):
    if n % i == 0:
      print("NIE")
      break
    else:
      print("TAK")



