from operator import index


sez = [5, 4, 3, 2, 1, 1, 1, 1, 1 , 3, 4, 5]

def prumer(sez):
    total = 0
    for n in sez:
        total += n
        print(total)