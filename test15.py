from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

print "copying from %s to %s"%(from_file, to_file)
open(to_file,'w').write(open(from_file).read())