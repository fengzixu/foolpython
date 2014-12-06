#have 100 cars
cars = 100
#each car space 
space_in_a_car=4
#divers
drivers=30;
#passagers
passengers=90
#empty cars
#dont driving car
cars_not_driven=cars-drivers
cars_driven=drivers
#have many capacity
carpool_capacity = cars_driven * space_in_a_car
#people in every car
average_passengers_per_car = passengers/cars_driven

print "there are",cars,"cars available."
print "there are only",drivers," drivers available"
print "there will be",cars_not_driven,"empty cars today"
print "we can transport",carpool_capacity,"people today"
print "we have ",passengers,"to carpool today"
print "we need to put about",average_passengers_per_car,"in each car."
