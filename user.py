# CONFIGURATION FILE
from termcolor import colored
import random


"""
user_config params:-

testCases: Number of testCases to test against
usedtt: Multiple testCases in input (NOTE: Refresh each global parameter after each test case)
showEachPass: Print affirmative after each test case passed
removeBlanks: remove blanks (whitespaces) in the output
whereFail: print where the output doesn't match
debug: for each input -> print input, your output & brute output
saveTC: path to a file which stores the failed test case, None if file is not to be saved
"""
user_config = {
    "testCases": 1000,
    "usedtt": False,
    "showEachPass": True,
    "removeBlanks": True,
    "whereFail": True,
    "inputPipe": "_temp/inputf.in",
    "debug": False,
    "saveTC": "sols/in.txt",
}


"""
NOTE: "_temp" is created during stress testing, it is advisable to leave these settings intact
NOTE: If you wish to change paths for intermediate executables, change appropriately in the makefile
stress_config params:
inputPipe: input file used to feed input to executables 
bruteExec: path to brute executable
myExec: path to your executable
"""
stress_config = {
    "inputPipe": "_temp/inputf.in",
    "bruteExec": "_temp/bruteOut",
    "myExec": "_temp/myOut",
}


# ===========


"""
docs: 
Generate your random test cases in this function

return: 
list of strings where each string is supposed to be displaed on a new line
"""


def gen_case():
    lim = int(5000)
    dlim = int(1e9)
    n = random.randint(1, lim)
    done = {}
    a = []
    while len(a) != n:
        put = random.randint(-dlim, dlim)
        while put in done:
            put = random.randint(-dlim, dlim)
        a.append(put)
        done[put] = 1
    tc = [str(n), " ".join(list(map(str, a)))]
    return tc


# ===========


"""
docs: 
Checks if your solution is correct based on an input
Currently performs string comparison

params: 
inp: list of strings denoting the input
brute_response: list of strings denoting brute output
my_response: list of strings denoting my output

return: 
boolean denoting if output satisifes the condition
"""


def checker(my_response, brute_response=None, inp=None):
    # check matching length
    if len(my_response) != len(brute_response):
        print(colored("\n!! FAIL !!", "red", attrs=["bold"]))
        if user_config["whereFail"]:
            print("whereFail: UNMATCHING LENGTH")
        return False

    # compare each line of response
    N = len(my_response)
    for i in range(N):
        if my_response[i] != brute_response[i]:
            print(colored("\n!! FAIL !!", "red", attrs=["bold"]))
            if user_config["whereFail"]:
                print("whereFail: LINE", i + 1)
                print("my_response: ", my_response[i])
                print("brute_response: ", brute_response[i])
            return False
    return True
