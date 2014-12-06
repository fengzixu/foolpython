def cheese_and_crackers(cheese_count, boxes_of_crackers):
	cheese_count+=10
	boxes_of_crackers+=10
	print "cheese_count %d   boxes_of_crackers %d"%(cheese_count,boxes_of_crackers) 
	print "you have %d cheeses!" % cheese_count
	print "you have %d boxes of crackers!"%boxes_of_crackers
	print "man that's enough for party!"
	print "get a blanket.\n"

	
print "we can just give the function numbers directly"
cheese_and_crackers(20,30)

print "of, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print "amount_of_cheese %d, amount_of_crackers %d"%(amount_of_cheese,amount_of_crackers)
print "we can even do math inside too:"

cheese_and_crackers(10+20,5+6)

print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)



def print_numbers(x,y):
	print "x = %d, y = %d\n" % (x, y)

print_numbers(1,2)
a = 9
b=8
print_numbers(a,b)
print_numbers(a+9,b+8)
print a,b


