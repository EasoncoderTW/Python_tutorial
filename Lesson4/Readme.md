# Lesson 4: Conditional Statements

In this lesson, we will cover the basics of conditional statements in Python, including the usage of `if`, `elif`, and `else` statements, comparison and logical operators, and nested conditional statements.

## Using `if`, `elif`, and `else` Statements

### If Statement
The `if` statement evaluates a condition and executes the block of code within it if the condition is `True`.
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### Elif Statement
The `elif` (short for "else if") statement allows you to check multiple conditions. If the preceding `if` condition is `False`, the `elif` condition is evaluated.
```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
```

### Else Statement
The `else` statement executes a block of code if none of the preceding conditions are `True`.
```python
x = 3
if x > 5:
    print("x is greater than 5")
elif x > 2:
    print("x is greater than 2 but less than or equal to 5")
else:
    print("x is 2 or less")
```

## Comparison and Logical Operators

### Comparison Operators
Comparison operators are used to compare values. They return `True` or `False`.
- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

### Logical Operators
Logical operators are used to combine conditional statements.
- `and`: Returns `True` if both conditions are `True`
- `or`: Returns `True` if at least one condition is `True`
- `not`: Returns `True` if the condition is `False`

### Examples
```python
# Comparison operators
a = 10
b = 5
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False

# Logical operators
x = 7
print(x > 5 and x < 10)  # True
print(x < 5 or x > 10)   # False
print(not (x < 5))       # True
```

## Nested Conditional Statements

Nested conditional statements are `if` statements inside other `if` statements. This allows for more complex condition checking.
```python
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x is greater than 5 and y is greater than 15")
    else:
        print("x is greater than 5 but y is 15 or less")
else:
    print("x is 5 or less")
```

## Examples and Exercises

### Example 1: Basic Conditional Statements
Write a program that checks if a number is positive, negative, or zero.
```python
num = 7
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
```

### Example 2: Logical Operators
Write a program that checks if a number is between 10 and 20 (inclusive).
```python
num = 15
if num >= 10 and num <= 20:
    print("The number is between 10 and 20")
else:
    print("The number is not between 10 and 20")
```

### Example 3: Nested Conditional Statements
Write a program that categorizes a person's age into child, teenager, or adult.
```python
age = 16
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

### Exercises

#### Exercise 1: Grade Checker
Write a program that takes a score (0-100) and prints the corresponding grade:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F

#### Solution
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

#### Exercise 2: Even or Odd
Write a program that checks if a number is even or odd.
```python
number = 42
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

#### Exercise 3: Leap Year Checker
Write a program that checks if a year is a leap year.
- A year is a leap year if it is divisible by 4, but not divisible by 100, except if it is also divisible by 400.

#### Solution
```python
year = 2000
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

Understanding conditional statements is crucial for controlling the flow of your Python programs. Practice these examples and exercises to become proficient in using `if`, `elif`, and `else` statements.
