# Lesson 3: Arithmetic Symbols

In this lesson, we will cover the basic arithmetic operations in Python, as well as modulus, exponentiation, and floor division. We will also discuss operator precedence, which determines the order in which operations are performed.

## Basic Arithmetic Operations

### Addition
The addition operator `+` adds two numbers together.
```python
a = 10
b = 5
result = a + b
print(result)  # Output: 15
```

### Subtraction
The subtraction operator `-` subtracts one number from another.
```python
a = 10
b = 5
result = a - b
print(result)  # Output: 5
```

### Multiplication
The multiplication operator `*` multiplies two numbers.
```python
a = 10
b = 5
result = a * b
print(result)  # Output: 50
```

### Division
The division operator `/` divides one number by another.
```python
a = 10
b = 5
result = a / b
print(result)  # Output: 2.0
```

## Modulus, Exponentiation, and Floor Division

### Modulus
The modulus operator `%` returns the remainder of a division.
```python
a = 10
b = 3
result = a % b
print(result)  # Output: 1
```

### Exponentiation
The exponentiation operator `**` raises a number to the power of another number.
```python
a = 2
b = 3
result = a ** b
print(result)  # Output: 8
```

### Floor Division
The floor division operator `//` divides one number by another and rounds down to the nearest integer.
```python
a = 10
b = 3
result = a // b
print(result)  # Output: 3
```

## Operator Precedence

Operator precedence determines the order in which operations are performed. Operators with higher precedence are evaluated before operators with lower precedence.

### Precedence Table
1. `()` Parentheses
2. `**` Exponentiation
3. `*`, `/`, `//`, `%` Multiplication, Division, Floor Division, Modulus
4. `+`, `-` Addition, Subtraction

### Example
Consider the following expression:
```python
result = 2 + 3 * 4 ** 2 / (1 - 5) % 3
```
The order of operations is as follows:
1. Parentheses: `1 - 5` → `-4`
2. Exponentiation: `4 ** 2` → `16`
3. Multiplication: `3 * 16` → `48`
4. Division: `48 / -4` → `-12.0`
5. Modulus: `-12.0 % 3` → `0.0`
6. Addition: `2 + 0.0` → `2.0`

So, the final result is `2.0`.

```python
result = 2 + 3 * 4 ** 2 / (1 - 5) % 3
print(result)  # Output: 2.0
```

## Exercises

### Exercise 1: Basic Arithmetic
Calculate the results of the following expressions and print the outputs:
1. `7 + 3`
2. `15 - 8`
3. `6 * 9`
4. `81 / 9`

### Solution
```python
print(7 + 3)   # Output: 10
print(15 - 8)  # Output: 7
print(6 * 9)   # Output: 54
print(81 / 9)  # Output: 9.0
```

### Exercise 2: Modulus, Exponentiation, and Floor Division
Calculate the results of the following expressions and print the outputs:
1. `17 % 5`
2. `2 ** 4`
3. `20 // 3`

### Solution
```python
print(17 % 5)   # Output: 2
print(2 ** 4)   # Output: 16
print(20 // 3)  # Output: 6
```

### Exercise 3: Operator Precedence
Calculate the result of the following expression and print the output:
```python
result = 5 + 2 * 3 ** 2 // (4 - 2) % 3
print(result)
```

### Solution
The order of operations is as follows:
1. Parentheses: `4 - 2` → `2`
2. Exponentiation: `3 ** 2` → `9`
3. Multiplication: `2 * 9` → `18`
4. Floor Division: `18 // 2` → `9`
5. Modulus: `9 % 3` → `0`
6. Addition: `5 + 0` → `5`

```python
result = 5 + 2 * 3 ** 2 // (4 - 2) % 3
print(result)  # Output: 5
```

Understanding these basic arithmetic operations and their precedence will help you write more complex and accurate Python programs.
