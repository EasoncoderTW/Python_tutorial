# Lesson 9 - Files

In this lesson, we will cover the basics of working with files in Python, including how to open, read, write, and close files, as well as understanding file modes and handling exceptions.

## Opening and Closing Files

### Opening a File
Files are opened using the `open()` function, which returns a file object. You need to specify the filename and the mode in which you want to open the file.
```python
file = open('example.txt', 'r')  # Open for reading
```

### Closing a File
It is important to close the file after performing operations to free up system resources.
```python
file.close()
```

### Using `with` Statement
Using the `with` statement to open a file ensures that it is properly closed after its suite finishes, even if an exception is raised.
```python
with open('example.txt', 'r') as file:
    content = file.read()
```

## Reading from Files

### Reading the Entire File
You can read the entire content of a file using the `read()` method.
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Reading Line by Line
You can read the file line by line using the `readline()` method.
```python
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')  # end='' to avoid double newline
        line = file.readline()
```

### Reading All Lines into a List
You can read all the lines of a file into a list using the `readlines()` method.
```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
```

## Writing to Files

### Writing to a File
You can write to a file using the `write()` method.
```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
```

### Writing a List of Lines
You can write a list of lines to a file using the `writelines()` method.
```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

## File Modes

### Common File Modes
- `'r'` - Read mode (default). Opens the file for reading.
- `'w'` - Write mode. Opens the file for writing (creates a new file or truncates the existing file).
- `'a'` - Append mode. Opens the file for writing and appends to the end of the file if it exists.
- `'b'` - Binary mode. Used with other modes to read/write binary files.

### Example of Different Modes
```python
# Read mode
with open('example.txt', 'r') as file:
    content = file.read()

# Write mode
with open('example.txt', 'w') as file:
    file.write("Overwriting the content.")

# Append mode
with open('example.txt', 'a') as file:
    file.write("\nAppending this line.")

# Binary mode
with open('example.bin', 'wb') as file:
    file.write(b"Binary data")
```

## Exception Handling with Files

### Handling Exceptions
It is important to handle exceptions when working with files to avoid crashes due to file-related errors.
```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")
```

## Examples and Exercises

### Example 1: Reading a File
Read the contents of a file and print each line.
```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

### Example 2: Writing to a File
Write multiple lines to a file.
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

### Example 3: Appending to a File
Append a line to an existing file.
```python
with open('example.txt', 'a') as file:
    file.write("Appending this line.\n")
```

### Example 4: Exception Handling
Handle exceptions when trying to read a non-existent file.
```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")
```

### Exercises

#### Exercise 1: Count Lines
Write a function that takes a filename as an argument and returns the number of lines in the file.

#### Solution
```python
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

# Test
print(count_lines('example.txt'))  # Output: (number of lines in example.txt)
```

#### Exercise 2: Copy File
Write a function that takes two filenames as arguments and copies the content of the first file to the second file.

#### Solution
```python
def copy_file(source, destination):
    with open(source, 'r') as src_file:
        content = src_file.read()
    with open(destination, 'w') as dest_file:
        dest_file.write(content)

# Test
copy_file('example.txt', 'copy_example.txt')
```

#### Exercise 3: Word Frequency
Write a function that takes a filename as an argument and returns a dictionary with the frequency of each word in the file.

#### Solution
```python
def word_frequency(filename):
    with open(filename, 'r') as file:
        content = file.read()
    words = content.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Test
print(word_frequency('example.txt'))  # Output: {word: frequency, ...}
```

Understanding how to work with files is crucial for data processing and storage in Python. Practice these examples and exercises to become proficient in opening, reading, writing, and handling files, as well as managing file modes and exceptions.
