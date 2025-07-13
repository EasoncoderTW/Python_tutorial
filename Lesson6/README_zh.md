# 第六課：迴圈敘述

在本課程中，我們將介紹 Python 中迴圈敘述的基礎，包括 `for` 和 `while` 迴圈的使用、迴圈控制敘述如 `break` 和 `continue`，以及嵌套迴圈。

## 使用 `for` 和 `while` 迴圈

### For 迴圈
`for` 迴圈用於迭代序列（如列表、元組、字典、集合或字串）。

#### 範例：For 迴圈
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
輸出：
```
apple
banana
cherry
```

### While 迴圈
`while` 迴圈在條件為 `True` 時重複執行程式碼區塊。

#### 範例：While 迴圈
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
輸出：
```
0
1
2
3
4
```

## 迴圈控制敘述：`break` 和 `continue`

### Break 敘述
`break` 敘述用於在迴圈完成所有項目的迭代之前退出迴圈。

#### 範例：Break 敘述
```python
for num in range(10):
    if num == 5:
        break
    print(num)
```
輸出：
```
0
1
2
3
4
```

### Continue 敘述
`continue` 敘述用於跳過迴圈的當前迭代並繼續下一個迭代。

#### 範例：Continue 敘述
```python
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```
輸出：
```
1
3
5
7
9
```

## 嵌套迴圈
嵌套迴圈是在另一個迴圈內部的迴圈。內部迴圈對外部迴圈的每次迭代都會執行一次。

#### 範例：嵌套迴圈
```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```
輸出：
```
i = 0, j = 0
i = 0, j = 1
i = 1, j = 0
i = 1, j = 1
i = 2, j = 0
i = 2, j = 1
```

## 範例和練習

### 範例 1：使用 `for` 迴圈
編寫程式印出列表中每個數字的平方。
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number ** 2)
```
輸出：
```
1
4
9
16
25
```

### 範例 2：使用 `while` 迴圈
編寫程式使用 `while` 迴圈印出從 10 到 1 的數字。
```python
count = 10
while count > 0:
    print(count)
    count -= 1
```
輸出：
```
10
9
8
7
6
5
4
3
2
1
```

### 範例 3：使用 `break` 敘述
編寫程式找出列表中第一個能被 3 整除的數字並印出。找到該數字後停止迴圈。
```python
numbers = [1, 2, 4, 8, 9, 12]
for number in numbers:
    if number % 3 == 0:
        print(f"第一個能被 3 整除的數字：{number}")
        break
```
輸出：
```
第一個能被 3 整除的數字：9
```

### 範例 4：使用 `continue` 敘述
編寫程式使用 `for` 迴圈印出 0 到 10 之間的所有奇數。
```python
for num in range(11):
    if num % 2 == 0:
        continue
    print(num)
```
輸出：
```
1
3
5
7
9
```

### 範例 5：嵌套迴圈
編寫程式使用嵌套迴圈印出 3x3 矩陣。
```python
for i in range(3):
    for j in range(3):
        print(f"{i},{j}", end=" ")
    print()
```
輸出：
```
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
```

### 練習

#### 練習 1：數字總和
編寫程式使用 `while` 迴圈找出 1 到 100 所有數字的總和。

#### 解答
```python
total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(f"1 到 100 的數字總和：{total}")
```
輸出：
```
1 到 100 的數字總和：5050
```

#### 練習 2：乘法表
編寫程式使用嵌套迴圈生成 1 到 5 的乘法表。

#### 解答
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j}", end="\t")
    print()
```
輸出：
```
1	2	3	4	5
2	4	6	8	10
3	6	9	12	15
4	8	12	16	20
5	10	15	20	25
```

#### 練習 3：階乘計算
編寫程式使用 `for` 迴圈計算給定數字的階乘。

#### 解答
```python
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num} 的階乘是 {factorial}")
```
輸出：
```
5 的階乘是 120
```

理解迴圈以及如何控制它們對於有效管理 Python 中的重複任務至關重要。練習這些範例和練習，以熟練使用 `for` 和 `while` 迴圈，以及迴圈控制敘述和嵌套迴圈。