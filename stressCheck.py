'''
PREREQ:
1) Attached Makefile 'stress' command
2) Input should be piped in through inputPipe
3) Actual solution should be in T.cpp and brute should be in brute.cpp
'''

import os
from subprocess import run, PIPE
from termcolor import colored # externally downloaded
import random

# USER NOTE:- Do refresh each global quantity after each test case!
# USER PARAMETERS
# ===========
TestCases = 1000 # Number of testCases to test against
Usedtt = True # Multiple testCases in input
showEachPass = True # Print affirmative after each test case passed
removeBlanks = True # remove blanks in the output
whereFail = True # print where the output doesn't match
inputPipe = "inputf.in" # input file for prog
# ===========

# generating test cases
# USER PARAM
def genCase():
	# generate
	limw = 10
	limn = int(1e6)
	W = random.randint(1, limw)
	N = random.randint(1, limn)
	X = []
	for i in range(W):
		X.append(random.randint(1, N))

	# form tc
	tc = [str(W), str(N)]
	sX = list(map(str, X))
	tc.append(' '.join(sX))
	# print(*tc, sep = '\n') # DEBUG OUTPUT

	return tc

# failed a test case
def fail(tc, my_response, brute_response):
	print("\n-- Test Case --\n")
	print(*tc, sep = '\n')
	print("\n-- My Output --\n")
	print(*my_response, sep = '\n')
	print("\n-- Brute Output --\n")
	print(*brute_response, sep = '\n')
	exit(0)

# check if solution matches
def checker(my_response, brute_response): # currently string compares the output
	# check matching length
	if len(my_response) != len(brute_response):
		print(colored("\n!! FAIL !!", 'red', attrs = ['bold']))
		if whereFail:
			print("whereFail: UNEVEN LENGTH")
		return False
		

	# compare each line of response
	N = len(my_response)
	for i in range(N):
		if my_response[i] != brute_response[i]:
			print(colored("\n!! FAIL !!", 'red', attrs = ['bold']))
			if whereFail:
				print("whereFail: LINE", i + 1)
				print("my_response: ", my_response[i])
				print("brute_response: ", brute_response[i])
			return False
	return True

# TESTING LOOP =============>
print(colored("\n#### Stress Testing .. ####", 'cyan', attrs = ['bold']))
for currentTc in range(1, TestCases + 1):

	# fetching test case
	tc = genCase()
	if Usedtt:
		tc = ["1"] + tc

	# write to inputf.in
	stressIn = open(inputPipe, "w")
	for tline in tc:
		stressIn.write(tline + "\n")
	stressIn.close()

	# get my out
	my_proc = run("./myOut", stdout = PIPE)
	my_response = (my_proc.stdout.decode('utf-8')).split('\n')
	if removeBlanks:
		my_response = [line for line in my_response if line.strip()] # removing blanks
	# print (my_response) # DEBUG OUTPUT

	# get brute out
	brute_proc = run("./bruteOut", stdout = PIPE)
	brute_response = (brute_proc.stdout.decode('utf-8')).split('\n')
	if removeBlanks:
		brute_response = [line for line in brute_response if line.strip()] # removing blanks
	# print (brute_response) # DEBUG OUTPUT

	# check if output matches
	if !checker(my_response, brute_response):
		fail(tc, my_response, brute_response)
	elif showEachPass: # test case passed
		print (colored(".Passed case " + str(currentTc), 'green'))

# success
print(colored("\n> ALL BRUTE PASSED", 'cyan', attrs = ['bold']))
