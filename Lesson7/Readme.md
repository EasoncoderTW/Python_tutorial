# Lesson 7: Functions

In this lesson, we will cover the basics of functions in Python, including how to define and call functions, how to work with function parameters and return values, and understanding the scope and lifetime of variables.

## Defining and Calling Functions

### Defining a Function
A function is defined using the `def` keyword followed by the function name, parentheses, and a colon. The code block within every function starts with an indentation.
```python
def greet():
    print("Hello, world!")
```

### Calling a Function
A function is called by using the function name followed by parentheses.
```python
greet()  # Output: Hello, world!
```

## Function Parameters and Return Values

### Parameters
Parameters are specified within the parentheses in the function definition. They act as placeholders for the values that are passed to the function when it is called.
```python
def greet(name):
    print(f"Hello, {name}!")
```
```python
greet("Alice")  # Output: Hello, Alice!
```

### Return Values
A function can return a value using the `return` statement.
```python
def add(a, b):
    return a + b
```
```python
result = add(3, 4)
print(result)  # Output: 7
```

### Default Parameters
A function can have default parameter values, which are used if no argument is provided for the parameter when the function is called.
```python
def greet(name="World"):
    print(f"Hello, {name}!")
```
```python
greet()         # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
```

## Scope and Lifetime of Variables

### Local Scope
Variables defined inside a function are in the local scope of that function and are not accessible outside the function.
```python
def my_function():
    x = 10
    print(x)

my_function()  # Output: 10
print(x)       # Error: NameError: name 'x' is not defined
```

### Global Scope
Variables defined outside any function are in the global scope and can be accessed from anywhere in the code.
```python
x = 10

def my_function():
    print(x)

my_function()  # Output: 10
print(x)       # Output: 10
```

### The `global` Keyword
To modify a global variable inside a function, use the `global` keyword.
```python
x = 10

def my_function():
    global x
    x = 5

my_function()
print(x)  # Output: 5
```

### Lifetime of Variables
The lifetime of a variable is the period during which the variable exists in memory. Variables defined inside a function exist only while the function is executing.

## Examples and Exercises

### Example 1: Basic Function
Define a function that takes a number and prints its square.
```python
def print_square(number):
    print(number ** 2)
```
```python
print_square(4)  # Output: 16
```

### Example 2: Function with Return Value
Define a function that takes two numbers and returns their product.
```python
def multiply(a, b):
    return a * b
```
```python
result = multiply(3, 5)
print(result)  # Output: 15
```


### Example 3: Variable Scope
Demonstrate the difference between local and global scope.
```python
x = 10

def my_function():
    x = 5
    print(f"Inside function: {x}")

my_function()  # Output: Inside function: 5
print(f"Outside function: {x}")  # Output: Outside function: 10
```

### Exercises

#### Exercise 1: Sum of List
Write a function that takes a list of numbers and returns the sum of all the numbers in the list.

#### Solution
```python
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```
```python
result = sum_list([1, 2, 3, 4, 5])
print(result)  # Output: 15
```

#### Exercise 2: Factorial Function
Write a function that takes a number and returns its factorial.

#### Solution
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
```python
result = factorial(5)
print(result)  # Output: 120
```

#### Exercise 3: Check Prime
Write a function that takes a number and checks if it is prime. The function should return `True` if the number is prime, and `False` otherwise.

#### Solution
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
```python
result = is_prime(7)
print(result)  # Output: True
result = is_prime(10)
print(result)  # Output: False
```

Understanding functions and how to use them effectively is crucial for writing reusable and modular code in Python. Practice these examples and exercises to become proficient in defining and calling functions, working with parameters and return values, and managing the scope and lifetime of variables.
