'''
Basics of python Executable code 
'''
from functools import reduce

boolean = True
Integer = 2
Float = 2.0
String = 'This is String'

print(boolean, Integer, Float, String ) 

# Typecasting

print('Float To Integer :' ,int(2.1))
print('Float to Integer: ',float(2))

# type() is used to print the class/data-type of variable

print(type(5))

# int('A') will not be typecasted

# Expression and variables

answer = 43 +31 //2 -1
print("\n",answer)

'''
Here,
answer: variable
=, +, //, - : Operators
43, 31, 2, 1 : Operands 
'''

# Strings

alpha = 'abcd'
#alpha[0] ='b' # will not work
alpha = alpha + 'e' # will work
print(alpha)
alpha.replace('d','k')

# Escape Sequence is denoted by \.
print("\nFind 'a': ",alpha.find('a'))
print("\nFind 'ab': ",alpha.find('ab'))
print("\nUppercase: ",alpha.upper())
print("\nReplace: ",alpha)

# Lists

list_1 = [1,3,2,'ab',4]
list_1.extend([2,3,1,4,5])
print(list_1)
del(list_1[0])
print(list_1,"\n")

# Tuples

tuple_1 = (1,2,3)

# Dictionary

dict_1 = {'a':1,'b':2}
for value,key in dict_1.items():
    print('Key: ',key,'-> value: ',value)

print('\n')
# Loops

# For Loop
for i in range(1,10):
    print(i,end='- ')
print("\n")

# While Loop
i = 0
while(i<=10):
    print(i,end='- ')
    i += 1
print('\n')

# Conditional Statements
a = 7
if (a > 5):
    print(True)
else:
    print(False)

# Functions

def print_bye(name):
    print(name,' bye - bye !')

print_bye('Krishna')

# Scope 
def add_1(y):
    x=x+1
    print(x)
x=2
# z = add_1(x) //returns error

# Objects and Classes

class Employee:
    increment = 1.5 # Class variable
    number_of_employee = 0 
    
    def __init__(self, first, last, sal): # Constructor for class
        self.fname = first   # instance variable
        self.lname = last
        self.salary = sal
    
    def increase(self):
        self.salary = self.salary * self.increment
    
    @classmethod # a function that uses only class variable
    def change_increment(cls, amount):
        cls.increment = amount

print('\nOOPS IN PYTHON\n')
Emp_1 = Employee('Narayan','Krishna',40000)

print('Name: ',Emp_1.fname+' '+Emp_1.lname,'\nSalary of Emp_1: ',Emp_1.salary,'')

Employee.change_increment(2)
Emp_1.increase()
print('New salary after increment: ',Emp_1.salary)

# Class Method as an alternative Constructor

class Employee_2:
    increment = 1.5 # Class variable
    number_of_employee = 0 
    
    def __init__(self, first, last, sal): # Constructor for class
        self.fname = first   # instance variable
        self.lname = last
        self.salary = sal
    
    def increase(self):
        self.salary = self.salary * self.increment

    @classmethod
    
    def from_string(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)

Emp_2 = Employee_2.from_string('Romit-Kumar-38000')
print('\nExample of class method as an alternative constructor:-\n','Salary of Emp_2: ',Emp_2.salary)

# Static methods in class (when there is no use of class methods or instance methods)

class Box:
    length = '5m'

    def __init__ (self,shape):
        self.shape = shape

    @staticmethod
    def is_shipped_on(day):
        if day == 'sun':
            return False
        else:
            return True

box_1 = Box('square')
print("\nExample of static method in class:-\n",'Is Shipped on Sunday:',box_1.is_shipped_on('sun'))

# Inheritance in Python Class

class Programmer(Employee):
    def __init__(self,fname,lname,sal,prolang,exp):
        super().__init__(fname,lname,sal)
        self.prolang = prolang
        self.exp = exp
    
    def increase(self): # Method overwriting
        self.salary = int(self.salary * (self.increment+0.2))

Emp_3 = Programmer('Fullmetal','Alchemist',45000,'Python','0yrs')    
print('\nExample Of Inheritance:-\n','Emp_3 salary: ',Emp_3.salary)
Emp_3.increase()
print('\nNew salary: ',Emp_3.salary)


