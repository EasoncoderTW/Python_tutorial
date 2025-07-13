# 第八課 - 模組和套件

在本課程中，我們將介紹 Python 中模組和套件的基礎，包括如何匯入模組、使用標準函式庫和第三方套件，以及建立和使用自訂模組。

## 匯入模組

### 匯入模組
使用 `import` 敘述匯入模組。這允許您訪問模組中定義的函數、類別和變數。
```python
import math

print(math.sqrt(16))  # 輸出：4.0
```

### 匯入特定屬性
您也可以從模組中匯入特定的屬性。
```python
from math import sqrt

print(sqrt(16))  # 輸出：4.0
```

### 重新命名模組
模組可以使用 `as` 關鍵字重新命名。
```python
import math as m

print(m.sqrt(16))  # 輸出：4.0
```

## 標準函式庫和第三方套件

### 標準函式庫
Python 附帶豐富的標準函式庫。一些常用的標準函式庫包括：
- `math` 用於數學函數
- `datetime` 用於操作日期和時間
- `os` 用於與作業系統互動

### 第三方套件
第三方套件可以使用 `pip`（Python 套件安裝器）安裝。例如，要安裝用於發送 HTTP 請求的 `requests` 套件，您可以執行：
```bash
pip install requests
```

安裝後，您可以在程式碼中匯入和使用該套件。
```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 輸出：200
```

## 建立和使用自訂模組

### 建立自訂模組
您可以將 Python 程式碼儲存在 `.py` 檔案中來建立自己的模組。例如，建立一個名為 `my_module.py` 的檔案，內容如下：
```python
# my_module.py

def greet(name):
    return f"Hello, {name}!"
```

### 使用自訂模組
要使用自訂模組，在另一個 Python 檔案中匯入它。
```python
# main.py

import my_module

print(my_module.greet("Alice"))  # 輸出：Hello, Alice!
```

## 範例和練習

### 範例 1：使用標準函式庫
使用 `datetime` 標準函式庫獲取目前日期和時間。
```python
import datetime

now = datetime.datetime.now()
print(now)  # 輸出：2024-07-04 12:34:56.789012（範例輸出）
```

### 範例 2：安裝和使用第三方套件
安裝 `requests` 套件並使用它發送 GET 請求。
```python
import requests

response = requests.get('https://api.github.com')
print(response.json())  # 輸出：來自 GitHub API 的 JSON 回應
```

### 範例 3：建立和使用自訂模組
建立一個自訂模組，包含計算數字階乘的函數。
```python
# factorial_module.py

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
```python
# main.py

import factorial_module

print(factorial_module.factorial(5))  # 輸出：120
```

### 範例 4：具有多個函數的自訂模組
建立一個自訂模組 `math_utils.py`，包含多個函數：`add`、`subtract`、`multiply` 和 `divide`。
```python
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
```
```python
# main.py

import math_utils

print(math_utils.add(3, 5))        # 輸出：8
print(math_utils.subtract(10, 4))  # 輸出：6
print(math_utils.multiply(2, 7))   # 輸出：14
print(math_utils.divide(20, 5))    # 輸出：4.0
```

### 範例 5：從套件匯入
建立一個名為 `shapes` 的套件，包含兩個模組：`circle.py` 和 `rectangle.py`。每個模組應有計算面積和周長的函數。

#### 目錄結構：
```
shapes/
    __init__.py
    circle.py
    rectangle.py
```

#### circle.py：
```python
# circle.py

import math

def area(radius):
    return math.pi * (radius ** 2)

def perimeter(radius):
    return 2 * math.pi * radius
```

#### rectangle.py：
```python
# rectangle.py

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)
```

#### main.py：
```python
# main.py

from shapes import circle, rectangle

print(circle.area(5))          # 輸出：78.53981633974483
print(circle.perimeter(5))     # 輸出：31.41592653589793
print(rectangle.area(4, 6))    # 輸出：24
print(rectangle.perimeter(4, 6))  # 輸出：20
```

### 練習

#### 練習 1：列表總和
建立一個自訂模組 `list_utils.py`，包含一個接收數字列表並回傳所有數字總和的函數。在另一個腳本中匯入並使用此模組。

#### 解答
```python
# list_utils.py

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```
```python
# main.py

import list_utils

result = list_utils.sum_list([1, 2, 3, 4, 5])
print(result)  # 輸出：15
```

#### 練習 2：檢查質數
建立一個自訂模組 `prime_utils.py`，包含一個接收數字並檢查是否為質數的函數。如果數字是質數，函數應回傳 `True`，否則回傳 `False`。在另一個腳本中匯入並使用此模組。

#### 解答
```python
# prime_utils.py

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
```python
# main.py

import prime_utils

print(prime_utils.is_prime(7))   # 輸出：True
print(prime_utils.is_prime(10))  # 輸出：False
```

#### 練習 3：幾何套件
建立一個名為 `geometry` 的套件，包含兩個模組：`triangle.py` 和 `square.py`。每個模組應有計算面積和周長的函數。在腳本中匯入並使用這些模組。

#### 解答
#### 目錄結構：
```
geometry/
    __init__.py
    triangle.py
    square.py
```

#### triangle.py：
```python
# triangle.py

def area(base, height):
    return 0.5 * base * height

def perimeter(a, b, c):
    return a + b + c
```

#### square.py：
```python
# square.py

def area(side):
    return side ** 2

def perimeter(side):
    return 4 * side
```

#### main.py：
```python
# main.py

from geometry import triangle, square

print(triangle.area(5, 10))      # 輸出：25.0
print(triangle.perimeter(3, 4, 5))  # 輸出：12
print(square.area(4))           # 輸出：16
print(square.perimeter(4))      # 輸出：16
```

#### 練習 4：天氣資料模組
建立一個自訂模組 `weather_utils.py`，包含一個 `get_weather` 函數，接收城市名稱並回傳虛擬天氣報告字串（例如，"The weather in {city} is sunny."）。在腳本中匯入並使用此模組。

#### 解答
```python
# weather_utils.py

def get_weather(city):
    return f"The weather in {city} is sunny."
```
```python
# main.py

import weather_utils

print(weather_utils.get_weather("New York"))  # 輸出：The weather in New York is sunny.
print(weather_utils.get_weather("Paris"))     # 輸出：The weather in Paris is sunny.
```

理解模組和套件對於在 Python 中有效組織和重複使用程式碼至關重要。練習這些範例和練習，以熟練匯入模組、使用標準函式庫和第三方套件，以及建立和使用自訂模組。這將幫助您編寫更清潔、更易維護的程式碼，並與其他開發人員更有效地協作。