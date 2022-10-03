def mojefunkce(e):
    return len(e)

auta = ["SAAB", "Volvo", "Mitsubishi", "Volkswagen", "BMW", "Mercedes-Benz", "Subaru", "Lancia"]

auta.sort(key=mojefunkce)

print(auta)