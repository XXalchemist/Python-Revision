# Python Basics

## Topics Covered

|*Sr. No.*| *Topic Name* |
|----------|--------------|
|1. | Types of data |
|2. | Expressions and variables |
|3. | String, Tuple, List, Dictionary, Set |
|4. | Loops |
|5. | Conditional Statements |
|6. | Functions and scope |
|7. | Objects and Classes and Dunder Methods|
|8. | ```__name__ == __main__``` |
|9. | ``` *args and **kwargs ```|
|10.| Try, Except, Else and Finally (Exception handling)|
|11.| Virtual Enviroment |
|12.| Iterators, Iterables and Generators |
|13.| List, Set, Generator and Dictionary Comprehension |
|14.| Map, Reduce, Filter and Join |
|15.| Bisect Module |
|16.| Lambda Function |
|17.| Enumerate |
|18.| Formatting of string |
|19.| ! Property, Decorators, Settters and Getters |

### 1. Data Types

_Everything in Python is an Object_

**Data Types :-**<br>
*int* : Integer Number ; 
*float* : Decimal Number ;
*str* : String (Collection of characters) ;
*bool* : True or False value <br>

_Typecasting is supported in python. Example: int(2.1) = 2._

```Python
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
```
### 2. Expression and Variables

**Expression: Statement consists of operators and operands to perform certain operation.**<br>

**Variables: Used to store data in programming language.**

### 3. String, List, Tuple, Dictionary, Set

