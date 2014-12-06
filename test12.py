from sys import argv   #import argv

script, filename = argv

txt = open(filename)    #openfile

print "here's your file %r:"%filename

#print txt.read() #print file passage

print txt.read()
txt.close()
txt=open(filename)
print txt.read()
