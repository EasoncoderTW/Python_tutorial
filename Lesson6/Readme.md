# Lesson 6: Loop Statements

In this lesson, we will cover the basics of loop statements in Python, including the usage of `for` and `while` loops, loop control statements such as `break` and `continue`, and nested loops.

## Using `for` and `while` Loops

### For Loop
A `for` loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string).

#### Example: For Loop
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

### While Loop
A `while` loop repeatedly executes a block of code as long as a condition is `True`.

#### Example: While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
Output:
```
0
1
2
3
4
```

## Loop Control Statements: `break` and `continue`

### Break Statement
The `break` statement is used to exit a loop before it has finished iterating over all items.

#### Example: Break Statement
```python
for num in range(10):
    if num == 5:
        break
    print(num)
```
Output:
```
0
1
2
3
4
```

### Continue Statement
The `continue` statement is used to skip the current iteration of the loop and continue with the next iteration.

#### Example: Continue Statement
```python
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```
Output:
```
1
3
5
7
9
```

## Nested Loops
A nested loop is a loop inside another loop. The inner loop is executed once for each iteration of the outer loop.

#### Example: Nested Loop
```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```
Output:
```
i = 0, j = 0
i = 0, j = 1
i = 1, j = 0
i = 1, j = 1
i = 2, j = 0
i = 2, j = 1
```

## Examples and Exercises

### Example 1: Using `for` Loop
Write a program to print the square of each number in a list.
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number ** 2)
```
Output:
```
1
4
9
16
25
```

### Example 2: Using `while` Loop
Write a program to print numbers from 10 to 1 using a `while` loop.
```python
count = 10
while count > 0:
    print(count)
    count -= 1
```
Output:
```
10
9
8
7
6
5
4
3
2
1
```

### Example 3: Using `break` Statement
Write a program to find the first number in a list that is divisible by 3 and print it. Stop the loop once the number is found.
```python
numbers = [1, 2, 4, 8, 9, 12]
for number in numbers:
    if number % 3 == 0:
        print(f"First number divisible by 3: {number}")
        break
```
Output:
```
First number divisible by 3: 9
```

### Example 4: Using `continue` Statement
Write a program to print all odd numbers from 0 to 10 using a `for` loop.
```python
for num in range(11):
    if num % 2 == 0:
        continue
    print(num)
```
Output:
```
1
3
5
7
9
```

### Example 5: Nested Loops
Write a program to print a 3x3 matrix using nested loops.
```python
for i in range(3):
    for j in range(3):
        print(f"{i},{j}", end=" ")
    print()
```
Output:
```
0,0 0,1 0,2 
1,0 1,1 1,2 
2,0 2,1 2,2 
```

### Exercises

#### Exercise 1: Sum of Numbers
Write a program to find the sum of all numbers from 1 to 100 using a `while` loop.

#### Solution
```python
total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(f"Sum of numbers from 1 to 100: {total}")
```
Output:
```
Sum of numbers from 1 to 100: 5050
```

#### Exercise 2: Multiplication Table
Write a program to generate a multiplication table for numbers 1 to 5 using nested loops.

#### Solution
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j}", end="\t")
    print()
```
Output:
```
1	2	3	4	5	
2	4	6	8	10	
3	6	9	12	15	
4	8	12	16	20	
5	10	15	20	25	
```

#### Exercise 3: Factorial Calculation
Write a program to calculate the factorial of a given number using a `for` loop.

#### Solution
```python
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")
```
Output:
```
Factorial of 5 is 120
```

Understanding loops and how to control them is essential for efficiently managing repetitive tasks in Python. Practice these examples and exercises to become proficient in using `for` and `while` loops, as well as loop control statements and nested loops.