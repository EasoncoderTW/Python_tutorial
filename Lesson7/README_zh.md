# 第七課：函數

在本課程中，我們將介紹 Python 中函數的基礎，包括如何定義和呼叫函數、如何處理函數參數和回傳值，以及理解變數的作用域和生命週期。

## 定義和呼叫函數

### 定義函數
函數使用 `def` 關鍵字定義，後面跟著函數名稱、括號和冒號。每個函數內的程式碼區塊都以縮排開始。
```python
def greet():
    print("Hello, world!")
```

### 呼叫函數
函數通過使用函數名稱後跟括號來呼叫。
```python
greet()  # 輸出：Hello, world!
```

## 函數參數和回傳值

### 參數
參數在函數定義的括號內指定。它們充當在呼叫函數時傳遞給函數的值的佔位符。
```python
def greet(name):
    print(f"Hello, {name}!")
```
```python
greet("Alice")  # 輸出：Hello, Alice!
```

### 回傳值
函數可以使用 `return` 敘述回傳一個值。
```python
def add(a, b):
    return a + b
```
```python
result = add(3, 4)
print(result)  # 輸出：7
```

### 預設參數
函數可以有預設參數值，如果在呼叫函數時沒有為參數提供引數，就會使用這些預設值。
```python
def greet(name="World"):
    print(f"Hello, {name}!")
```
```python
greet()         # 輸出：Hello, World!
greet("Alice")  # 輸出：Hello, Alice!
```

## 變數的作用域和生命週期

### 區域作用域
在函數內部定義的變數處於該函數的區域作用域中，在函數外部無法訪問。
```python
def my_function():
    x = 10
    print(x)

my_function()  # 輸出：10
print(x)       # 錯誤：NameError: name 'x' is not defined
```

### 全域作用域
在任何函數外部定義的變數處於全域作用域中，可以從程式碼的任何地方訪問。
```python
x = 10

def my_function():
    print(x)

my_function()  # 輸出：10
print(x)       # 輸出：10
```

### `global` 關鍵字
要在函數內部修改全域變數，請使用 `global` 關鍵字。
```python
x = 10

def my_function():
    global x
    x = 5

my_function()
print(x)  # 輸出：5
```

### 變數的生命週期
變數的生命週期是變數在記憶體中存在的時間。函數內部定義的變數只在函數執行期間存在。

## 範例和練習

### 範例 1：基本函數
定義一個接收數字並印出其平方的函數。
```python
def print_square(number):
    print(number ** 2)
```
```python
print_square(4)  # 輸出：16
```

### 範例 2：帶回傳值的函數
定義一個接收兩個數字並回傳它們乘積的函數。
```python
def multiply(a, b):
    return a * b
```
```python
result = multiply(3, 5)
print(result)  # 輸出：15
```

### 範例 3：變數作用域
展示區域作用域和全域作用域的差異。
```python
x = 10

def my_function():
    x = 5
    print(f"函數內部：{x}")

my_function()  # 輸出：函數內部：5
print(f"函數外部：{x}")  # 輸出：函數外部：10
```

### 練習

#### 練習 1：列表總和
編寫一個接收數字列表並回傳列表中所有數字總和的函數。

#### 解答
```python
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```
```python
result = sum_list([1, 2, 3, 4, 5])
print(result)  # 輸出：15
```

#### 練習 2：階乘函數
編寫一個接收數字並回傳其階乘的函數。

#### 解答
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
```python
result = factorial(5)
print(result)  # 輸出：120
```

#### 練習 3：檢查質數
編寫一個接收數字並檢查它是否為質數的函數。如果數字是質數，函數應該回傳 `True`，否則回傳 `False`。

#### 解答
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
```python
result = is_prime(7)
print(result)  # 輸出：True
result = is_prime(10)
print(result)  # 輸出：False
```

理解函數及其有效使用對於在 Python 中編寫可重複使用和模組化的程式碼至關重要。練習這些範例和練習，以熟練定義和呼叫函數、處理參數和回傳值，以及管理變數的作用域和生命週期。