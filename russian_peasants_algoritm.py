#!/usr/bin/env python3

#The Russian Peasant's Algorithm

#Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

def russian(a,b):
	x = a; y = b 						# Semicolon -> Compund Statement
	z = 0								# Acmulator
	while x > 0:  						# While loop begins
		if x % 2 == 1: z += y 			# Modulo operator
		y = y << 1 						# Shift binary over to left = multiply with 2
		x = x >> 1 						# Shift binary over to right = divide by 2
	return z 							# Return z

print russian(357, 16)					# Testing the algorithm with values
print russian(16, 24)
