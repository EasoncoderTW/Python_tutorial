# 第二課：類型和物件

在 Python 中，每個值都有資料型別，這定義了該值的特性，例如可以對其執行什麼操作。Python 是一個動態型別語言，意味著您不必明確宣告變數的資料型別。Python 會根據指派給變數的值自動確定資料型別。

## Python 中的型別

### 1. Int（整數）
整數是沒有小數點的完整數字。它們可以是正數或負數。整數的例子有 5、-3、100 等。

### 2. Float（浮點數）
浮點數是有小數點或使用科學記號的數字。浮點數的例子有 3.14、-0.001、2.5e2 等。

### 3. Str（字串）
字串是用單引號（''）、雙引號（""）或三引號（''' 或 """）包圍的字符序列。字串的例子有 "hello"、'Python'、"123" 等。

### 4. Bool（布林值）
布林值代表兩個值中的一個：True 或 False。它們通常用於條件敘述和比較中。

### 範例
```python
# 整數
x = 5
y = -3
print(type(x))  # <class 'int'>

# 浮點數
pi = 3.14
value = 2.5e2
print(type(value))  # <class 'float'>

# 字串
name = "Alice"
message = 'Hello, World!'
print(type(message))  # <class 'str'>

# 布林值
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>
```

## Python 中的型別轉換

型別轉換，也稱為型別轉型，是將值從一種資料型別轉換為另一種資料型別的過程。Python 提供了幾個內建的型別轉換函數。

### 常見的型別轉換函數

1. `int()`：將值轉換為整數。
2. `float()`：將值轉換為浮點數。
3. `str()`：將值轉換為字串。
4. `bool()`：將值轉換為布林值。

### 範例
```python
# 將浮點數轉換為整數
pi = 3.14
pi_int = int(pi)
print(pi_int)  # 3

# 將整數轉換為浮點數
num = 10
num_float = float(num)
print(num_float)  # 10.0

# 將整數轉換為字串
number = 123
number_str = str(number)
print(number_str)  # "123"

# 將字串轉換為整數
string = "456"
string_int = int(string)
print(string_int)  # 456

# 將字串轉換為浮點數
string_float = float(string)
print(string_float)  # 456.0

# 將不同值轉換為布林值
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("Hello"))  # True
```

在本教學中，我們介紹了 Python 中的基本資料型別 - int、float、str 和 bool。理解這些資料型別對於編寫 Python 程式至關重要。歡迎進一步探索這些型別以及如何在 Python 中使用它們。

## 練習

1. **識別資料型別**：
   確定以下值在 Python 中的資料型別：
   - 42
   - 3.14159
   - "Python"
   - True
   - '123'

2. **型別轉換練習**：
   轉換以下值並印出它們的新資料型別：
   - 將 `7.5` 轉換為整數。
   - 將 `100` 轉換為字串。
   - 將 `"False"` 轉換為布林值。
   - 將 `0` 轉換為布林值。