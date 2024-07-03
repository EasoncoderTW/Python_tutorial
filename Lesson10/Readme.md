
# Lesson 10 - Classes and Objects (Object-Oriented Programming)

In this lesson, we will cover the basics of object-oriented programming (OOP) in Python, including how to define classes and create objects, understanding attributes and methods, and exploring inheritance and polymorphism.

## Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes. It allows for organizing code in a way that models real-world entities, making it easier to manage and scale.

### Key Concepts
- **Class**: A blueprint for creating objects (a particular data structure).
- **Object**: An instance of a class.
- **Attributes**: Variables that belong to an object or class.
- **Methods**: Functions that belong to an object or class.

## Defining Classes and Creating Objects

### Defining a Class
A class is defined using the `class` keyword, followed by the class name and a colon.
```python
class Dog:
    pass
```

### Creating an Object
An object is created by calling the class as if it were a function.
```python
my_dog = Dog()
print(my_dog)  # Output: <__main__.Dog object at 0x...>
```

## Understanding Attributes and Methods

### Attributes
Attributes are variables that belong to an object. They are defined in the `__init__` method, which is called when an object is created.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
```

### Methods
Methods are functions that belong to an object. They are defined inside a class.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Woof!
```

## Inheritance and Polymorphism

### Inheritance
Inheritance allows a class to inherit attributes and methods from another class. The class that inherits is called the child class, and the class being inherited from is called the parent class.
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak())  # Output: Woof!
print(my_cat.speak())  # Output: Meow!
```

### Polymorphism
Polymorphism allows methods to be used interchangeably between different classes. It is achieved by defining methods in the child classes with the same name as methods in the parent class.
```python
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    print(animal.name + " says " + animal.speak())
# Output:
# Buddy says Woof!
# Whiskers says Meow!
```

## Examples and Exercises

### Example 1: Simple Class
Define a class `Person` with attributes `name` and `age`, and a method `greet` that prints a greeting message.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Alice", 30)
person.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

### Example 2: Inheritance
Define a parent class `Vehicle` with attributes `brand` and `model`, and a method `drive`. Create a child class `Car` that inherits from `Vehicle` and adds an attribute `seats`.
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

car = Car("Toyota", "Corolla", 5)
car.drive()  # Output: The Toyota Corolla is driving.
print(f"This car has {car.seats} seats.")  # Output: This car has 5 seats.
```

### Example 3: Polymorphism
Define a parent class `Shape` with a method `area`. Create child classes `Circle` and `Rectangle` that implement the `area` method.
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:
    print(f"The area is {shape.area()}")
# Output:
# The area is 28.26
# The area is 20
```

### Exercises

#### Exercise 1: Define a Class
Define a class `Book` with attributes `title`, `author`, and `pages`. Add a method `description` that prints the book's details.

#### Solution
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def description(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

book = Book("1984", "George Orwell", 328)
book.description()  # Output: '1984' by George Orwell, 328 pages.
```

#### Exercise 2: Inheritance
Define a parent class `Employee` with attributes `name` and `salary`. Create a child class `Manager` that inherits from `Employee` and adds an attribute `department`.

#### Solution
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

manager = Manager("John Doe", 75000, "IT")
print(f"{manager.name} manages the {manager.department} department with a salary of {manager.salary}.")
# Output: John Doe manages the IT department with a salary of 75000.
```

#### Exercise 3: Polymorphism
Create a parent class `Animal` with a method `make_sound`. Create child classes `Dog` and `Cat` that implement the `make_sound` method. Write a function that takes a list of animals and calls the `make_sound` method on each.

#### Solution
```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def make_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Dog(), Cat()]
make_sounds(animals)
# Output:
# Woof!
# Meow!
```

Understanding classes and objects is crucial for mastering object-oriented programming in Python. Practice these examples and exercises to become proficient in defining classes, creating objects, and using inheritance and polymorphism effectively.

---

# Advanced Topics in Classes and Objects

In this lesson, we will delve deeper into some advanced features of classes and objects in Python, including special methods (also known as magic methods or dunder methods), such as `__call__`, `__repr__`, `__del__`, `__str__`, and `__add__`.

## Special Methods

Special methods in Python are defined by prefixing and suffixing their names with double underscores (`__`). These methods allow you to define the behavior of objects for built-in operations.

### `__repr__` and `__str__`

- `__repr__`: Defines the "official" string representation of an object. It is used for debugging and development.
- `__str__`: Defines the "informal" or nicely printable string representation of an object. It is used by the `print` function and `str()`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(repr(person))  # Output: Person(name='Alice', age=30)
print(person)        # Output: Alice, 30 years old
```

