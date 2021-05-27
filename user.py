# CONFIGURATION FILE
from termcolor import colored
import random


'''
user_config params:-

testCases: Number of testCases to test against
usedtt: Multiple testCases in input (NOTE: Refresh each global parameter after each test case)
showEachPass: Print affirmative after each test case passed
removeBlanks: remove blanks (whitespaces) in the output
whereFail: print where the output doesn't match
inputPipe: input file used to feed input to executables
debug: for each input -> print input, your output & brute output
saveTC: path to a file which stores the failed test case, None if file is not to be saved
'''
user_config = {
    "testCases" : 1000, 
    "usedtt" : False,
    "showEachPass" : True,
    "removeBlanks" : True, 
    "whereFail" : True, 
    "inputPipe" : "temp/inputf.in",
	"debug": False,
	"saveTC": "sols/in.txt"
}


# ===========


'''
docs: 
Generate your random test cases in this function

return: 
list of strings where each string is supposed to be displaed on a new line
'''
def gen_case():
	lim = int(10)
	dlim = 10
	n = random.randint(1, lim)
	a = [random.randint(-dlim, dlim) for i in range(n)]
	tc = [str(n), ' '.join(list(map(str, a)))]
	return tc


# ===========


'''
docs: 
Checks if your solution is correct based on an input
Currently performs string comparison

params: 
inp: list of strings denoting the input
brute_response: list of strings denoting brute output
my_response: list of strings denoting my output

return: 
boolean denoting if output satisifes the condition
'''
def checker(my_response, brute_response = None, inp = None):
    # check matching length
	if len(my_response) != len(brute_response):
		print(colored("\n!! FAIL !!", 'red', attrs = ['bold']))
		if user_config["whereFail"]:
			print("whereFail: UNMATCHING LENGTH")
		return False
		
	# compare each line of response
	N = len(my_response)
	for i in range(N):
		if my_response[i] != brute_response[i]:
			print(colored("\n!! FAIL !!", 'red', attrs = ['bold']))
			if user_config["whereFail"]:
				print("whereFail: LINE", i + 1)
				print("my_response: ", my_response[i])
				print("brute_response: ", brute_response[i])
			return False
	return True
