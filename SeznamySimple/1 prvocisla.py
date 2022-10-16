a = int(input("Kolik chcete najít prvočísel"))

primes = [2]
counter = primes[0]+1

while len(primes) < a:
    for x in primes:
        if counter % x:
            continue
        else:
            break

    if x == primes[-1]:
        primes.append(counter)
    counter += 2

print(primes)
#pekne