seznam = [14, 2, 5, 99, 150, 15, 55, 44, 1, 77]
seznam[0] = 1

min = 50
index = -1
minindex = -1

for index in range(len(seznam)):
    index = index + 1
    print(index)

for item in seznam:
    index = index + 1
    if min > item:
        min = item
        minindex = index
        print(min,minindex)

for index in range(len(seznam)):
    if seznam[index] == 14

temp = seznam[0]
seznam[0] = min


for item in seznam:
    if min > item:
        min = item
        print(min)