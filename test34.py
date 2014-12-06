ten_things = "apples oranges crows telephone light sugar"

print "wait there's not 10 things in that list, let's fix that"

stuff = ten_things.split(' ')
print stuff
more_stuff = ['day','night','song','frisbee','corn','banana','girl','boy']

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "adding: ", next_one
	stuff.append(next_one)
	print "there's %d items now. " % len(stuff)

print "now the stuff:", stuff
print "now the more stuff", more_stuff

print "let's do somthing with stuff"

print stuff[-1]

print stuff[-1]

print stuff.pop()

print stuff

print ' '.join(stuff)

print '#'.join(stuff[3:5])

temp = ' '.join(stuff)

print isinstance(temp,str)













