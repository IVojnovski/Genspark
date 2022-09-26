import math
import re
from operator import itemgetter
from shutil import move

# A website requires the users to input username and password to register. Write a program to check the validity of
# password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.#
username = input("Please input a username: ")
password = input("Please input a password (should have at least one lowercase letter, one number, one capital letter"
                 ", and one of these special characters : $#@. The minimum length should be 6 and the maximum should be"
                 " 12: ")
pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,12}$"
if re.match(pattern, password):
    print("This is the correct password!")
else:
    print("This is an incorrect password")

# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
# age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys. #
def SortingTuples():
    names = []
    while (True):
        name = input("Enter person to sort:")
        if len(name) == 0:
            break
        names.append(tuple(name.split(",")))
    names.sort(key=itemgetter(0, 1, 2))
    print(names)

# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n
#
# Hints:
# Consider use yield #
class GenNums:
    def __init__(self):
        self.number = 26
    def nums(self, num):
        ans = []
        for x in range(num):
            if x % self.number == 0:
                ans.append(x)
        print(ans)
# ------------------------------------------------------------------------------------------------------------------ #
# Question£º
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after
# a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input. #
def RobotMoves():
    x = 0
    y = 0

    while(True):
        direct = input("Enter which direction you'd like the robot to move (UP, DOWN, LEFT, or RIGHT) followed by the "
                     "number of steps:").split()
        if len(direct) == 0:
            break
        if move[0][0].lower() == "UP":
            y += int(move[1])
        elif move[0][0].lower() == "DOWN":
            y -= int(move[1])
        elif move[0][0].lower() == "LEFT":
            x -= int(move[1])
        elif move[0][0].lower() == "RIGHT":
            x += int(move[1])
        else:
            break

    print("Distance Traveled: ", int(math.dist([0, 0], [x, y])))
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key
# alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
#
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input. #
list = {}
while True:
    words = input("Enter words to count and display the frequency of each word: ").split()
    if len(words) == 0:
        break
    for x in words:
        if x not in list:
            list[x] = 1
        elif x in list:
            list[x] += 1
res = sorted(list.items())

for x in res:
    print(str(x[0]) + ": " + str(x[1]))
# ------------------------------------------------------------------------------------------------------------------ #
# Question 23
# level 1
#
# Question:
#     Write a method which can calculate square value of number
#
# Hints:
#     Using the ** operator #
def square(number):
    print("The square of this number is: ", number**2)

square(6)
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
#     Python has many built-in functions, and if you do not know how to use it, you can read document online or find
#     some books. But Python has a built-in document function for every built-in functions.
#     Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
#     And add document for your own function
#
# Hints:
#     The built-in document method is __doc__ #
def doc():
    """this is my function and it does nothing"""

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
print(doc.__doc__)

# ------------------------------------------------------------------------------------------------------------------ #
# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later #
class_param = 0
class Define():
    def __init__(self):
        self.class_param = 12
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a function which can compute the sum of two numbers.
#
# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value. #
def add(num, num2):
    print("The sum of these 2 numbers is: ", num + num2)

add(1, 2)
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a function that can convert a integer into a string and print it in console.
#
# Hints:
#
# Use str() to convert a number to string. #
def intToString(number):
    print(str(number))

intToString(71569016359691)
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in
# console.
#
# Hints:
#
# Use int() to convert a string to integer.
# Question:
# Define a function that can accept two strings as input and concatenate them and then print it in console.
# Hints:
# Use + to concatenate the strings #
def convertStringtoInt(stringNum, stringNum2):
    print("The sum of these 2 numbers is: ", int(stringNum) + int(stringNum2))

convertStringtoInt("23", "5")
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two
# strings have the same length, then the function should print al l strings line by line.
#
# Hints: #
def biggerString(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    else:
        print(str2)

biggerString("This is a smaller string", "This is definitely the larger string")
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is
# even, otherwise print "It is an odd number".
#
# Hints:
#
# Use % operator to check if a number is even or odd. #
def evenOrOdd(numb):
    if numb % 2 == 0:
        print("this number is even")
    else:
        print("this number is odd")

evenOrOdd(4)
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the
# values are square of keys.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number. #
dicti = dict()
for x in range(1, 4):
    dicti[x] = x**2

print(dicti)
# ------------------------------------------------------------------------------------------------------------------ #
# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
# values are square of keys.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops. #
dictio = dict()
for x in range(1, 21):
    dictio[x] = x**2

print(dictio)
# ------------------------------------------------------------------------------------------------------------------ #
