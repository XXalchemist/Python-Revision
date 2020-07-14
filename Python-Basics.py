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
