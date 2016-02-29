fib1 = 1;
fib2 = 1;
temp = 0;
sum = 0;

while(fib1 <= 4000000):
	temp = fib1;
	fib1 = fib1 + fib2;
	fib2 = temp;
	if(fib1 % 2 == 0):
		sum += fib1;

print sum;
