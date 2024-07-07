# Lesson 5: Lists and Array-like Structures

In this lesson, we will cover the basics of lists in Python, list methods and operations, and an introduction to tuples, dictionaries, and sets.

## Introduction to Lists

### What is a List?
A list is a collection of items in a particular order. Lists are mutable, meaning they can be changed after they are created. Lists are defined by enclosing elements in square brackets (`[]`).

### Creating a List
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

### Accessing Elements
```python
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1])  # Output: cherry
```

### Modifying Elements
```python
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

## List Methods and Operations

### Adding Elements
- **append()**: Adds an element to the end of the list.
  ```python
  fruits.append("orange")
  print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
  ```

- **insert()**: Inserts an element at a specified position.
  ```python
  fruits.insert(1, "banana")
  print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'cherry', 'orange']
  ```

### Removing Elements
- **remove()**: Removes the first occurrence of an element.
  ```python
  fruits.remove("banana")
  print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
  ```

- **pop()**: Removes and returns the last item, or the item at the specified position.
  ```python
  popped_fruit = fruits.pop()
  print(popped_fruit)  # Output: orange
  print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
  ```

### Other Useful Methods
- **sort()**: Sorts the list in ascending order.
  ```python
  fruits.sort()
  print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
  ```

- **reverse()**: Reverses the order of the list.
  ```python
  fruits.reverse()
  print(fruits)  # Output: ['cherry', 'blueberry', 'apple']
  ```

- **len()**: Returns the number of elements in the list.
  ```python
  print(len(fruits))  # Output: 3
  ```

### List Comprehensions
List comprehensions provide a concise way to create lists.
```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Understanding Tuples, Dictionaries, and Sets

### Tuples
Tuples are immutable sequences, typically used to store collections of heterogeneous data. Tuples are defined by enclosing elements in parentheses (`()`).

```python
tuple_example = (1, "apple", 3.14)
print(tuple_example)  # Output: (1, 'apple', 3.14)
print(tuple_example[1])  # Output: apple
```

### Dictionaries
Dictionaries are unordered collections of key-value pairs. Dictionaries are defined by enclosing key-value pairs in curly braces (`{}`).

```python
dict_example = {"name": "Alice", "age": 25, "city": "New York"}
print(dict_example)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(dict_example["name"])  # Output: Alice

# Adding a new key-value pair
dict_example["email"] = "alice@example.com"
print(dict_example)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
```

### Sets
Sets are unordered collections of unique elements. Sets are defined by enclosing elements in curly braces (`{}`).

```python
set_example = {"apple", "banana", "cherry"}
print(set_example)  # Output: {'apple', 'cherry', 'banana'}

# Adding an element to a set
set_example.add("orange")
print(set_example)  # Output: {'apple', 'cherry', 'banana', 'orange'}

# Removing an element from a set
set_example.remove("banana")
print(set_example)  # Output: {'apple', 'cherry', 'orange'}
```

## Examples and Exercises

### Example 1: List Operations
Create a list of numbers and perform various operations.
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(2, 2.5)
numbers.remove(4)
print(numbers)  # Output: [1, 2, 2.5, 3, 5, 6]
```

### Example 2: Tuple and Dictionary
Create a tuple and a dictionary, then access their elements.
```python
tuple_example = (10, 20, 30)
dict_example = {"first": 10, "second": 20, "third": 30}

print(tuple_example[1])  # Output: 20
print(dict_example["second"])  # Output: 20
```

### Example 3: Set Operations
Create a set and perform various operations.
```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}
```

### Exercises

#### Exercise 1: List Manipulation
1. Create a list of five of your favorite movies.
2. Add a new movie to the list.
3. Remove the second movie from the list.
4. Print the final list of movies.

#### Solution
```python
movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "The Dark Knight"]
movies.append("Pulp Fiction")
movies.pop(1)
print(movies)  # Output: ['Inception', 'Interstellar', 'The Godfather', 'The Dark Knight', 'Pulp Fiction']
```

#### Exercise 2: Dictionary Usage
1. Create a dictionary with three key-value pairs: name, age, and city.
2. Add a new key-value pair for email.
3. Update the age value.
4. Print the final dictionary.

#### Solution
```python
person = {"name": "John", "age": 30, "city": "New York"}
person["email"] = "john@example.com"
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}
```

#### Exercise 3: Set Operations
1. Create a set of five unique colors.
2. Add a new color to the set.
3. Remove an existing color from the set.
4. Print the final set of colors.

#### Solution
```python
colors = {"red", "blue", "green", "yellow", "purple"}
colors.add("orange")
colors.remove("green")
print(colors)  # Output: {'red', 'blue', 'yellow', 'purple', 'orange'}
```

#### Exercise 4: Top 3 Student
- Suppose you have a dictionary format with student names and grades as follows:
```python
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Carol": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 91,
}

###  add your code here ###


```
- finish the code that find out the top-3 score student


Understanding lists and other array-like structures in Python is fundamental for handling collections of data. Practice these examples and exercises to become proficient in using lists, tuples, dictionaries, and sets.
