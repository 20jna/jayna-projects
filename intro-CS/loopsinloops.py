import math
test = int(input("enter a number: "))
if test==0:
	print("can't handle 0")
else:

	isPrime = True

	for i in range(2, int(math.sqrt(test)+1)):
		if test%1==0:
			print("not prime")	
			isPrime = False
			break
	if isPrime:
		print("prime")

