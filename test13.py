from sys import argv

script, filename = argv

print "we're going to erase %r."%filename
print "if you don't want that, hit ctrl-c"
print "if you do want that, hit return"

raw_input("?")
print "opening the file..."
target = open(filename,'w')

print "Truncating the file .goodbye!"
target.truncate()

print "now, i'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "i'm going to write these to the file."
target.write("%s\n%s\n%s\n"%(line1,line2,line3))


print "and finally , we close it"
target.close()
