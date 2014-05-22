def primefactors():
	primes = []
	for i in range(13195):
		if (i > 2) and (600851475143 % i == 0):
			p = 0
			for j in range(i+1):
				if j > 0:
					if i % j == 0:
						p += 1
			if p == 2:
				primes.append(i)
	print primes

primefactors()


