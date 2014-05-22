# def fibonacci(lim):
# 	counter = 0
# 	sequence = [0, 1]
# 	t1 = 0
# 	t2 = 1
# 	while t2 < lim:
# 		counter += 1
# 		temp = t2
# 		t2 += t1
# 		t1 = temp
# 		if t2 < lim:
# 			counter += 1
# 			sequence.append(t2)
# 	return (sequence, counter)

# def evensum(lim):
# 	ans = 0
# 	seq = fibonacci(lim)
# 	sequence = seq[0]
# 	counter = seq[1]
# 	for i in sequence:
# 		counter += 1
# 		if (i % 2) == 0:
# 			counter += 1
# 			ans += i
# 	print ans
# 	print counter



# def evenfibonacci(lim):
# 	t1 = 1
# 	t2 = 1
# 	ans = 0
# 	counter =0
# 	while t2 < lim:
# 		counter += 1 
# 		if t2 % 2 == 0:
# 			counter += 1
# 			ans += t2
# 		temp = t2
# 		t2 += t1
# 		t1 = temp
# 	print counter
# 	print ans


def evenfibonacci(lim):
	t1 = 1
	t2 = 1
	ans = 0
	counter =0
	while t2 < lim:
		counter += 1 
		if t2 % 2 == 0:
			counter += 1
			ans += t2
		temp = t2
		t2 += t1
		t1 = temp
	print counter
	print ans


evenfibonacci(4000000)
