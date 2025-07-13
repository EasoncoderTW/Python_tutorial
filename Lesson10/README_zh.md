# 第十課 - 類別和物件（物件導向程式設計）

在本課程中，我們將介紹 Python 中物件導向程式設計（OOP）的基礎，包括如何定義類別和建立物件、理解屬性和方法，以及探索繼承和多型。

## 物件導向程式設計介紹

物件導向程式設計（OOP）是一種使用物件和類別的程式設計範式。它允許以建模現實世界實體的方式組織程式碼，使其更容易管理和擴展。

### 關鍵概念
- **類別**：建立物件的藍圖（特定的資料結構）。
- **物件**：類別的實例。
- **屬性**：屬於物件或類別的變數。
- **方法**：屬於物件或類別的函數。

## 定義類別和建立物件

### 定義類別
類別使用 `class` 關鍵字定義，後面跟著類別名稱和冒號。
```python
class Dog:
    pass
```

### 建立物件
物件通過呼叫類別（如同呼叫函數）來建立。
```python
my_dog = Dog()
print(my_dog)  # 輸出：<__main__.Dog object at 0x...>
```

## 理解屬性和方法

### 屬性
屬性是屬於物件的變數。它們在 `__init__` 方法中定義，該方法在物件建立時被呼叫。
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)
print(my_dog.name)  # 輸出：Buddy
print(my_dog.age)   # 輸出：3
```

### 方法
方法是屬於物件的函數。它們在類別內部定義。
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()  # 輸出：Woof!
```

## 繼承和多型

### 繼承
繼承允許一個類別從另一個類別繼承屬性和方法。繼承的類別稱為子類別，被繼承的類別稱為父類別。
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

print(my_dog.speak())  # 輸出：Woof!
print(my_cat.speak())  # 輸出：Meow!
```

### 多型
多型允許方法在不同類別之間互換使用。它通過在子類別中定義與父類別中方法同名的方法來實現。
```python
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    print(animal.name + " says " + animal.speak())
# 輸出：
# Buddy says Woof!
# Whiskers says Meow!
```

## 範例和練習

### 範例 1：簡單類別
定義一個 `Person` 類別，具有 `name` 和 `age` 屬性，以及一個印出問候訊息的 `greet` 方法。
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"你好，我的名字是 {self.name}，我 {self.age} 歲。")

person = Person("Alice", 30)
person.greet()  # 輸出：你好，我的名字是 Alice，我 30 歲。
```

### 範例 2：繼承
定義一個父類別 `Vehicle`，具有 `brand` 和 `model` 屬性，以及一個 `drive` 方法。建立一個子類別 `Car`，從 `Vehicle` 繼承並添加 `seats` 屬性。
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} 正在行駛。")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

car = Car("Toyota", "Corolla", 5)
car.drive()  # 輸出：Toyota Corolla 正在行駛。
print(f"這輛車有 {car.seats} 個座位。")  # 輸出：這輛車有 5 個座位。
```

### 範例 3：多型
定義一個父類別 `Shape`，具有 `area` 方法。建立子類別 `Circle` 和 `Rectangle`，實作 `area` 方法。
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
    print(f"面積是 {shape.area()}")
# 輸出：
# 面積是 28.26
# 面積是 20
```

### 練習

#### 練習 1：定義類別
定義一個 `Book` 類別，具有 `title`、`author` 和 `pages` 屬性。添加一個 `description` 方法，印出書籍的詳細資訊。

#### 解答
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"《{self.title}》作者：{self.author}，共 {self.pages} 頁。")

book = Book("1984", "George Orwell", 328)
book.description()  # 輸出：《1984》作者：George Orwell，共 328 頁。
```

#### 練習 2：繼承
定義一個父類別 `Employee`，具有 `name` 和 `salary` 屬性。建立一個子類別 `Manager`，從 `Employee` 繼承並添加 `department` 屬性。

#### 解答
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
print(f"{manager.name} 管理 {manager.department} 部門，薪資為 {manager.salary}。")
# 輸出：John Doe 管理 IT 部門，薪資為 75000。
```

#### 練習 3：多型
建立一個父類別 `Animal`，具有 `make_sound` 方法。建立子類別 `Dog` 和 `Cat`，實作 `make_sound` 方法。編寫一個函數，接收動物列表並對每個動物呼叫 `make_sound` 方法。

#### 解答
```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "汪汪！"

class Cat(Animal):
    def make_sound(self):
        return "喵喵！"

def make_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Dog(), Cat()]
make_sounds(animals)
# 輸出：
# 汪汪！
# 喵喵！
```

理解類別和物件對於掌握 Python 中的物件導向程式設計至關重要。練習這些範例和練習，以熟練定義類別、建立物件，並有效使用繼承和多型。

---

# 類別和物件的進階主題

在本課程中，我們將深入探討 Python 中類別和物件的一些進階功能，包括特殊方法（也稱為魔術方法或雙底線方法），例如 `__call__`、`__repr__`、`__del__`、`__str__` 和 `__add__`。

## 特殊方法

Python 中的特殊方法是通過在名稱前後加上雙底線（`__`）來定義的。這些方法允許您為內建操作定義物件的行為。

### `__repr__` 和 `__str__`

- `__repr__`：定義物件的「官方」字串表示。用於除錯和開發。
- `__str__`：定義物件的「非正式」或友好的字串表示。由 `print` 函數和 `str()` 使用。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"{self.name}，{self.age} 歲"

person = Person("Alice", 30)
print(repr(person))  # 輸出：Person(name='Alice', age=30)
print(person)        # 輸出：Alice，30 歲
```

### `__call__`

`__call__` 方法允許物件像函數一樣被呼叫。
```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 輸出：1
print(counter())  # 輸出：2
```

### `__del__`

`__del__` 方法在物件即將被銷毀時被呼叫。它對清理動作很有用。
```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"資源 {self.name} 已建立")

    def __del__(self):
        print(f"資源 {self.name} 已銷毀")

resource = Resource("資料庫連接")
del resource  # 輸出：資源 資料庫連接 已銷毀
```

### `__add__`

`__add__` 方法允許您為物件定義 `+` 運算子的行為。
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
print(v3)  # 輸出：Vector(6, 8)
```

## 其他特殊方法

### `__getitem__` 和 `__setitem__`

這些方法允許物件用於索引和項目賦值。
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
print(my_list[0])  # 輸出：1
my_list[1] = 4
print(my_list[1])  # 輸出：4
```

### `__len__`

`__len__` 方法允許您為物件定義 `len()` 函數的行為。
```python
class MyList:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

my_list = MyList()
my_list.items = [1, 2, 3]
print(len(my_list))  # 輸出：3
```

### `__iter__` 和 `__next__`

這些方法允許物件用作迭代器。
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
# 輸出：
# 1
# 2
# 3
```

理解和使用特殊方法允許您為物件定義自訂行為，使它們更直觀和強大。練習這些範例和練習，以熟練在 Python 中使用特殊方法。