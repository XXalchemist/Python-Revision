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
|7. | Objects and Classes |
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

```python
if (condition 1):
    block of statements
elif (condition 2):
    block of statements
else:
    block of statements
```
### 