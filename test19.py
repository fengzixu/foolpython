def add(a,b):
	print "ADDING %d + %d  = %d" % (a,b,a+b)
	return a + b
def subtract(a,b):
	print "subtract %d - %d = %d" % (a,b,a-b)
	return a - b;
def multiply(a, b):
	print"multiply %d * %d = %d" % (a,b,a*b)
	return a * b
	
def divide(a,b):
	print "divide %d / %d = %d" %(a,b,a/b)
	return a/b
	
print "let's go do some math with just function"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "age %d heigth %d weight %d iq %d" %(age, height, weight, iq)

print "here is puzzle"

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "that becomes:", what , "Can you do it by hand"


chu = divide(iq,2)
cheng = multiply(weight,chu)
jian = subtract(height,cheng)
jia = add(age,jian)

print "jia = %d" % jia