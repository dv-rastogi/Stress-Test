"""
PREREQ:
1) Attached Makefile 'stress' command
2) User configuration set in 'user.py'
3) Actual solution should be in 'sols/main.cpp' and brute should be in 'sols/brute.cpp'
"""

import os
from subprocess import run, PIPE
from termcolor import colored
from user import user_config, gen_case, checker


# failed a test case
def fail(tc, my_response, brute_response):
    print("\n-- Test Case --\n")
    print(*tc, sep="\n")
    print("\n-- My Output --\n")
    print(*my_response, sep="\n")
    print("\n-- Brute Output --\n")
    print(*brute_response, sep="\n")

    if user_config["saveTC"] is not None:
        with open(user_config["inputPipe"], "r") as f1:
            lines = f1.readlines()
            with open(user_config["saveTC"], "w") as f2:
                f2.writelines(lines)
        print(colored(f"\n> Test case saved at {user_config['saveTC']}", "yellow"))

    exit(0)


# TESTING LOOP =============>
print(colored("\n#### Stress Testing .. ####", "cyan", attrs=["bold"]))
for currentTc in range(1, user_config["testCases"] + 1):

    # fetching test case
    tc = gen_case()
    if user_config["usedtt"]:
        tc = ["1"] + tc
    if user_config["debug"]:
        print("Test case")
        print(*tc, sep="\n")

    # write to inputPipe
    stressIn = open(user_config["inputPipe"], "w")
    for tline in tc:
        stressIn.write(tline + "\n")
    stressIn.close()

    # get my out
    my_proc = run(
        ["temp/myOut"], stdout=PIPE, stdin=open(user_config["inputPipe"], "r")
    )
    my_response = (my_proc.stdout.decode("utf-8")).split("\n")
    if user_config["removeBlanks"]:
        my_response = [line for line in my_response if line.strip()]  # removing blanks
    if user_config["debug"]:
        print("My response")
        print(my_response)

    # get brute out
    brute_proc = run(
        ["temp/bruteOut"], stdout=PIPE, stdin=open(user_config["inputPipe"], "r")
    )
    brute_response = (brute_proc.stdout.decode("utf-8")).split("\n")
    if user_config["removeBlanks"]:
        brute_response = [
            line for line in brute_response if line.strip()
        ]  # removing blanks
    if user_config["debug"]:
        print("Brute response")
        print(brute_response)

    # check if output matches
    if not checker(my_response, brute_response=brute_response, inp=tc):
        fail(tc, my_response, brute_response)
    elif user_config["showEachPass"]:  # test case passed
        print(colored(".Passed case " + str(currentTc), "green"))

# success
print(colored("\n> ALL BRUTE PASSED", "cyan", attrs=["bold"]))
