# read content from poem.txt line by line and display the same on screen #
f1 = open("poem.txt", "r")
line1 = f1.readline()
line2 = f1.readline()
print(line1 + line2)
f1.close()
# ----------------------------------------------------------------------- #

# count number of lines from story.txt which don't start with a capital T (should display 3) #
f2 = open("story.txt", "r")
count = 0
while True:
    line = f2.readline()
    if line.startswith("T"):
        count -= 1
    else:
        count += 1
    if not line:
        break
print(count)
f2.close()
# ----------------------------------------------------------------------- #

# function to count and display the total number of words in a text file #
def numberWords(filepath):
    file = open(filepath, "r")
    data = file.read()
    words = data.split()
    print("Number of words in the text file: ", len(words))
    file.close()
# ----------------------------------------------------------------------- #

# function that reads notes.txt should find and count the word 'the' (output should be 5) #
f3 = open("notes.txt", "r")
di = dict()
for line in f3:
    line = line.strip()
    line = line.lower()
    lines_words = line.split(" ")

    for word in lines_words:
        if word in di:
            di[word] = di[word] + 1
        else:
            di[word] = 1
print("occurences of the word 'the'", "=", di["the"])

f3.close()
# ----------------------------------------------------------------------- #

# write a function 'display_words()' to read lines from story.txt and display all words that
# are less than 4 characters #
def display_words(filepath):
    file2 = open(filepath, "r")
    for lin in file2:
        lin = lin.strip()
        lin = lin.lower()
        line_words = lin.split(" ")

        for wor in line_words:
            if len(wor) < 4:
                print(wor)
    file2.close()

display_words("story.txt")
# ----------------------------------------------------------------------- #

# Write a function to count the words 'this' and 'these' present in article.txt #
f4 = open("article.txt", "r")
d = dict()
for li in f4:
    li = li.strip()
    li = li.lower()
    li_words = li.split(" ")

    for wo in li_words:
        if wo in d:
            d[wo] = d[wo] + 1
        else:
            d[wo] = 1
print("occurences of the word 'this'", "=", d["this"])
print("occurences of the word 'these'", "=", d["these"])
f4.close()
# ----------------------------------------------------------------------- #

# Write a function to count word in a text file that end with the letter 'e' #
def endsE(filepath):
    file3 = open(filepath, "r")
    counts = 0
    while True:
        liness = file3.readline()
        if liness.endswith("e"):
            counts -= 1
        else:
            counts += 1
        if not liness:
            break
    print(counts)
    file3.close()

endsE("article.txt")
# ----------------------------------------------------------------------- #

# Write a function to count the uppercase characters in a text file #
def upperCase(filepath):
    file4 = open(filepath, "r")
    text = file4.read()
    c = 0
    for i in text:
        if i.isupper():
            c += 1
    print(c)
    file4.close()

upperCase("notes.txt")
# ----------------------------------------------------------------------- #

# Rectangle class: allows you to build a rectangle with length and width attributes
# create a Perimeter method and an Area method to calculate the perimeter and area
# create a method Display that displays the length, width, perimeter, area of an object
# created using the rectangle class
# Create a Parallelepipede child class inheriting from Rectangle with a height attribute
# and another Volume method to calculate the volume of the Parallelepipede #
class Rectangle:

    def __init__(self, width, length):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Width:", self.width)
        print("Length:", self.length)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())

rectangle = Rectangle(7, 9)
rectangle.display()

class Parallelepipede(Rectangle):
    def __init__(self, height, width, length):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.width * self.height * self.length

    def display(self):
        super().display()
        print("Height: ", self.height)
        print("Volume: ", self.volume())

# ----------------------------------------------------------------------- #

# Person class and child Student class: Person attributes = name and age (both Strings)
# Create a display() method that displays the name and age of an object created from the
# Person class.
# Create a child class Student which inherits from the Person class which also has the 'section' attribute
# Create a method displayStudent() that displays the name, age, and section of an object
# created from the Student class
# Then test the displayStudent() method#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Section: ", self.section)

person = Person("Guy", 25)
person.display()

student = Student("Guy", 27, "English")
student.displayStudent()

# ----------------------------------------------------------------------- #

# Bank Account class: class called BankAccount which represents a bank account having
# the attributes: accountNumber(int), name(String), balance(float/int)
# Constructor with the parameters: accountNumber, name, balance
# Deposit() method which manages the deposit actions
# Withdrawal() method which manages withdrawal actions
# bankFees() method to apply bank fees with a percentage of 5% of the balance account
# Create a display() method to display all account details#
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdrawal(self, withdrawal):
        self.balance -= withdrawal

    def bankFees(self):
        fee = self.balance * .05
        self.balance -= fee

    def display(self):
        print("Account Number: ", self.accountNumber)
        print("Name: ", self.name)
        print("Balance: ", self.balance)

bankAcc = BankAccount(937501750, "Guy", 200)
bankAcc.deposit(25)
bankAcc.withdrawal(100)
bankAcc.bankFees()
bankAcc.display()
# ----------------------------------------------------------------------- #
