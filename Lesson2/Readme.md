# Lesson 2: Type and Object

In Python, every value has a data type, which defines the characteristics of that value such as what operations can be performed on it. Python is a dynamically typed language, meaning you don't have to explicitly declare the data type of a variable. Python automatically determines the data type based on the value assigned to it.

## Types in Python

### 1. Int (Integer)
Integers are whole numbers without any decimal point. They can be positive or negative. Examples of integers are 5, -3, 100, etc.

### 2. Float (Floating-Point Number)
Floats are numbers that have a decimal point or use scientific notation. Examples of floats are 3.14, -0.001, 2.5e2, etc.

### 3. Str (String)
Strings are sequences of characters enclosed in single quotes (''), double quotes ("") or triple quotes (''' or """). Examples of strings are "hello", 'Python', "123", etc.

### 4. Bool (Boolean)
Booleans represent one of two values: True or False. They are often used in conditional statements and comparisons.

### Examples
```python 
# Integer
x = 5 
y = -3 
print(type(x))  # <class 'int'>

# Floats
pi = 3.14 
value = 2.5e2 
print(type(value))  # <class 'float'>

# Strings
name = "Alice" 
message = 'Hello, World!' 
print(type(message))  # <class 'str'>

# Booleans
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>
```

## Type Conversion in Python

Type conversion, also known as type casting, is the process of converting a value from one data type to another. Python provides several built-in functions for type conversion.

### Common Type Conversion Functions

1. `int()`: Converts a value to an integer.
2. `float()`: Converts a value to a floating-point number.
3. `str()`: Converts a value to a string.
4. `bool()`: Converts a value to a boolean.

### Examples
```python
# Converting float to int
pi = 3.14
pi_int = int(pi)
print(pi_int)  # 3

# Converting int to float
num = 10
num_float = float(num)
print(num_float)  # 10.0

# Converting int to string
number = 123
number_str = str(number)
print(number_str)  # "123"

# Converting string to int
string = "456"
string_int = int(string)
print(string_int)  # 456

# Converting string to float
string_float = float(string)
print(string_float)  # 456.0

# Converting different values to boolean
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("Hello"))  # True
```

In this tutorial, we covered the basic data types in Python - int, float, str, and bool. Understanding these data types is essential for writing Python programs. Feel free to explore more about these types and how to work with them in Python.

## Exercise

1. **Identify Data Types**:
   Determine the data types of the following values in Python:
   - 42
   - 3.14159
   - "Python"
   - True
   - '123'
   
2. **Type Conversion Practice**:
   Convert the following values and print their new data types:
   - Convert `7.5` to an integer.
   - Convert `100` to a string.
   - Convert `"False"` to a boolean.
   - Convert `0` to a boolean.
   

