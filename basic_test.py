#!/usr/bin/env python3

#The Russian Peasant's Algorithm - basic test function

#Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

def adding(a,b):
	return a + b

def test_adding():
	assert adding(3,4) == 7
	assert adding(3,2) == 5
	assert adding(3,2) != 8
	assert adding(99,49) == 148
	#assert adding(99,49) == 7

	return "All tests pass for function adding()"

print test_adding()