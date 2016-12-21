#!/usr/bin/python
#-*- encoding:utf-8 -*-

from math import floor
from random import random
import string

vowels = ('a','e','i','o','u')
consonants = ('b','c','d','f','g','h','j','l','m','n','p','r','s','t','v','w','x','y','z')
# Right now, removed 'q', 'k' because of their uselessness, can be readded without problem

#uppers = string.ascii_uppercase
uppers = tuple( map(str.upper, vowels + consonants) ) # This way we avoid unwanted consonants

# Each consonant maps other consonants that might follow it
conections = {'b': ('l', 'r'), 'c': ('h', 'k', 'l', 'r', 't'), 'd': ('r'), \
'f': ('l', 'r'), 'g': ('l', 'r', 'u'), 'k': ('l', 'r', 't'), \
'l': ('l'), 'm' : ('p'), 'n': ('s', 't'), \
'p' : ('l', 'r'), 't': ('l', 'r', 's'), 'q': ('u'), \
'w': ('r') }
CONECTION_CHANCE = 0.5

# Gets one random value from "cont". "cont" may be a list, a tuple...
def pick_random_value_from_container(cont):
	index = int(floor( random() * len(cont) ))
	return cont[index]
	
# Generates one component, which will have "comp_length" length, to be part of the full name
def generate_comp(comp_length):
	if comp_length < 1:
		print 'Given length cannot be less than 1.'
		return ''
	
	comp = [];
	
	# Upper letter as first character
	first = pick_random_value_from_container(uppers)
	comp.append(first)
	
	# If first letter is a consonant, we made a half iteration (so consonant is not followed by not valid consonant)
	if not first.lower() in vowels:
		if first in conections.keys() and random() < CONECTION_CHANCE:
			new_cons = pick_random_value_from_container(conections.get(first))
			comp.append(new_cons)
			
		vowel = pick_random_value_from_container(vowels)
		comp.append(vowel)
	
	# Generates pairs of vowels and consonants
	while len(comp) < comp_length:
		cons = pick_random_value_from_container(consonants)
		comp.append(cons)
		
		# Gives a chance to add a second consonant to the previous if it has one
		if cons in conections.keys() and random() < CONECTION_CHANCE:
			new_cons = pick_random_value_from_container(conections.get(cons))
			comp.append(new_cons)
			
		vowel = pick_random_value_from_container(vowels)
		comp.append(vowel)
	
	#comp = comp[:comp_length]
	
	return ''.join(comp);

# Generates a full name in which the i_th component will have "lengths[i]" length
# So, typically, "lengths" will consist in a list with 3 elements (first name and two surnames or one first name, one last name and one surname)
def generate_full_name(lengths):
	result = [generate_comp(l) for l in lengths]
	return ' '.join(result)

### Test ###
MINIMUM_TEST_LENGTH = 3
MAXIMUM_TEST_LENGTH = 8
NAME_NUM_COMPONENTS = 3
NAMES_TO_GENERATE = 19

# We will generate NAMES_TO_GENERATE full names
for i in range(NAMES_TO_GENERATE):
	# In this test, "lengths" is refilled with NAME_NUM_COMPONENTS random numbers varying from MINIMUM_TEST_LENGTH to MAXIMUM_TEST_LENGTH in each iteration
	ls = [ int(floor( random() * MAXIMUM_TEST_LENGTH ) + MINIMUM_TEST_LENGTH) for j in range(NAME_NUM_COMPONENTS)]

	# This is when the full name is requested and generated
	full_name = generate_full_name(ls)
	
	# Prints the result!
	print full_name #, ls
	
# If you just want the simplest example:
print generate_full_name([3,5,5])
