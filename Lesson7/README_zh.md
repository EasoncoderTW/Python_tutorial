# 第七課：Python 的魔法函數！🪄✨

歡迎來到 Python 函數的魔法世界！今天，我們將學習如何創造魔法咒語（函數），讓你的程式更聰明、更快速、更有趣！🧙‍♂️

## 函數為什麼如此神奇？🪄

想像你是一位巫師：
- 你施展咒語來問候朋友（打招呼）。
- 你使用藥水來計算你的金幣（加法運算）。
- 你召喚一隻龍來保護你的城堡（重複使用程式碼）。

函數就是 Python 中的咒語！它們讓你可以重複使用程式碼、簡化任務，並讓你的程式超級強大！🐉

## 函數的基礎 🧙‍♀️

### 定義函數：你的魔法咒語書 📖
函數就像在咒語書中寫下咒語。使用 `def` 關鍵字，給你的咒語取個名字，並在大括號中寫下魔法。
```python
# 一個簡單的問候咒語
def greet():
    print("Hello, world! 🌍")
```

### 呼叫函數：施展你的咒語 🪄
要施展咒語，只需呼叫它的名字並加上括號。
```python
greet()  # 輸出：Hello, world! 🌍
```

## 函數參數：自訂你的咒語 🧪

### 參數：你的藥水成分 🧪
在函數中添加參數以自訂其行為。
```python
# 一個個性化的問候咒語
def greet(name):
    print(f"Hello, {name}! 🌟")
```
```python
greet("Alice")  # 輸出：Hello, Alice! 🌟
```

### 預設參數：你的備案 🛡️
為參數設置預設值，使你的咒語更靈活。
```python
def greet(name="World"):
    print(f"Hello, {name}! 🌟")
```
```python
greet()         # 輸出：Hello, World! 🌟
greet("Alice")  # 輸出：Hello, Alice! 🌟
```

## 返回值：寶藏箱 🎁

### 返回值：收集你的獎勵 💰
函數可以返回值，就像施展咒語後收集寶藏一樣。
```python
# 一個加法咒語
def add(a, b):
    return a + b
```
```python
result = add(3, 4)
print(result)  # 輸出：7
```

## 變數的作用域與生命週期：魔法圈 🔮

### 局部作用域：魔法圈內 🌀
函數內的變數受到魔法圈保護，無法在外部訪問。
```python
def my_function():
    x = 10
    print(x)

my_function()  # 輸出：10
print(x)       # 錯誤：NameError: name 'x' is not defined
```

### 全域作用域：巫師的領域 🌍
函數外的變數可以在任何地方訪問。
```python
x = 10

def my_function():
    print(x)

my_function()  # 輸出：10
print(x)       # 輸出：10
```

### `global` 關鍵字：擴展魔法圈 🪄
使用 `global` 在函數內修改全域變數。
```python
x = 10

def my_function():
    global x
    x = 5

my_function()
print(x)  # 輸出：5
```

## 有趣的挑戰：提升你的巫術！🧙‍♂️

### 挑戰 1：平方咒語 🟦
撰寫一個函數，接收一個數字並輸出其平方。
```python
def print_square(number):
    print(number ** 2)
```
```python
print_square(4)  # 輸出：16
```

### 挑戰 2：乘法藥水 🧪
撰寫一個函數，接收兩個數字並返回它們的乘積。
```python
def multiply(a, b):
    return a * b
```
```python
result = multiply(3, 5)
print(result)  # 輸出：15
```

### 挑戰 3：質數檢測器 🔍
撰寫一個函數，檢查一個數字是否為質數。
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

函數是撰寫可重複使用和模組化程式碼的關鍵。練習這些範例和挑戰，成為程式設計的巫師大師吧！🧙‍♀️