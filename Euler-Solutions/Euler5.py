num = 1
notFinished = True;
while(notFinished):
	notFinished = False;
	for i in range(2, 21):
		if(num % i != 0):
			notFinished = True;
			num += 1;
			break;
	if(num % 50000 == 0):
		print num

print num
