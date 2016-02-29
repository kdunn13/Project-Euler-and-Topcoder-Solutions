import math

def isPrime(num):
	if(num == 2):
		return 1;

	if(num % 2 == 0):
		return 0;

	for i in range(3, int(math.floor(math.sqrt(num))) + 1, 2):
		if(num % i == 0):
			return 0;

	return 1;

counter = 2;
primeCounter = 0;

while(1):
	if(isPrime(counter)):
		primeCounter += 1
	if(primeCounter == 10001):
		print counter;
		break;
	counter += 1;
