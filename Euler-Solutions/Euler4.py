def isPalindrome(num):
	num = str(num);
	numCopy = num;
	numCopy = numCopy[::-1]

	if(numCopy == num):
		return 1;
	return 0;

max = 0;
for i in range(100, 1000):
	for j in range(100, 1000):
		num = i * j
		if(isPalindrome(num) and num > max):
			max = num;
print max;
