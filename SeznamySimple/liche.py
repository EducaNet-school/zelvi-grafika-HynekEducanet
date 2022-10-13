import random
list = []
a = int(input("Zadejte jedno liché číslo"))
if int(a % 2 == 1):
    for i in range(8):
       ele = print(a + random.randrange(1,8,2))
    print("Toto je liché číslo")