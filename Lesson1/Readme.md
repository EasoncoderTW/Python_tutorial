# Lesson 1: print and input

## 1. Hello world
In Python, you can execute with just one line of command. Compared to C/C++, which are also high-level languages, Python’s syntax is diverse and simple.

python 
```python
# print "hello world"
print("hello world")
```
C
```C
#include <stdio.h>

int main()
{
    printf("hello world\n");
    return 0;
}
```
C++
```CPP
#include <iostream>
using namespace std;

int main()
{
    cout << "hello world" << endl;
    return 0;
}
```

> Hello World 的由來 -https://kknews.cc/zh-tw/tech/l9x2e8b.html


## 2. print function and input function

In Python, the print function is used to output information to the console, while the input function is used to get input from the user.

```python
# use print to output a string on screen
print("Hello, world!")

# use input to get letters from user
name = input("Please enter your name: ")
print("Hello, " + name + "!")
```

The print function has two common parameters: **sep** and **end**
```python
print(string 1, string 2, ... , sep=" ", end="\n") # by default
```
All strings will be printed and separated by the string represented by sep. The default is " " (blank key). And the end will be concatenated with the string represented by end, and the default is a newline symbol `\n`.

## Excersice
Please complete the fill in the blanks in the program and make the output string use the input string as the delimiter.

```
Enter seperator: @@@
Enter a string: Apple
Apple@@@Apple@@@Apple@@@Apple@@@Apple
```