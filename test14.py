from sys import argv

scripts, filename = argv

fileptr = open(filename)

print fileptr.read()