# Magic / Dunder Method in Python -> Represented by '__methodName__' and is used for method overriding.

class Employee_3:

    def __init__(self, first, last, sal): # Constructor for class
        self.fname = first   # instance variable
        self.lname = last
        self.salary = sal

    # Magic method
    def __add__(self,other): # Changing the functionality of addition
        return self.salary + other.salary

    def __repr__(self): # what to show when we print object
        return 'Employee_3({}, {}, {})'.format(self.fname, self.lname, self.salary)
    
    # def __str__(self): #overwrites the repr method
    #     return 'The name is {} {}'.format(self.fname,self.lname)

Emp_4 = Employee_3('Dante','Kumar',40000)
Emp_5 = Employee_3('Gordon','Freeman',1000000)

print('\nExample of Dunder Methods:-\n','Emp_4 + Emp_5: ',Emp_4 + Emp_5,"--- repr(Emp_4): ",repr(Emp_4))

# *args and **kwargs

def function_1(*args):
    return 'The names are {}, {} and {}'.format(args[0],args[1],args[2])

print('\nExample of args: ',function_1('Prince',"Babbage","Charly"))

def function_2(**kwargs):
    for key, value in kwargs.items():
        print(key,' -> ',value)

marksheet = {'Rohan': 92, 'Mohan': 85}
print('\nExample of kwargs: ',"Marks of: ")
function_2(**marksheet)

# Exception Handling

# Exception - only interrupts certain part of program. Error - interrupt whole program.

try:
    open('a.txt')
except Exception as e:
    print("\nError : ",e)

# Handling Multiple exceptions

try:
    file = open('a.txt','r')
except EOFError as e:
    print(e)
except IOError as e:
    print('This is I/O Error')
finally:
    print('This will always run')

# Generators and iterators

def gen(n):
    for i in range(n):
        yield i
obj_1 = gen(10)
print('\nGenerators Example :- \n',obj_1)
print(next(obj_1))
print(next(obj_1))

print('\nFor Loop:-')
for i in range(10):
    print(i,end=',')

print('\nComprehsions Examples :- ')
# List, Set, Dictionary and Generator Comprehension
list_1 = [1,2,3,4,5,6,7,8,9]
print('List Example:-\n',[ item for item in list_1 if item % 2 == 0])

# Dictionary
keys = ['a','b', 'c']
values = ['1','2','3']
print('Dictionary Example:-\n',{i:j for (i,j) in zip(keys,values)})
# Set
squared = { x**2 for x in list_1 }
print('Set Example:-\n',squared)

# Generator
print('Generator Example:-\n')
gen = (i for i in range(56) if i% 3 == 0)
for item in gen:
    print(item, end =' ')

# Map

h1 = [1,2,3,4,5]
def square(n):
    return n*n

sq = list(map(square, h1))
print('\nExample Of Mapping: ',sq)

# Filter

def greater_than_2(num):
    if num > 2:
        return True
    else:
        return False
greater_than_2v = filter(greater_than_2, h1)
print('\nExample Of Filter: ',list(greater_than_2v))

# Reduce

def mul_num (a,b):
    return a*b

mul_list = reduce(mul_num, h1)

# Join

list_of = [ 'chalk', 'pen', 'paper']
print('\nExample of Join: ',' and '.join(list_of))

# Bisect Module
import bisect

list_num = [1,2,3,4,8]
print(bisect.bisect(list_num,5)) # tells where to insert number
print(bisect.insort(list_num,5)) # insert number
print('\nExample of Bisect: ',list_num)

# Lambda Function

add = lambda x,y: x+y
print('\nExample of Lamda Function: ',add(5,10))

# Enumerate in Python

print('\nEnumerate in Python :-')
rand_alpha = ['ab','cd','ed']

for i,item in enumerate(rand_alpha):
    print(i,' -> ',item)

# Formatting in Python
print('\nFormatting of string :-')
name = 'Algorithm To Live By'
categ = 'non-fiction'
template = 'This is {} book and category of this book is {}'.format(name,categ)
print(template)
template = 'This is {1} book and category of this book is {0}'.format(name,categ)
print(template)