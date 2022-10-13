from re import A

list = []

a = int(input("Zadejte číslo od 2 do 10"))
if int(a < 10 and a > 2):
    for i in range (1, 11):
        print(a, "x", i, "=", a*i)
        list.append(a*i)
elif(a > 10):
    print("Číslo je větší než 10")
elif(a < 2):
    print("Číslo je menší než 2")

print(list)