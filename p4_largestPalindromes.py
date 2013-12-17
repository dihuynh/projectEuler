#!/usr/bin/env python

def check_palindrome (a):
	return str(a)[::-1] == str(a)

def get_palindromes ():
	i = 999
	all_palindromes = []
	while (i>0):
		j = 999
		while (j>0):
			product = i * j
			if check_palindrome(product):
				all_palindromes.append(product)
			j = j - 1
		i = i - 1

	return all_palindromes;


answer = get_palindromes()
answer.sort()
print answer[-1]