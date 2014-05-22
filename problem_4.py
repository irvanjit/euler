def palindrome():
	a1 = []
	a2 = []
	p = []
	counter = 0
	for x in range(100, 1000):
		counter += 1
		a1.append(x)
		a2.append(x)
	for i in a1:
		for j in a2:
			num = str(a1[i-100] * a2[j-100])
			match1 = match2 = 0
			if len(num) % 2 == 0:
				for k in range(len(num)/2):
					if num[k] == num[(len(num)-1)-k]:
						match1 += 1
				if match1 == len(num)/2:
					p.append(int(num))
			else:
				for m in range((len(num)-1) /2):
					if num[m] == num[(len(num)-1)-m]:
						match2 += 1
				if match2 == (len(num)-1)/2:
					p.append(int(num))
	ans = sorted(p)
	print ans
palindrome()