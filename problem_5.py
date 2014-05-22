import pdb

# def factors(num):
# 	prime = 2
# 	primes = [1]
# 	fin = False
# 	for item in primes:
# 		while num % prime != 0:
# 			prime += 1
# 		primes.append(prime)
# 		num = num / prime
# 		prime = 2
# 		for item in primes:
# 			if num == item:
# 				fin = True
# 		if fin is True:
# 			primes.append(num)
# 			break
# 	return primes

# def listfactors(start, end):
# 	allfactors = [1]
# 	for i in range(start, end):
# 		temp = factors(i)
# 		print temp
# 		for item in temp:
# 			if item != 1:
# 				allfactors.append(item)
# 	product = 1
# 	for obj in allfactors:
# 		product = product * obj

# listfactors(2, 11)


def multiples():
	i = 232792560
	found = False
	while not found:
		j = 11
		i+=232792560
		div=True
		print i
		for j in range(21,30):
			if (i%j==0):
				pass
			else:
				div=False
				break
		if div:
			found = True
	print i
	return i


def multiple():
	i = 2520
	found = False
	while not found:
		j = 11
		i+=2520
		div=True
		print i
		for j in range(11,20):
			if (i%j==0):
				pass
			else:
				div=False
				break
		if div:
			found = True
	print i
	return i

multiples()