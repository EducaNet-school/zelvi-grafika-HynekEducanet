seznam = [5,8,11,3,20,1]

for item in seznam:
    print(item)

for index in range(len(seznam)):
    print(seznam[index])

for index in range(len(seznam)):
    if seznam[index] == 20:
        print(index)

print(seznam[0])