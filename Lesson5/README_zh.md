# 第五課：列表和類似陣列的結構

在本課程中，我們將介紹 Python 中列表的基礎知識、列表方法和操作，以及元組、字典和集合的介紹。

## 列表介紹

### 什麼是列表？
列表是按特定順序排列的項目集合。列表是可變的，意味著它們在創建後可以被修改。列表通過將元素包含在方括號（`[]`）中來定義。

### 創建列表
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # 輸出：['apple', 'banana', 'cherry']
```

### 訪問元素
```python
print(fruits[0])  # 輸出：apple
print(fruits[1])  # 輸出：banana
print(fruits[-1])  # 輸出：cherry
```

### 修改元素
```python
fruits[1] = "blueberry"
print(fruits)  # 輸出：['apple', 'blueberry', 'cherry']
```

## 列表方法和操作

### 添加元素
- **append()**：將元素添加到列表的末尾。
  ```python
  fruits.append("orange")
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry', 'orange']
  ```

- **insert()**：在指定位置插入元素。
  ```python
  fruits.insert(1, "banana")
  print(fruits)  # 輸出：['apple', 'banana', 'blueberry', 'cherry', 'orange']
  ```

### 刪除元素
- **remove()**：刪除第一個出現的元素。
  ```python
  fruits.remove("banana")
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry', 'orange']
  ```

- **pop()**：刪除並返回最後一個項目，或指定位置的項目。
  ```python
  popped_fruit = fruits.pop()
  print(popped_fruit)  # 輸出：orange
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry']
  ```

### 其他有用的方法
- **sort()**：按升序排序列表。
  ```python
  fruits.sort()
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry']
  ```

- **reverse()**：反轉列表的順序。
  ```python
  fruits.reverse()
  print(fruits)  # 輸出：['cherry', 'blueberry', 'apple']
  ```

- **len()**：返回列表中元素的數量。
  ```python
  print(len(fruits))  # 輸出：3
  ```

### 列表推導式
列表推導式提供了一種簡潔的方式來創建列表。
```python
squares = [x**2 for x in range(10)]
print(squares)  # 輸出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 理解元組、字典和集合

### 元組
元組是不可變的序列，通常用於存儲異質資料的集合。元組通過將元素包含在括號（`()`）中來定義。

```python
tuple_example = (1, "apple", 3.14)
print(tuple_example)  # 輸出：(1, 'apple', 3.14)
print(tuple_example[1])  # 輸出：apple
```

### 字典
字典是鍵值對的無序集合。字典通過將鍵值對包含在大括號（`{}`）中來定義。

```python
dict_example = {"name": "Alice", "age": 25, "city": "New York"}
print(dict_example)  # 輸出：{'name': 'Alice', 'age': 25, 'city': 'New York'}
print(dict_example["name"])  # 輸出：Alice

# 添加新的鍵值對
dict_example["email"] = "alice@example.com"
print(dict_example)  # 輸出：{'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
```

### 集合
集合是唯一元素的無序集合。集合通過將元素包含在大括號（`{}`）中來定義。

```python
set_example = {"apple", "banana", "cherry"}
print(set_example)  # 輸出：{'apple', 'cherry', 'banana'}

# 向集合添加元素
set_example.add("orange")
print(set_example)  # 輸出：{'apple', 'cherry', 'banana', 'orange'}

# 從集合中刪除元素
set_example.remove("banana")
print(set_example)  # 輸出：{'apple', 'cherry', 'orange'}
```

## 範例和練習

### 範例 1：列表操作
創建一個數字列表並執行各種操作。
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(2, 2.5)
numbers.remove(4)
print(numbers)  # 輸出：[1, 2, 2.5, 3, 5, 6]
```

### 範例 2：元組和字典
創建一個元組和字典，然後訪問它們的元素。
```python
tuple_example = (10, 20, 30)
dict_example = {"first": 10, "second": 20, "third": 30}

print(tuple_example[1])  # 輸出：20
print(dict_example["second"])  # 輸出：20
```

### 範例 3：集合操作
創建一個集合並執行各種操作。
```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)  # 輸出：{'apple', 'cherry', 'orange'}
```

### 練習

#### 練習 1：列表操作
1. 創建一個包含五部您最喜歡電影的列表。
2. 向列表中添加一部新電影。
3. 從列表中刪除第二部電影。
4. 印出最終的電影列表。

#### 解答
```python
movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "The Dark Knight"]
movies.append("Pulp Fiction")
movies.pop(1)
print(movies)  # 輸出：['Inception', 'Interstellar', 'The Godfather', 'The Dark Knight', 'Pulp Fiction']
```

#### 練習 2：字典使用
1. 創建一個包含三個鍵值對的字典：姓名、年齡和城市。
2. 添加一個新的電子郵件鍵值對。
3. 更新年齡值。
4. 印出最終的字典。

#### 解答
```python
person = {"name": "John", "age": 30, "city": "New York"}
person["email"] = "john@example.com"
person["age"] = 31
print(person)  # 輸出：{'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}
```

#### 練習 3：集合操作
1. 創建一個包含五種不同顏色的集合。
2. 向集合中添加一種新顏色。
3. 從集合中刪除一種現有顏色。
4. 印出最終的顏色集合。

#### 解答
```python
colors = {"red", "blue", "green", "yellow", "purple"}
colors.add("orange")
colors.remove("green")
print(colors)  # 輸出：{'red', 'blue', 'yellow', 'purple', 'orange'}
```

#### 練習 4：前三名學生
- 假設您有以下格式的字典，包含學生姓名和成績：
```python
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Carol": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 91,
}

###  在此處添加您的程式碼 ###
```
- 完成程式碼以找出前三名的學生

理解 Python 中的列表和其他類似陣列的結構對於處理資料集合是基礎的。練習這些範例和練習，以熟練使用列表、元組、字典和集合。