### `__call__`

The `__call__` method allows an object to be called like a function.
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
```

### `__del__`

The `__del__` method is called when an object is about to be destroyed. It is useful for cleanup actions.
```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Resource {self.name} created")
    
    def __del__(self):
        print(f"Resource {self.name} destroyed")

resource = Resource("Database Connection")
del resource  # Output: Resource Database Connection destroyed
```

### `__add__`

The `__add__` method allows you to define the behavior of the `+` operator for your objects.
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)
```

## Other Special Methods

### `__getitem__` and `__setitem__`

These methods allow objects to be used with indexing and item assignment.
```python
class MyList:
    def __init__(self):
        self.items = []
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList()
my_list.items = [1, 2, 3]
print(my_list[0])  # Output: 1
my_list[1] = 4
print(my_list[1])  # Output: 4
```

### `__len__`

The `__len__` method allows you to define the behavior of the `len()` function for your objects.
```python
class MyList:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)

my_list = MyList()
my_list.items = [1, 2, 3]
print(len(my_list))  # Output: 3
```

### `__iter__` and `__next__`

These methods allow objects to be used as iterators.
```python
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

for number in MyRange(1, 4):
    print(number)
# Output:
# 1
# 2
# 3
```

## Examples and Exercises

### Example 1: `__repr__` and `__str__`
Define a class `Book` with `__repr__` and `__str__` methods.
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "George Orwell")
print(repr(book))  # Output: Book(title='1984', author='George Orwell')
print(book)        # Output: '1984' by George Orwell
```

### Example 2: `__call__`
Define a class `Multiplier` that multiplies a number by a given factor when called.
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

times_two = Multiplier(2)
print(times_two(5))  # Output: 10
```

### Example 3: `__del__`
Define a class `File` that prints a message when a file object is deleted.
```python
class File:
    def __init__(self, name):
        self.name = name
        print(f"File {self.name} opened")
    
    def __del__(self):
        print(f"File {self.name} closed")

file = File("example.txt")
del file  # Output: File example.txt closed
```

### Example 4: `__add__`
Define a class `ComplexNumber` that adds two complex numbers.
```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)
c3 = c1 + c2
print(c3)  # Output: ComplexNumber(4, 6)
```

### Exercises

#### Exercise 1: `__getitem__` and `__setitem__`
Define a class `Dictionary` that implements the `__getitem__` and `__setitem__` methods.

#### Solution
```python
class Dictionary:
    def __init__(self):
        self.data = {}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value

d = Dictionary()
d['name'] = 'Alice'
print(d['name'])  # Output: Alice
```

#### Exercise 2: `__len__`
Define a class `Sentence` that implements the `__len__` method to return the number of words in the sentence.

#### Solution
```python
class Sentence:
    def __init__(self, text):
        self.words = text.split()
    
    def __len__(self):
        return len(self.words)

s = Sentence("Hello world this is a sentence")
print(len(s))  # Output: 6
```

#### Exercise 3: `__iter__` and `__next__`
Define a class `Countdown` that implements the `__iter__` and `__next__` methods to count down from a given number to zero.

#### Solution
```python
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current

for number in Countdown(5):
    print(number)
# Output:
# 5
# 4
# 3
# 2
# 1
# 0
```

Understanding and using special methods allow you to define custom behaviors for your objects, making them more intuitive and powerful. Practice these examples and exercises to become proficient in using special methods in Python.