**String: Sequence of characters that is denoted under "" or ''. Example: "Name". Immutable(can't change the value of string but can overwrite it) , Ordered Sequence. Stride => [start:stop:jump]**<br>

_Some Examples of String Methods are :-_

1. .upper( ) : Convert to uppercase.
2. .replace('old_subset','new_subset') : replace the subset of string.
3. .find('subset') : returns -1 if not present.

**List: Iterable object, ordered sequence, mutable object and denoted by [ ].Example: [1,3,4,2].**<br>

_Some Examples of List methods are :-_

1. .extend( )
2. .sort()
3. .split("delimiter")

_del object name can delete any object in python._

**Tuple: Immutable, ordered object and denoted by ( ). Example: (1,2,3).**<br>
**Set: Unordered object, contains unique value and is represented by { }. Example: {1,2,3}.**<br>

1. .add('')
2. .remove('')
3. .union(set_name)

**Dictionary: Contains keys and values, acts as hash map, keys have to be immutable and unique and values can be mutable. Example: {'a':1,'b':2}**<br>

1. .keys()
2. .values()
3. .items()
 
_name in dictionary name will lookup for name in keys_

### 4. Loops

_There are three types of loop in python._<br>

1. For
2. While

### 5. Conditional Statements

**Relational Operators  : >=, <=, ==, ===, !=; Logical Operators: AND, OR, NOT; Arithmetic Operators: +, - ,/, %, //**
```python
if (condition 1):
    block of statements
elif (condition 2):
    block of statements
else:
    block of statements
```
### 6. Functions and Scope

**Function: Block of statement that have to execute agian and again.**
_Syntax :-_
```python
def function_name(parameters):
    block of statements
    return value
```
**Scope: Variables that is used in particular block of statements.**
_if variable is not declared in function then it store the global value of that variable._

### 7. Objects and Classes

**Class**: Blueprint of Object, and **Object**: Instance of Class.

_Every object has_ :-
1. a **type**.
2. an internal data representation **Blueprint**.
3. set of procedures for interacting with objects **Methods**.
   
_A class or types **Methods** are function that every instance of that class or type provides.

>Syntax :-

```python

class ClassName: # Parent classes can be multiple or none according to the need.
    
    # Class variable - variable that is used by only this class.
    variable_name = value

    # Constructor
    def __init__(self, instanceVariables):
        self.instanceVariable = instanceVariable

    # Class Methods - method used by class only.
    @classmethod
    def class_method_name(cls, value): # used to change value of class variable
        cls.variable_name = value

    # Static methods - when there is no use of class or instance method
    @staticmethod
    def static_method_name(parameters):
        block of statements
  
# Inheritance 

class ClassName(ParentClass):
    
    def __init__(self,parameters_1, parameters_2):
        # if parameters_1 is present in parent class then we can inherit that class.
        super().__init__(parameters_1):
            self.parameters_2 = parameters_2
    
    # Same methods name can be used to overwrite methods of parent class. First class searches method in present class and after that it searches methods in parent class.


# Magic / Dunder Methods : used for method override and represented "__methodname__".

__add__ : To override addition. Example: (A + B)
__repr__: To cahnge representation of object. Example: repr(object_name) 
__str__: To overwrite repr() method. Example: str(object_name)


```
### 8. __name__ == '__main__'

**It is best to use __name__ == '__main__' in python coding to run particular section of code from particular package and modules. __name__ is global variable**

```python


if __name__ == '__main__':
    main()

def main():
    block of statements    
```

### 9. *args and **kwargs

***args**: To take number of variables as an argument. Multiple one value pass. `type(*args) = tuple`<br>
****kwargs**: To take two values each time. Multiple Two Value pass. `type(**kwargs) = dictionary`<br>

>We can change names of args and kwargs but not notation.

### 10. Exception Handling

**Exception: only interrupts certain part of program.**
**Error: interrupts whole executable program.**<br>
`try, except is used to handle exceptions in python.`<br>

>Syntax :-

```python

# Exception handling for multiple exceptions

try:
    error statement
except error_name as e:
    block of statements
except error_name as e:
    block of statements
.
.
.
finally: # This will run every time
    block of statements

# Exception handling with else

try:
    statement
except Exception as e:
    print(e)
else:
    print("if except block doesn't execute")
finally:
    print('This will always execute')

```

### 11. Virtual Enviroment

**To use certain packages in certain project.**<br>

>All commands here are for windows cmd/powershell.<br>

_To install virtualenv :-_
```s
pip install virtualenv
```
_To create and activate virtual env :-_
```s
virtualenv virtualenv_name
virtualenv_name/scripts/activate
```
_To deactivate virtual env :-_
```s
deactivate
```
_To create requirements.txt file to hold all required package name :-_
```s
pip freeze>requirements.txt
```
_To create virtual env which have preinstalled system packages :-_
```s
virtualenv --system-site-package virtualenv_name
```
_To delete virtual env :-_
```s
del virtualenv_name
```
_To install packages that are in requirements.txt :-_
```s
pip install -r requirements.txt
```

### 12. Iterators, Iterables and Generators

- Iterator : operator used for iteration.
- Iterable : object that can be iterated.
- Iteration: process of iterating elements.
- Generator: takes time but doesn't consume much memory, very useful to create iterable object.
  
` iter() `is used to create iterable object.

>Python code :-
```python

# Generator

def gernerator_name(parameters):
    for i in range(200):
        yield i
print(gen(1000))

obj_1 = gen(1000)
obj_1.next() # To yield next item of generator object


```

### 13. List, Set, Dictionary and Generator Comprehension

**List Comprehension**
```Python
list_object = [ ]
[function for parameters in list_object if condition] 
```

**Dictionary Comprehension**
```Python
dict_1 = { }
{function for parameters in list_object if condition}
```

**Set Comprehension**
```Python
set_1 = set()
{function for parameters in list_object if condition} 
```

**Generator Comprehension**
```Python
gen = (function for parameters in list_object if condition)
for item in gen:
    print(item)

```

### 14. Map, Filter, Reduce and join in Python

- **Map:** return map object , map each element of sequence to the given function._Syntax:_ *map  (function_to_apply, list_of_inputs)*
- **Reduce:** return list object, reduce the number of elements in sequence by applying function to each element of the sequence._Syntax:_ *First import : from functools import reduce then reduce(function_name, list)*
- **Filter:** return filter object, contains elements if the condition is true. We have to typecast the result._Syntax:_ *filter(function_name, list_of_inputs)*
- **Join:** Join each elements in list with some symbol._Syntax:_ *'symbol'.join(list_of_inputs)*
  
