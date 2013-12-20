#!/usr/bin/env python

import itertools
import math
# this is really slow, like really slow
#print list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))[999999]


#let's be smarter
print "There are 10 spots _ _ _ _ _ _ _ _ _ _"
print "There are 9! permutations if 0 takes the first spot"
print "That is", math.factorial(9), "which isn't close to 1 million"
print "So 0 can't be in the first spot"
print "Similarly, there are 9! permutations if 1 takes the first spot"
print "So in a lexicographic order, we have 2*9! (",2*math.factorial(9),\
		")\nafter enumerating with 0's and 1's as the first character"
print
print "Still not 1 million. How about one more, let's make 2 our first character"
print "We're at 3*9!(",3*math.factorial(9),"). aaand there it is"
print "This is more than 1 million, so the first character has to be a 2"
print "Keep following this logic and you'll get: 2783915460"