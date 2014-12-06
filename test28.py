def print_num(i):
	numbers = []
	for num in range(0,i):
		print "at the top i is %d"%num
		numbers.append(num)
		print "numbers is ", numbers
		if num + 1 < i:
			 print "at bottom i is %d" % (num+1)
	print "numbers "
	for num in numbers:
		print num

def print_again(i,j):
	numbers = []
	num = 0
	while(num<i):
	
		print "at the top num is %d" % num
		numbers.append(num)
		num = num + j;
		print "numbers now: ", numbers
		print "at the bottom num is %d" % num
		
		
	
	print "numbers is :"
	for each in numbers:
		print each
		
print_again(6,1)