list = []
a = int(input("Zadejte jedno liché číslo "))
if int(a % 2 == 1):
  print("Toto je liché číslo")
  for num in range(a, a + 16):
    if num % 2 != 0:
      print(num)
      list.append(num)
elif int(a % 2 == 0):
  print("Toto je sudé číslo!")

print(list)
#je to dobre, chybi ale soucet