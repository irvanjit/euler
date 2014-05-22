# def addmultiples():
# 	runcount = 0
# 	ans = 0
# 	for i in range(1000):
# 		runcount += 1
# 		if (i % 3) == 0:
# 			ans += i
# 		elif (i % 5 ) ==0:
# 			ans += i
# 	print ans
# 	print runcount


# 534 total iterations
# def addmultiples(n):
# 	runcount = 0
# 	ans = 0
# 	i = 0
# 	j = 0

# 	while i < n:
# 		runcount += 1
# 		i += 3
# 		if (i < n):
# 			ans += i

# 	while j < n:
# 		runcount += 1
# 		j += 5
# 		if (j % 3 != 0) and (j < n):
# 			ans += j
# 	print ans
# 	print runcount

def addmultiples(n):
	def sumxdivby(p):
		r = n/p
		s = p*(0.5*r*(r+1))
		return s
	ans = sumxdivby(3) + sumxdivby(5) - sumxdivby(15)
	print ans
