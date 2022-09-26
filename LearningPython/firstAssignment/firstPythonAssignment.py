# Simple Calculator #
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("Select Operation")
print("1. Addition 2. Subtraction 3. Multiplication 4. Division")
user = input("Enter choice: ")

if user in ('1', '2', '3', '4'):
    num1 = float(input("First Number in Operation: "))
    num2 = float(input("First Number in Operation: "))
    if user == '1':
        print("Your answer is = ", addition(num1, num2))
    elif user == '2':
        print("Your answer is = ", subtraction(num1, num2))
    elif user == '3':
        print("Your answer is = ", multiplication(num1, num2))
    elif user == '4':
        print("Your answer is = ", division(num1, num2))
else:
    print("Invalid operation please select a number 1-4")

# ------------------------------------------------------------------------------------ #

# largest among three numbers #

num_list_3 = [3, 7, 99]
print("Largest among the 3 numbers: ", max(num_list_3))

# ------------------------------------------------------------------------------------ #

# Leap Year

year = int(input("Enter a year: "))
if year % 400 == 0 and year % 100 == 0:
    print("This is a Leap Year!")
elif year % 4 == 0 and year % 100 != 0:
    print("This is a Leap Year!")
else:
    print("This is not a Leap Year!")

# ------------------------------------------------------------------------------------ #

# Generate Fibonacci Sequence #

num_terms = int(input("How many terms?: "))
first_term = 0
second_term = 1
count = 0
if num_terms <= 0:
    print("Input a positive integer!")
elif num_terms == 1:
    print("Fibonacci Sequence up to", num_terms, ":")
    print(first_term)
else:
    print("Fibonacci Sequence: ")
    while count < num_terms:
        print(first_term)
        nth = first_term + second_term
        first_term = second_term
        second_term = nth
        count += 1
print("END OF SEQUENCE!")

# ------------------------------------------------------------------------------------ #

# Check Prime Number #

num_prime = int(input("Enter a number to check if it is a prime number: "))
if num_prime % 2 != 0:
    print(num_prime, "is a prime number!")
else:
    print(num_prime, "is not a prime number!")

# ------------------------------------------------------------------------------------ #

# Absolute Value using function #

num_abs = int(input("Enter a number to get the absolute value: "))
print("The absolute value is ", abs(num_abs))

# ------------------------------------------------------------------------------------ #

# number of strings where string length is 2 #

sample_list = ['abc', 'xyz', 'aba', '1221']
counter = 0
for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        counter += 1
print(counter)

# ------------------------------------------------------------------------------------ #

# removing duplicates from a list #

list = [1, 1, 2, 3, 4, 5, 4]
dupes_removed = [*set(list)]
print(dupes_removed)

# ------------------------------------------------------------------------------------ #

# checks if a list is empty #

empty_list = []
if len(empty_list):
    print("List is populated!")
else:
    print("List is empty!")

# ------------------------------------------------------------------------------------ #

# copies a list to another list #

first_list = [1, 2, 5, 6, 10]
copied_list = first_list.copy()
print(copied_list)

# ------------------------------------------------------------------------------------ #

# prints the maximum number in the list #

num_list = [2, 5, 100]
print(max(num_list))

# ------------------------------------------------------------------------------------ #

# prints the sum of all values of the list #

sum_list = [8, 2, 3, 0, 7]
print(sum(sum_list))

# ------------------------------------------------------------------------------------ #

# multiplies every value in the list #

multiply_list = [8, 2, 3, -1, 7]
product = 1
for x in multiply_list:
    product = product * x
print(product)

# ------------------------------------------------------------------------------------ #

# reverses the txt string #

txt = "1234abcd"[::-1]
print(txt)

# ------------------------------------------------------------------------------------ #
