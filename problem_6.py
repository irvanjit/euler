import pdb
def sumsquarediff(num):
	sumofsquares = 0
	squareofsums = 0
	for i in range(1, num):
		sumofsquares += (i**2)
		squareofsums += i
	squareofsums = squareofsums**2
	ans = squareofsums - sumofsquares
	print sumofsquares
	print squareofsums
	print ans

sumsquarediff(101)