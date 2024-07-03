# Lesson 8 - Modules and Packages

In this lesson, we will cover the basics of modules and packages in Python, including how to import modules, use standard libraries and third-party packages, and create and use custom modules.

## Importing Modules

### Importing a Module
A module is imported using the `import` statement. This allows you to access functions, classes, and variables defined in the module.
```python
import math

print(math.sqrt(16))  # Output: 4.0
```

### Importing Specific Attributes
You can also import specific attributes from a module.
```python
from math import sqrt

print(sqrt(16))  # Output: 4.0
```

### Renaming a Module
Modules can be renamed using the `as` keyword.
```python
import math as m

print(m.sqrt(16))  # Output: 4.0
```

## Standard Libraries and Third-Party Packages

### Standard Libraries
Python comes with a rich set of standard libraries. Some commonly used standard libraries include:
- `math` for mathematical functions
- `datetime` for manipulating dates and times
- `os` for interacting with the operating system

### Third-Party Packages
Third-party packages can be installed using `pip`, the Python package installer. For example, to install the `requests` package for making HTTP requests, you would run:
```bash
pip install requests
```

Once installed, you can import and use the package in your code.
```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200
```

## Creating and Using Custom Modules

### Creating a Custom Module
You can create your own modules by saving Python code in a `.py` file. For example, create a file named `my_module.py` with the following content:
```python
# my_module.py

def greet(name):
    return f"Hello, {name}!"
```

### Using a Custom Module
To use the custom module, import it in another Python file.
```python
# main.py

import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
```

## Examples and Exercises

### Example 1: Using a Standard Library
Use the `datetime` standard library to get the current date and time.
```python
import datetime

now = datetime.datetime.now()
print(now)  # Output: 2024-07-04 12:34:56.789012 (example output)
```

### Example 2: Installing and Using a Third-Party Package
Install the `requests` package and use it to make a GET request.
```python
import requests

response = requests.get('https://api.github.com')
print(response.json())  # Output: JSON response from the GitHub API
```

### Example 3: Creating and Using a Custom Module
Create a custom module with a function that calculates the factorial of a number.
```python
# factorial_module.py

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
```python
# main.py

import factorial_module

print(factorial_module.factorial(5))  # Output: 120
```

### Example 4: Custom Module with Multiple Functions
Create a custom module `math_utils.py` with multiple functions: `add`, `subtract`, `multiply`, and `divide`.
```python
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
```
```python
# main.py

import math_utils

print(math_utils.add(3, 5))        # Output: 8
print(math_utils.subtract(10, 4))  # Output: 6
print(math_utils.multiply(2, 7))   # Output: 14
print(math_utils.divide(20, 5))    # Output: 4.0
```

### Example 5: Importing from a Package
Create a package named `shapes` with two modules: `circle.py` and `rectangle.py`. Each module should have functions to calculate the area and perimeter.

#### Directory Structure:
```
shapes/
    __init__.py
    circle.py
    rectangle.py
```

#### circle.py:
```python
# circle.py

import math

def area(radius):
    return math.pi * (radius ** 2)

def perimeter(radius):
    return 2 * math.pi * radius
```

#### rectangle.py:
```python
# rectangle.py

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)
```

#### main.py:
```python
# main.py

from shapes import circle, rectangle

print(circle.area(5))          # Output: 78.53981633974483
print(circle.perimeter(5))     # Output: 31.41592653589793
print(rectangle.area(4, 6))    # Output: 24
print(rectangle.perimeter(4, 6))  # Output: 20
```

### Exercises

#### Exercise 1: Sum of List
Create a custom module `list_utils.py` with a function that takes a list of numbers and returns the sum of all the numbers in the list. Import and use this module in another script.

#### Solution
```python
# list_utils.py

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```
```python
# main.py

import list_utils

result = list_utils.sum_list([1, 2, 3, 4, 5])
print(result)  # Output: 15
```

#### Exercise 2: Check Prime
Create a custom module `prime_utils.py` with a function that takes a number and checks if it is prime. The function should return `True` if the number is prime, and `False` otherwise. Import and use this module in another script.

#### Solution
```python
# prime_utils.py

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
```python
# main.py

import prime_utils

print(prime_utils.is_prime(7))   # Output: True
print(prime_utils.is_prime(10))  # Output: False
```

#### Exercise 3: Geometry Package
Create a package named `geometry` with two modules: `triangle.py` and `square.py`. Each module should have functions to calculate the area and perimeter. Import and use these modules in a script.

#### Solution
#### Directory Structure:
```
geometry/
    __init__.py
    triangle.py
    square.py
```

#### triangle.py:
```python
# triangle.py

def area(base, height):
    return 0.5 * base * height

def perimeter(a, b, c):
    return a + b + c
```

#### square.py:
```python
# square.py

def area(side):
    return side ** 2

def perimeter(side):
    return 4 * side
```

#### main.py:
```python
# main.py

from geometry import triangle, square

print(triangle.area(5, 10))      # Output: 25.0
print(triangle.perimeter(3, 4, 5))  # Output: 12
print(square.area(4))           # Output: 16
print(square.perimeter(4))      # Output: 16
```

#### Exercise 4: Weather Data Module
Create a custom module `weather_utils.py` with a function `get_weather` that takes a city name and returns a string with a dummy weather report (e.g., "The weather in {city} is sunny."). Import and use this module in a script.

#### Solution
```python
# weather_utils.py

def get_weather(city):
    return f"The weather in {city} is sunny."
```
```python
# main.py

import weather_utils

print(weather_utils.get_weather("New York"))  # Output: The weather in New York is sunny.
print(weather_utils.get_weather("Paris"))     # Output: The weather in Paris is sunny.
```

Understanding modules and packages is crucial for organizing and reusing code effectively in Python. Practice these examples and exercises to become proficient in importing modules, using standard libraries and third-party packages, and creating and using custom modules. This will help you write cleaner, more maintainable code and collaborate more effectively with other developers.
