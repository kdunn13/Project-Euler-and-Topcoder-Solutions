import math
num = 600851475143
counter = 2;
while(1):
	while(num % counter == 0):
		num /= counter;
	counter += 1;
	if(num == counter):
		print counter;
		exit(1);
