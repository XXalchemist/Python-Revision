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
|13.| Map, Reduce, Filter and Join |
|14.| List, Set, Generator and Dictionary Comprehension |
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
