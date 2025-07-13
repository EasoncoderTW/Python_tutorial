# 第四課：條件敘述

在本課程中，我們將介紹 Python 中條件敘述的基礎，包括 `if`、`elif` 和 `else` 敘述的使用、比較和邏輯運算子，以及嵌套條件敘述。

## 使用 `if`、`elif` 和 `else` 敘述

### If 敘述
`if` 敘述評估一個條件，如果條件為 `True`，則執行其中的程式碼區塊。
```python
x = 10
if x > 5:
    print("x 大於 5")
```

### Elif 敘述
`elif`（"else if" 的縮寫）敘述讓您檢查多個條件。如果前面的 `if` 條件為 `False`，則評估 `elif` 條件。
```python
x = 10
if x > 15:
    print("x 大於 15")
elif x > 5:
    print("x 大於 5 但小於或等於 15")
```

### Else 敘述
如果前面的所有條件都不為 `True`，`else` 敘述執行一個程式碼區塊。
```python
x = 3
if x > 5:
    print("x 大於 5")
elif x > 2:
    print("x 大於 2 但小於或等於 5")
else:
    print("x 為 2 或更小")
```

## 比較和邏輯運算子

### 比較運算子
比較運算子用於比較值，它們返回 `True` 或 `False`。
- `==`：等於
- `!=`：不等於
- `>`：大於
- `<`：小於
- `>=`：大於或等於
- `<=`：小於或等於

### 邏輯運算子
邏輯運算子用於組合條件敘述。
- `and`：如果兩個條件都為 `True`，則返回 `True`
- `or`：如果至少有一個條件為 `True`，則返回 `True`
- `not`：如果條件為 `False`，則返回 `True`

### 範例
```python
# 比較運算子
a = 10
b = 5
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False

# 邏輯運算子
x = 7
print(x > 5 and x < 10)  # True
print(x < 5 or x > 10)   # False
print(not (x < 5))       # True
```

## 嵌套條件敘述

嵌套條件敘述是在其他 `if` 敘述內部的 `if` 敘述。這允許進行更複雜的條件檢查。
```python
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x 大於 5 且 y 大於 15")
    else:
        print("x 大於 5 但 y 小於或等於 15")
else:
    print("x 小於或等於 5")
```

## 範例和練習

### 範例 1：基本條件敘述
編寫一個程式來檢查一個數字是正數、負數還是零。
```python
num = 7
if num > 0:
    print("這個數字是正數")
elif num < 0:
    print("這個數字是負數")
else:
    print("這個數字是零")
```

### 範例 2：邏輯運算子
編寫一個程式來檢查一個數字是否在 10 到 20 之間（包含端點）。
```python
num = 15
if num >= 10 and num <= 20:
    print("這個數字在 10 到 20 之間")
else:
    print("這個數字不在 10 到 20 之間")
```

### 範例 3：嵌套條件敘述
編寫一個程式將一個人的年齡分類為兒童、青少年或成人。
```python
age = 16
if age < 13:
    print("兒童")
elif age < 20:
    print("青少年")
else:
    print("成人")
```

### 練習

#### 練習 1：成績檢查器
編寫一個程式，輸入分數（0-100）並印出對應的等級：
- 90-100：A
- 80-89：B
- 70-79：C
- 60-69：D
- 0-59：F

#### 解答
```python
score = 85
if score >= 90:
    print("等級：A")
elif score >= 80:
    print("等級：B")
elif score >= 70:
    print("等級：C")
elif score >= 60:
    print("等級：D")
else:
    print("等級：F")
```

#### 練習 2：奇數或偶數
編寫一個程式來檢查一個數字是奇數還是偶數。
```python
number = 42
if number % 2 == 0:
    print("這個數字是偶數")
else:
    print("這個數字是奇數")
```

#### 練習 3：閏年檢查器
編寫一個程式來檢查一年是否為閏年。
- 如果一年能被 4 整除但不能被 100 整除，或者能被 400 整除，則為閏年。

#### 解答
```python
year = 2000
if year % 400 == 0:
    print(f"{year} 是閏年")
elif year % 100 == 0:
    print(f"{year} 不是閏年")
elif year % 4 == 0:
    print(f"{year} 是閏年")
else:
    print(f"{year} 不是閏年")
```

理解條件敘述對於控制 Python 程式的流程至關重要。練習這些範例和練習，以熟練使用 `if`、`elif` 和 `else` 敘述。