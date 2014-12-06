from sys import exit

from random import randint

def death():
	"""
	hahaha
	"""
	quips = ['you died. you kinda suck at this',
			 'nice job, you died ... jackass',
			 'such a luser',
			 'i have a small puppy that better at this.']
	print quips[randint(0,len(quips)-1)]
	exit(1)


def central_corridor():
	print "the gothons of planet percal #25 have invaded your ship and destroyed"
	print "yourentire crew. you are the last surviving memeber and your last"
	print "mission is to get the neutron destruct bomb from the weapons armory"
	print "escape pod"

	action = raw_input('> ')

	if action == "shoot!":
		print "quick on the draw you yank out your blaster and fire it at the gothon"
		return "death"

	elif action == "dodge!":
		print "like a world class boxer you dodge, weave, slip and slide rigth"
		return "death"
	elif action == "tell a joke":
		print "luck for you they made you learn gothon insults in academy"
		return "laser_weapon_armory"
	else:
		print "does not compute"
		return "central_corridor"


def laser_weapon_armory():
	print "you do a dive roll into the weapon armory."
	code = "%d%d%d"%(randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("[keypad]> ")	
	guesses = 0

	while guess!=code and guesses<10:
		print "bzzzzeddd!"
		guesses+=1
		guess = raw_input("[keypad]> ")

	if guess == code :
		print "the container clicks open and seal breaks"
		return 'the_bridge'
	else:
		print "the lock buzzes one lasr time and then you hear a sicking"
		return "death"	
def the_bridge():
	print "you burst onto the bridge with neutron destruct bomb"

	action = raw_input("> ")
	if action == "throw the bomb":
		print "in a panic you throw the bomb at the group of gothon"
	elif action == "slowly place the bomb":
		print "you point your balster at bomb under your harm"

def escape_pod():
	print "you rush through the ship deperately trying to make it"
	good_pod = randint(1,5)
	guess = raw_input("[pod #]> ")

	if int(guess) != good_pod:
		print "you jump into pod %s  and hit the eject button."%guess	
		return 'death'	
	else:
		print "you jump into pod %s  and hit the eject button."%guess
		print "time . you win"
		exit(0)

ROOMS = {'death':death,
		 'central_corridor':central_corridor,
		 'laser_weapon_armory':laser_weapon_armory,
		 'the_bridge':the_bridge,
		 'escape_pod':escape_pod
		 }


def runner(map1, start):
	next = start

	while True:
		room = map1[next]
		print "\n------"
		next = room()

runner(ROOMS,'central_corridor')











































