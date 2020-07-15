'''
Basics of python Executable code 
'''
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