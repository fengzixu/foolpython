def print_two(*args):
	arg1,arg2 = args
	print "arg1:%r, arg2:%r"%(arg1,arg2)

	
def print_two_again(arg1,arg2):
	print "arg1:%r, arg2:%r"%(arg1,arg2)

def print_one(arg1):
	print"arg1:%r"%arg1

def print_nothing():
	print "i got nothing"
	
print_two("haha","heihei")
print_two_again("wocao","nima")
print_one("hehe")
print_nothing()